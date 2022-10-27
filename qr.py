import cv2

image = cv2.imread('qr3.png')

image = cv2.resize(image, (1000, 1000))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

goodContours =[]
for c in contours:
    approx = cv2.approxPolyDP(c, 1, True)

if len(approx) == 4:
    goodContours.append(approx)

image = cv2.drawContours(image, goodContours, -1, (0, 255, 0), 2, cv2.LINE_AA)
print(goodContours)
cv2.imshow("kep", image)
cv2.waitKey(0)