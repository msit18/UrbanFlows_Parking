folderName = '04-26_17.00.00'
folderTime = folderName[6:8]+folderName[9:11]
folderDate = folderName[0:5]
imagePath = '/home/ubuntu/Parking/{0}/*.jpg'.format(folderName)

useBackgroundSubtraction = False

#saveFig saves the 
    #showEstDistFreeSpaceGraph Aggregrated Free Space in Feet Graph
    #showFreeSpaceCoord CompareGraph
saveFig = False

#main method analyzeImages_frameNum
saveImgs = False

##1 Frame/30 seconds
analyzeFR = 15

#Number of frames that can pass before a spot's occupancy status is changed from taken to available
#Is currently at 1, was previously 7 and 2
occlusionFR = 2

site = "Ames St"
parkingSpotSizeinFt = 17
ftperpx = 86.333/1190 #(5parkingx17ft+4linesx1/3ft)/(1493-303px)
estftperpx = 86.333/1669 #(5parkingx17ft+4linesx1/3ft)/(1679-10px)
linearRegVals = [ -6.41328433e-04,   3.65880005e-07,   1.26635656e+00]
##For reference:
#             estftperpx = 80.0/1310 #(4parkingx20ft)/(1650-340px)

##Ames street
##Spots 1-4
spot_lowEnd = 1
spot_highEnd = 4

##Spots 0-4
# spot_lowEnd = 0
# spot_highEnd = 4