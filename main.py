import cv2
import numpy as np


# lesson 1, 2
# install img
img = cv2.imread("imges/i.jpg")

# methods
cut_img = cv2.resize(img, (500, 500))
blur_img = cv2.GaussianBlur(img, (9, 9), 0)
bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# binary
bin_img = cv2.Canny(img, 10, 100)
kernel = np.ones((5, 5), np.uint8)
img = cv2.dilate(bin_img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)

# show result
# cv2.imshow("Result", new_img[100:200, 300:400])
# cv2.imshow("Result", img)

# cv2.waitKey(0)

# lesson 3
photo = np.zeros((450, 450, 3), dtype='uint8')

# ... = BGR (not RGB)
photo[200:250, 200:250] = 10, 120, 70

cv2.rectangle(photo, (20, 20), (50, 50), (119, 201, 105), thickness=cv2.FILLED)

cv2.line(photo, (50, 50), (200, 200), (255, 255, 255), thickness=3)

cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (255, 0, 0), thickness=2)

cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 50, (119, 201, 77), thickness=3)

cv2.putText(photo, 'MagicWithCV2', (125, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), thickness=3)

cv2.imshow('Photo', photo)
cv2.waitKey(0)


# lesson 4 and loop with lesson 2
cap = cv2.VideoCapture("videos/voleyball.mp4")
while True:
    success, vimg = cap.read()

    vimg = cv2.resize(vimg, (500, 500))
    vimg = cv2.GaussianBlur(vimg, (9, 9), 0)
    vimg = cv2.cvtColor(vimg, cv2.COLOR_BGR2GRAY)

    vimg = cv2.Canny(vimg, 75, 75)
    kernel = np.ones((5, 5), np.uint8)
    vimg = cv2.dilate(vimg, kernel, iterations=1)
    vimg = cv2.erode(vimg, kernel, iterations=1)

    cv2.imshow('Result', vimg)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break


# def rotate(img, angle):
#     height, width = img.shape[0], img.shape[1 ]


img = cv2.imread("imges/i.jpg")

img = cv2.flip(img, 0)
cv2.imshow("Result", img)

cv2.waitKey(0)
