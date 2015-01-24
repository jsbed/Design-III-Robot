import cv2

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("GRAY", gray)
    cv2.imshow("RGB", frame)
    c = cv2.waitKey(1)
    if c == 27: #to quit, the 'ESC' key is pressed
        exit()

cap.release()
cv2.destroyAllWindows()
