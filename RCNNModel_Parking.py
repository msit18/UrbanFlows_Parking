import sys
sys.path.append('/home/ubuntu/py-faster-rcnn/caffe-fast-rcnn/python')
sys.path.append('/home/ubuntu/py-faster-rcnn/tools')
import caffe, cv2

import _init_paths
from fast_rcnn.config import cfg, get_output_dir
from fast_rcnn.bbox_transform import clip_boxes, bbox_transform_inv
from fast_rcnn.nms_wrapper import nms
from utils.timer import Timer

from utils.blob import im_list_to_blob

import numpy as np
import Parameters as p

class RCNNModel():
    #     CLASSES = ('__background__',
#                     'aeroplane', 'bicycle', 'bird', 'boat',
#                    'bottle', 'bus', 'car', 'cat', 'chair',
#                    'cow', 'diningtable', 'dog', 'horse',
#                    'motorbike', 'person', 'pottedplant',
#                    'sheep', 'sofa', 'train', 'tvmonitor')
#     self.net = None
    class_car_index = 7
    def __init__(self,prototxt,caffemodel):
        self.net = self.initCaffeLib(prototxt, caffemodel)

    def initCaffeLib(self, prototxt, caffemodel):
        cfg.TEST.HAS_RPN = True
        caffe.set_mode_gpu()
        caffe.set_device(0)
        net = caffe.Net(prototxt, caffemodel, caffe.TEST)
        im = 128 * np.ones((300, 500, 3), dtype=np.uint8)
        for i in xrange(2):
            _, _, _= self.im_detect(net, im)
        print '\n\nLoaded network {:s}'.format(caffemodel)
        return net
        
    def carDetectionMethod(self, im ):
        scores, boxes, deepFeatures = self.im_detect(self.net, im)
        # Visualize detections for each class
        # 0.7, 0.3, 0.5
        # CONF_THRESH = 0.7 #Doesn't matter here
        # NMS_THRESH = 0.2
        # OBJ_THRESH = 0.4
        NMS_THRESH = p.RCNN_NMS_Thresh
        OBJ_THRESH = p.RCNN_OBJ_Thresh
        detectedCarsInThisFrame = []
        
        cls_ind = self.class_car_index
        cls_boxes = boxes[:, 4*cls_ind:4*(cls_ind + 1)]
        cls_scores = scores[:, cls_ind]

        dets = np.hstack((cls_boxes,
                          cls_scores[:, np.newaxis],deepFeatures)).astype(np.float32) #stacks them together
        keep = nms(dets, NMS_THRESH) #Removes overlapping bounding boxes
        dets = dets[keep, :]
        obj_inds = np.where(dets[:, 4] >= OBJ_THRESH)[0] #Threshold applied to score values here
        return dets[obj_inds,:]
    

    def _get_image_blob(self,im):
        """Converts an image into a network input.

        Arguments:
            im (ndarray): a color image in BGR order

        Returns:
            blob (ndarray): a data blob holding an image pyramid
            im_scale_factors (list): list of image scales (relative to im) used
                in the image pyramid
        """
        im_orig = im.astype(np.float32, copy=True)
        im_orig -= cfg.PIXEL_MEANS

        im_shape = im_orig.shape
        im_size_min = np.min(im_shape[0:2])
        im_size_max = np.max(im_shape[0:2])

        processed_ims = []
        im_scale_factors = []

        for target_size in cfg.TEST.SCALES:
            im_scale = float(target_size) / float(im_size_min)
            # Prevent the biggest axis from being more than MAX_SIZE
            if np.round(im_scale * im_size_max) > cfg.TEST.MAX_SIZE:
                im_scale = float(cfg.TEST.MAX_SIZE) / float(im_size_max)
            im = cv2.resize(im_orig, None, None, fx=im_scale, fy=im_scale,
                            interpolation=cv2.INTER_LINEAR)
            im_scale_factors.append(im_scale)
            processed_ims.append(im)

        # Create a blob to hold the input images
        blob = im_list_to_blob(processed_ims)

        return blob, np.array(im_scale_factors)

    def _get_blobs(self,im, rois):
        """Convert an image and RoIs within that image into network inputs."""
        blobs = {'data' : None, 'rois' : None}
        blobs['data'], im_scale_factors = self._get_image_blob(im)
        if not cfg.TEST.HAS_RPN:
            blobs['rois'] = self._get_rois_blob(rois, im_scale_factors)
        return blobs, im_scale_factors

    def im_detect(self, net, im, boxes=None):
        """Detect object classes in an image given object proposals.

        Arguments:
            net (caffe.Net): Fast R-CNN network to use
            im (ndarray): color image to test (in BGR order)
            boxes (ndarray): R x 4 array of object proposals or None (for RPN)

        Returns:
            scores (ndarray): R x K array of object class scores (K includes
                background as object category 0)
            boxes (ndarray): R x (4*K) array of predicted bounding boxes
        """
        blobs, im_scales = self._get_blobs(im, boxes)

        # When mapping from image ROIs to feature map ROIs, there's some aliasing
        # (some distinct image ROIs get mapped to the same feature ROI).
        # Here, we identify duplicate feature ROIs, so we only compute features
        # on the unique subset.
        if cfg.DEDUP_BOXES > 0 and not cfg.TEST.HAS_RPN:
            v = np.array([1, 1e3, 1e6, 1e9, 1e12])
            hashes = np.round(blobs['rois'] * cfg.DEDUP_BOXES).dot(v)
            _, index, inv_index = np.unique(hashes, return_index=True,
                                            return_inverse=True)
            blobs['rois'] = blobs['rois'][index, :]
            boxes = boxes[index, :]

        if cfg.TEST.HAS_RPN:
            im_blob = blobs['data']
            blobs['im_info'] = np.array(
                [[im_blob.shape[2], im_blob.shape[3], im_scales[0]]],
                dtype=np.float32)

        # reshape network inputs
        net.blobs['data'].reshape(*(blobs['data'].shape))
        if cfg.TEST.HAS_RPN:
            net.blobs['im_info'].reshape(*(blobs['im_info'].shape))
        else:
            net.blobs['rois'].reshape(*(blobs['rois'].shape))

        # do forward
        forward_kwargs = {'data': blobs['data'].astype(np.float32, copy=False)}
        if cfg.TEST.HAS_RPN:
            forward_kwargs['im_info'] = blobs['im_info'].astype(np.float32, copy=False)
        else:
            forward_kwargs['rois'] = blobs['rois'].astype(np.float32, copy=False)
        blobs_out = net.forward(**forward_kwargs)

        if cfg.TEST.HAS_RPN:
            assert len(im_scales) == 1, "Only single-image batch implemented"
            rois = net.blobs['rois'].data.copy()
            # unscale back to raw image space
            boxes = rois[:, 1:5] / im_scales[0]

        if cfg.TEST.SVM:
            # use the raw scores before softmax under the assumption they
            # were trained as linear SVMs
            scores = net.blobs['cls_score'].data
        else:
            # use softmax estimated probabilities
            scores = blobs_out['cls_prob']

        if cfg.TEST.BBOX_REG:
            # Apply bounding-box regression deltas
            box_deltas = blobs_out['bbox_pred']
            pred_boxes = bbox_transform_inv(boxes, box_deltas)
            pred_boxes = clip_boxes(pred_boxes, im.shape)
        else:
            # Simply repeat the boxes, once for each class
            pred_boxes = np.tile(boxes, (1, scores.shape[1]))

        if cfg.DEDUP_BOXES > 0 and not cfg.TEST.HAS_RPN:
            # Map scores and predictions back to the original set of boxes
            scores = scores[inv_index, :]
            pred_boxes = pred_boxes[inv_index, :]

        return scores, pred_boxes, net.blobs['fc6'].data
    