
# coding: utf-8

# In[ ]:

import numpy as np
import cv2

class BackgroundSubtractionCPU():
    
    def __init__(self, bkgdImg):
        self.backgroundImg = bkgdImg
    
    def findMaxBBox(self, boxA, boxB):
        boxC = []
        print "There was an overlap"
        print "BoxA: ", boxA
        print "BoxB: ", boxB
        boxC.append(min(boxA[0], boxB[0]))
        boxC.append(min(boxA[1], boxB[1]))
        boxC.append(max(boxA[2], boxB[2]))
        boxC.append(max(boxA[3], boxB[3]))
        print "BoxC: ", boxC
        return boxC

    def bb_intersection_over_union(self, boxA, boxB):
        # determine the (x, y)-coordinates of the intersection rectangle
        xA = max(boxA[0], boxB[0])
        yA = max(boxA[1], boxB[1])
        xB = min(boxA[2], boxB[2])
        yB = min(boxA[3], boxB[3])

        # compute the area of intersection rectangle
        interArea = (xB - xA + 1) * (yB - yA + 1)

        # compute the area of both the prediction and ground-truth rectangles
        boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
        boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

        # compute the intersection over union by taking the intersection
        # area and dividing it by the sum of prediction + ground-truth
        # areas - the interesection area
        iou = interArea / float(boxAArea + boxBArea - interArea)

        if iou > 0:
            return self.findMaxBBox(boxA, boxB)
        else:
            print "There was no overlap"
            return 0

    ###Blurring and finding edges
    def blurAndThresholdNoise(self, image1blur, image2blur, highThresh, lowThresh):
        print "highThresh: ", highThresh
        print "lowThresh: ", lowThresh
        npblur1 = np.asarray(image1blur)
        npblur2 = np.asarray(image2blur)
        npdiff = npblur2-npblur1

        _threshold = np.where(npdiff < highThresh, 0, npdiff)
        thresholdImage = np.where(_threshold < lowThresh, 0, _threshold)
        return thresholdImage

    def contoursToBBox(self, contours, image):
        bboxArray = []
        for c in range(len(contours)):
            cnt = contours[c]
            x,y,w,h = cv2.boundingRect(cnt)
            bboxArray.append([x, y, x+w, y+h])
            cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
        return bboxArray

    def findLargestXBbox(self, array, image):
        biggestAreaBbox = [0, 0, 0, 0]
        biggestArea = 130
        for x in range(len(array)):
            w = array[x][2] - array[x][0]

            if w > biggestArea:
                biggestArea = w
                biggestAreaBbox = array[x]

        print "area: ", biggestArea
        print "biggestArea: ", biggestAreaBbox
        cv2.rectangle(image,(biggestAreaBbox[0], biggestAreaBbox[1]),(biggestAreaBbox[2], biggestAreaBbox[3]),(0, 255, 255),2)
        return biggestAreaBbox

    #include filter in this to make sure it returns a large enough bbox
    def findBiggestBbox(self, array, image, maxXCoord, maxYCoord):
        defaultArray = [maxXCoord, maxYCoord, 0, 0]
        currentLargestBbox = defaultArray

        for x in range(len(array)):
            resultBbox = self.findMaxBBox(array[x], currentLargestBbox)
            print "largestBbox so far: ", resultBbox
            currentLargestBbox = resultBbox

        w = currentLargestBbox[2] - currentLargestBbox[0]

        print "This was the width value: ", w
        print "maxXCoord: ", maxXCoord
        print "maxXCoord*0.75: ", maxXCoord*0.75
        print "percentage of detection: ", float(w)/maxXCoord
        print "Compare width: ", maxXCoord*0.75 < w
        if (maxXCoord*0.75 < w) == False:
            print "IS TRUE. BOX IS TOO SMALL. RETURNING FALSE"
            currentLargestBbox = defaultArray

        print "largestBbox: ", currentLargestBbox
        cv2.rectangle(image,(currentLargestBbox[0], currentLargestBbox[1]),(currentLargestBbox[2], currentLargestBbox[3]),(255, 0, 0),2)
        return currentLargestBbox

    def recursiveFailSafe(self, blur1, blur2, smolSlice):
        print "RUNNING RECURSIVEFAILSAFE"
        highEdgeLimit = 100
        lowEdgeLimit = 80
        largestXBbox = [0,0,0,0]

        while (highEdgeLimit < 255) & (lowEdgeLimit >= 0) & (largestXBbox == [0,0,0,0]):
            print "nothing matched. area was 0. black image"
            print "use edges and find contours"

            ###Thresholding
            diffImage = blur1
            for y in range(len(diffImage)):
                for x in range(len(diffImage[1])):
                    diff = blur2[y][x] - blur1[y][x]
                    if diff < highEdgeLimit | lowEdgeLimit > 80:
                        diffImage[y][x] = 0
                    else:
                        diffImage[y][x] = diff

            #Edges and finding contours
            diffEdges = cv2.Canny(diffImage, 100, 200)
            diffContours, diffHierarchy = cv2.findContours(diffEdges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

            #Find bbox of all contour returns, and draw all bbox found
            diffColor = cv2.cvtColor(diffImage, cv2.COLOR_GRAY2BGR)
            npbbox = self.contoursToBBox(diffContours, diffColor)
            print "NPBBOX : ", npbbox

            runAgain = False
            if len(npbbox) > 0:
                npbbox = np.array(npbbox)
                sortedNpBbox = npbbox[npbbox[:, 0].argsort()]

                print "DiffColor1: ", diffColor.shape[1]
                print "diffColor2: ", diffColor.shape[0]

                largestBboxTotal = self.findBiggestBbox(sortedNpBbox, diffColor, diffColor.shape[1], diffColor.shape[0])
                print "largestBboxTotal: ", largestBboxTotal
                print "TF: ", largestBboxTotal != [diffColor.shape[1], diffColor.shape[0],0,0]

                if largestBboxTotal != [diffColor.shape[1], diffColor.shape[0],0,0]:
                    return largestBboxTotal
                else:
                    runAgain = True
            else:
                runAgain = True

            if runAgain == True:
                print "BBOX IS EMPTY. THRESHOLD NEEDS TO BE FURTHER AJUSTED"
                ##adjust the parameters for filtering
                highEdgeLimit += 20
                lowEdgeLimit -= 20
                print "HighEdgeLimit: ", highEdgeLimit
                print "lowEdgeLimit: ", lowEdgeLimit

                if (highEdgeLimit > 225) & (lowEdgeLimit < 0):
                    print "RECURSIVE HAS MAXED OUT PARAMETERS. CANNOT DETECT EDGES"
                    break
                else:
                    if highEdgeLimit > 255:
                        print "highEdgeLimit is too high. Setting"
                        highEdgeLimit = 250
                    elif lowEdgeLimit < 0:
                        print "lowEdgeLimit is too low. Setting"
                        lowEdgeLimit = 10

                    print "highEdgeLimit has increased: ", highEdgeLimit
                    print "lowEdgeLimit has changed: ", lowEdgeLimit
                
    def backgroundSubtractionMain(self, currentFrame, coordinatesArray):
        print "coordinatesArray: ", coordinatesArray
        returnCars = []
        for dcar in range(len(coordinatesArray)):          
            ###Image slicing and blurring
            smolSlice = currentFrame[coordinatesArray[dcar][1]:coordinatesArray[dcar][3], coordinatesArray[dcar][0]:coordinatesArray[dcar][2]]
            gray1 = cv2.cvtColor(smolSlice,cv2.COLOR_BGR2GRAY)
            blur1 = cv2.blur(gray1,(20,20))
            blur1_copy = blur1

            cutSlice = self.backgroundImg[coordinatesArray[dcar][1]:coordinatesArray[dcar][3], coordinatesArray[dcar][0]:coordinatesArray[dcar][2]]
            gray2 = cv2.cvtColor(cutSlice,cv2.COLOR_BGR2GRAY)
            blur2 = cv2.blur(gray2,(20,20))
            blur2_copy = blur2		

            differenceImage = self.blurAndThresholdNoise(blur1_copy, blur2_copy, 240, 10)

            #Edges and finding contours
            edges = cv2.Canny(differenceImage,500,500)
            contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

            #Find bbox of all contour returns, and draw all bbox found
            color = cv2.cvtColor(differenceImage, cv2.COLOR_GRAY2BGR)
            bbox = self.contoursToBBox(contours, color)

            #Find widest bbox and draw in yellow on image
            largestXBbox = self.findLargestXBbox(bbox, color)
            
            if largestXBbox == [0,0,0,0]:
                largestXBbox = self.recursiveFailSafe(blur1, blur2, smolSlice)
                
            print "coordinatesArray[dcar]: ", coordinatesArray[dcar]
            print "largest0: ", largestXBbox
            print "add: ", largestXBbox[0]+coordinatesArray[dcar][0]

            addedCoordinates = [largestXBbox[0]+coordinatesArray[dcar][0], largestXBbox[1]+coordinatesArray[dcar][1],                                 largestXBbox[0]+coordinatesArray[dcar][2], largestXBbox[1]+coordinatesArray[dcar][3]]

            returnCars.append(addedCoordinates)
            print "largestXBbox: ", addedCoordinates
            print "NEXT IMAGE------------------------"
        return returnCars

