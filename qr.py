import cv2
import glob
import numpy as np

kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
vid = cv2.VideoCapture(0)
def qrRecognizer(name, inputImage):
    resizedImage = cv2.resize(inputImage, (600, 600))
    grayScaledImage = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)
    edgesWithCanny = cv2.Canny(grayScaledImage, 150, 250)
    contours, hierarchy = cv2.findContours(edgesWithCanny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    hierarchy = hierarchy[0]
    neededContours = []
    def getDepth(currentHierarchy):
        depth = 0
        while currentHierarchy[2] > 0:
            depth += 1
            currentHierarchy = hierarchy[currentHierarchy[2]]
        return depth

    for i,c in enumerate(contours):
        if getDepth(hierarchy[i]) >= 5:
            neededContours.append(c)


    drawedImage = cv2.drawContours(resizedImage, neededContours, -1,(83, 255, 0), 2)
    cv2.imshow(name, drawedImage)
    if len(neededContours) >= 3:
        print("Qr code Founded!")
    else:
        print("Qr code not Founded!")
    
  #Implemented and working with videocapture too.

#while(True):
 #   ret, frame = vid.read()
  #  newFrame = cv2.filter2D(frame, -1, kernel)
   # qrRecognizer("frame", newFrame)
    
    #if cv2.waitKey(1) & 0xFF == ord('q'):
     #   break
  
#vid.release()
#cv2.destroyAllWindows()

images = [cv2.imread(file) for file in glob.glob("./samples/*")]
for i,image in enumerate(images):
    qrRecognizer("Image %d" % (i),image)
cv2.waitKey(0)