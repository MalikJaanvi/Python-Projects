import cv2

cap = cv2.VideoCapture(0)

imgcounter =0 

while True:
    success , photo = cap.read() #read image and tell whether it is done successfully  or not , success is just a boolean value.
    cv2.imshow("video",photo)
    x =  cv2.waitKey(1) 
    if  x%0xFF == ord('q'):
        break

    elif x%0xFF == ord('m'):
        imagename = "opencv{}.png".format(imgcounter)
        cv2.imwrite(imagename,photo)
        print("ss taken")
        imgcounter +=1

cap.release()
cap.destroyAllWindows()