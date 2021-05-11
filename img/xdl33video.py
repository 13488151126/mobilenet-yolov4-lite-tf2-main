import cv2
import time


# 相机参数设置
def Setcamera(cap):
    cap.set(6, cv2.VideoWriter.fourcc('M', 'J', 'P', 'G'))
    cap.set(3, 480)
    cap.set(4, 640)


if __name__ == '__main__':
    fps = 0.0
    # cv2.namedWindow("camera", 1)
    # 开启ip摄像头
    video = "rtsp://admin:123456ab@128.192.0.34/h264/ch1/sub/av_stream"
    capture = cv2.VideoCapture(video)
    Setcamera(capture)
    c = 1
    frameRate = 20
    num = 0

    while True:
        ref, frame = capture.read()
        if ref:
            
            cv2.imshow("video", frame)
            t = 'ori\\' + str(time.time()).split('.', 1)[0]

            q = cv2.waitKey(10) & 0xff
            if q == ord('q'):
                capture.release()
                break
            elif q == ord('w'):
                print(t)
                cv2.imwrite(t + '.jpg', frame)

        # del ref,frame

    # cv2.destroyWindow("camera")

# if __name__ == '__main__':
#     fps = 0.0
#     cv2.namedWindow("camera", 1)
#     # 开启ip摄像头
#     video = "http://admin:password@192.168.18.165:8081/"
#     capture = cv2.VideoCapture(video)
#     Setcamera(capture)
#     c = 1
#     frameRate = 20
#     num = 0
#     while True:
#         t1 = time.time()
#
#         ref, frame = capture.read()
#
#
#         fps = (fps + (1. / (time.time() - t1))) / 2
#         print("fps= %.2f" % fps)
#         frame = cv2.putText(frame, "fps= %.2f" % (fps), (0, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
#
#         cv2.imshow("video", frame)
#         print((time.time() - t1))
#         c = cv2.waitKey(30) & 0xff
#         if c == ord('q'):
#             capture.release()
#             break
#
#     cv2.destroyWindow("camera")
