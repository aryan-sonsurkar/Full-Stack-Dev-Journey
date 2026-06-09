import cv2
camera = cv2.VideoCapture(0)
while True:
    success, frame = camera.read()
    hsv_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2HSV
    )
    lower_red = (0, 120, 70)
    upper_red = (10, 255, 255)
    mask = cv2.inRange(
        hsv_frame,
        lower_red,
        upper_red
    )
    cv2.imshow("Camera", frame)
    cv2.imshow("HSV", hsv_frame)
    cv2.imshow("Mask", mask)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    
camera.release()
cv2.destroyAllWindows()