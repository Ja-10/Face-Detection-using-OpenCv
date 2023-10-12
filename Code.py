import cv2
#load the haar-cascade classifier file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#load the input image
img = cv2.imread('/Users/j/Documents/image.jpeg')
cv2.imshow('Original Image',img)
cv2.waitKey(0)
#convert input image to grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#apply face detection method on the grayscale image
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
cv2.imshow('Resultant Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

