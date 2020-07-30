# import opencv library
import cv2

import serial
serl = serial.Serial('COM3', 9600)



# Create a VideoCapture() object as "video"
video = cv2.VideoCapture(0, cv2.CAP_DSHOW)

face_cascade = cv2.CascadeClassifier('C:\\Users\\USER\\Downloads\\tes\\haarcascade_frontalface_default.xml')

# Enter into an infinite while loop
while True:
    _, img = video.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        start_point = (x, y)
        end_point = (x+w, y+h)
        cv2.rectangle(img, start_point, end_point, (255, 0, 0), 2)

        area = w*h
        print(area)
 
        #distance =2*(10**(-9))*area**2 - (0.0009*area) + 109.16
        distance = round(61065*(area**-0.637))
        Distance = "Distance: " + str(distance) + " cm"

        cv2.putText(img, Distance, (x+10, y-10), cv2.FONT_HERSHEY_SIMPLEX, 1,(255, 0, 0), 3, cv2.LINE_AA) 

        serl.write(Distance.encode())



    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the webcam. in other words turn it of
video.release()

# Destroys all the windows which were created
cv2.destroyAllWindows()
