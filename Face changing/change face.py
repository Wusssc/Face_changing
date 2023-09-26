import cv2

image=cv2.imread("lena.png",1)
cv2.imshow("before", image)
img = cv2.imread("chg.jpg",1)
image[220:400,250:350] = img
cv2.imshow("after", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

