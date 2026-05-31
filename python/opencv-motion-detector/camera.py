import cv2
previous_frame = None
screenshot_taken = False
screenshot_count = 0
camera = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
while True:
    success, frame = camera.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if previous_frame is None:
        previous_frame = frame.copy()
        continue
    diff_frame = cv2.absdiff(frame,previous_frame)
    motion_score = diff_frame.sum()
    if motion_score > 3_000_000:
        if screenshot_taken == False:
            screenshot_count += 1
            cv2.imwrite(f"motion_{screenshot_count}.jpg", frame)
            print("Screenshot Saved")
            screenshot_taken = True

        cv2.putText(
            frame,
            "MOTION: YES",
            (20, 100),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    if motion_score <= 3_000_000:
        screenshot_taken = False

    previous_frame = frame.copy()
    edge_frame = cv2.Canny(gray_frame, 200, 300)
    cv2.putText(
        frame,
        "ARS VISION V3",
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )
    cv2.rectangle(
        frame,
        (10, 10),
        (300, 130),
        (0, 255, 0),
        2
    )
    faces = face_cascade.detectMultiScale(gray_frame)
    for (x, y, w, h)in faces:
        cv2.rectangle(
        frame,
        (x, y),
        (x+w, y+h),
        (0, 255, 0),
        2
        )
    cv2.imshow("Camera", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break
    
camera.release()
cv2.destroyAllWindows()