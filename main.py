import cv2 as cv

from PIL import Image

from color import get_limits

yellow = [0, 255, 255]  #yellow in rgb colorspace

cap = cv.VideoCapture(0)



while True:
    
    ret, frame = cap.read()
    
    hsvImage = cv.cvtColor( frame , cv.COLOR_BGR2HSV )
    
    lower_limit, upper_limit = get_limits(color=yellow)
    
    mask = cv.inRange(hsvImage, lower_limit, upper_limit) 
    
    
    mask_new = Image.fromarray(mask)
    
    bbox = mask_new.getbbox()
    
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        
        frame =  cv.rectangle(frame, (x1, y1),(x2, y2), (255, 255, 255), 9 )
    
    cv.imshow("frame", frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()

cv.destroyAllWindows()
    