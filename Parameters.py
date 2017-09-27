site = "Museum"
# folderName = '04-26_17.00.00'
folderName = '07-12_10.00.00'
folderTime = folderName[6:8]+folderName[9:11]
folderDate = folderName[0:5]
imagePath = '/home/ubuntu/Parking/{0}/{1}/*.jpg'.format(site, folderName)

useBackgroundSubtraction = False

#saveFig saves the 
    #showEstDistFreeSpaceGraph Aggregrated Free Space in Feet Graph
    #showFreeSpaceCoord CompareGraph
saveFig = True

#main method analyzeImages_frameNum
saveImgs = True

#add the text to the spots with its IDnum, occlusion counter, and occupancy status
addSpotText = True

##1 Frame/30 seconds
analyzeFR = 15

#Number of frames that can pass before a spot's occupancy status is changed from taken to available
#Is currently at 1, was previously 7 and 2
occlusionFR = 4

#######################
### site = "Ames St"
# RCNN_NMS_Thresh = 0.2
# RCNN_OBJ_Thresh = 0.10
# spotCoordinates = [[(51, 479), (322, 490), (283, 534), (8, 525)],\
#                  [(337, 491), (659, 492), (656, 541), (303, 533)], \
#                  [(677, 492), (958, 494), (989, 545), (670, 542)], \
#                  [(969, 500), (1242, 499), (1300, 539), (1000, 541)], \
#                  [(1256, 501), (1435, 493), (1493, 536), (1306, 541)], \
#                  [(1450, 495), (1596, 490), (1598, 528), (1505, 535)]]

# parkingSpotSizeinFt = 17
# horizontalThreshold = 591
# rotationVar = 2
# ftperpx = 86.333/1190 #(5parkingx17ft+4linesx1/3ft)/(1493-303px)
# estftperpx = 86.333/1669 #(5parkingx17ft+4linesx1/3ft)/(1679-10px)
# linearRegVals = [ -6.41328433e-04,   3.65880005e-07,   1.26635656e+00]
# ##For reference:
# #             estftperpx = 80.0/1310 #(4parkingx20ft)/(1650-340px)

# ##Ames street
# ##Spots 1-4
# # spot_lowEnd = 1
# # spot_highEnd = 4

# ##Spots 0-4
# spot_lowEnd = 0
# spot_highEnd = 4

#######################
### site = "Museum"
RCNN_NMS_Thresh = 0.1
RCNN_OBJ_Thresh = 0.90
spotCoordinates = [[(512, 671), (730, 683), (735, 695), (503, 686)],\
                   [(738, 682), (956, 676), (981, 693), (743, 695)],\
                   [(971, 677), (1162, 670), (1190, 681), (995, 693)],\
                   [(1178, 670), (1325, 655), (1353, 664), (1205, 680)],\
                   [(1342, 655), (1444, 644), (1468, 650), (1369, 662)]]

parkingSpotSizeinFt = 20
horizontalThreshold = 720
rotationVar = -2.5
ftperpx = 81.0/850 # (4parkingx20ft+3linesx1/3ft)/(1353-503)
estftperpx = 81.0/1126 # (4parkingx20ft+3linesx1/3ft)/(1629-503)
linearRegVals = [ -4.15581070e-04,   3.60997488e-07,   1.12321113e+00]
##Curious what the difference is. this linearRegVal is calculated without spot4:
# linearRegVals = [ -1.96755185e-04,   2.36720606e-07,   1.03414618e+00]

spot_lowEnd = 0
spot_highEnd = 3