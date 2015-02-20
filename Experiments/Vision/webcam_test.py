import cv2
import os

SS_DIRECTORY = "screenshots"

if not os.path.exists(SS_DIRECTORY):
    os.makedirs(SS_DIRECTORY)

SS_COUNT = len(os.listdir(SS_DIRECTORY))

cap = cv2.VideoCapture(1)
#cap.set(3,1280)
#cap.set(4,720)

while True:

	ret, frame = cap.read()
	
	cv2.imshow("RGB", frame)
	
	c = cv2.waitKey(1)
	if c == 27: #to quit, the 'ESC' key is pressed
		exit()

	if c == 10: # Touche Enter 
		cv2.imwrite(os.path.join(SS_DIRECTORY, "ss_{}.jpg".format(str(SS_COUNT))), frame)
		print("ss_" + str(SS_COUNT) + " taken")
		SS_COUNT += 1

cap.release()
cv2.destroyAllWindows()
