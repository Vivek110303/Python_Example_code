import cv2

cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Error: Could not open webcam.")
else:
    while True:

        ret, frame = cap.read()

        if not ret:
            print("Failed to grab frame")
            break


        cv2.imshow('Live', frame)


        if cv2.waitKey(10) & 0xFF == ord('z'):
            break

    cap.release()
    cv2.destroyAllWindows()
