import time
import datetime
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    st = st.replace(' ','_')
    st = st.replace(':', '-')

    output_name =str("output\\"+"{}".format(st)+".png")

    #cv2.imshow('frame',frame)

    cv2.imwrite(output_name, frame)
    print("Image saved!")

    time.sleep(10)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()