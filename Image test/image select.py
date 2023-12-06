import cv2 as cv


drawing = False
ix, iy = -1, -1


def draw_markers(event, x, y, flags, param):
    global ix, iy, drawing, frame, frame_copy
    if flags == cv.EVENT_FLAG_ALTKEY + cv.EVENT_FLAG_LBUTTON:
        if event == cv.EVENT_LBUTTONDOWN:
            print("Alt + lmouse down")
            drawing = True
            ix, iy = x, y
            frame_copy = frame.copy()
        elif event == cv.EVENT_MOUSEMOVE:
            if drawing:
                frame = cv.rectangle(
                    frame_copy.copy(), (ix, iy), (x, y), (0, 255, 0), 2)
        elif event == cv.EVENT_LBUTTONUP:
            print("Alt + lmouse up")
            drawing = False
            cv.rectangle(frame, (ix, iy), (x, y), (0, 255, 0), 2)

    elif event == cv.EVENT_LBUTTONUP:
        print("Draw crosshair")
        cv.drawMarker(frame, (x, y), (255, 0, 0), 0, 16, 2, 8)


cap = cv.VideoCapture('video.avi')
cap.set(cv.CAP_PROP_POS_FRAMES, 1)
ret, frame = cap.read()
frame_copy = frame.copy()
cv.namedWindow('frame')
cv.setMouseCallback('frame', draw_markers)

while(True):
    cv.imshow('frame', frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()