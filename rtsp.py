import cv2

rtsp_urls = ["rtsp://localhost:8554/stream"] * 8
window_titles = ["frame_" + str(i) for i in range(8)]

cam = [cv2.VideoCapture(i) for i in rtsp_urls]
ret = [None] * len(rtsp_urls)
frames = [None] * len(rtsp_urls)

# Camera
try:
    # while cam_0.isOpened():
    #     ret_0, frame_0 = cam_0.read()
    #     if not ret_0:
    #         print("Can't receive frame (stream end?). Exit...")
    #         break
    #     cv2.imshow("frame_0", frame_0)
    #     if cv2.waitKey(1) == ord("q"):
    #         break
    while True:
        for i, c in enumerate(cam):
            if c is not None:
                ret[i], frames[i] = c.read()

        for i, f in enumerate(frames):
            if ret[i] is True:
                cv2.imshow(window_titles[i], f)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break            
except KeyboardInterrupt:
    pass
finally:
    for c in cam:
        c.release()
    cv2.destroyAllWindows()