import cv2

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

while True:

    ret, frame = cap.read()
    #frame = cv2.resize(frame, (1280, 720)) 
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("GRAY", gray)
    
    cv2.imshow("RGB", frame)
    c = cv2.waitKey(1)
    if c == 27: #to quit, the 'ESC' key is pressed
        exit()

cap.release()
cv2.destroyAllWindows()
