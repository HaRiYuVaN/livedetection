import cv2
face_cap = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
vid_cap = cv2.VideoCapture(0)
while True:
    hari=10
    r,v = vid_cap.read()
    col=cv2.cvtColor(v,cv2.COLOR_BGRA2GRAY)
    facess = face_cap.detectMultiScale(col,1.1,5,cv2.CASCADE_SCALE_IMAGE,(30,30))
    for (x, y, w, h) in facess:
        cv2.rectangle(v, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("Video",v)
    if cv2.waitKey(10) == ord("a"):
        break
v.release()
