import cv2

rtsp = "rtsp://localhost:8554/stream"

cam_0 = cv2.VideoCapture(rtsp)

while cam_0.isOpened():
    ret_0, frame_0 = cam_0.read()
    if not ret_0:
        print("Can't receive frame (stream end?). Exit...")
        break
    cv2.imshow("frame_0", frame_0)
    if cv2.waitKey(1) == ord("q"):
        break

cam_0.release()
cv2.destroyAllWindows()