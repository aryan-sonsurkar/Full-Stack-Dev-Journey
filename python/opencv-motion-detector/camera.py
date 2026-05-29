import cv2
previous_frame = None
camera = cv2.VideoCapture(0)
while True:
    success, frame = camera.read()
    if previous_frame is None:
        previous_frame = frame.copy()
        continue
    diff_frame = cv2.absdiff(frame,previous_frame)
    motion_score = diff_frame.sum()
    if motion_score > 3_000_000:
        print("MOTION DETECTED")
    previous_frame = frame
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge_frame = cv2.Canny(gray_frame, 200, 300)
    cv2.imshow("Camera", diff_frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    
camera.release()
cv2.destroyAllWindows()