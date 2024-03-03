import cv2

img = cv2.imread("Opencv/Bluemosque.jpg", -1)

# -1,  cv2.IMREAD_COLOR : Loads a color image, Any transparency of image will be neglected. It is the default flag.
# 0,  cv2.IMREAD_GRAYSCALE : Loads image in greyscale mode
# 1,  cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel


# Resize the image and rotate
img = cv2.resize(img, (0, 0), fx=0.2, fy=0.3)
img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

# SAVE THE IMAGE or 'WRITE'
cv2.imwrite("Opencv/new_img.jpg", img)

# display image
cv2.imshow("image", img)

# Close the window opened
cv2.waitKey(0)  # 0 - wait until a number is pressed
cv2.destroyAllWindows()
