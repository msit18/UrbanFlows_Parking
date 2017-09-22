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
occlusionFR = 1

site = "Ames St"
parkingSpotSizeinFt = 17
##Ames street
##Spots 1-4

##Spots 0-4