import calibtest
import difTheImg
import cv2

c = 1
if c == 0:
    x =  difTheImg.difTheImg()
    # ret, binary = cv2.threshold(x, 127 ,180, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    cv2.imshow('i', x)
    cv2.waitKey()
    if cv2.waitKey() == 27:
        cv2.destroyAllWindows() 
    cv2.imwrite('F:/vsc_workspace/opencv/calib/3.BMP', x)
else:
    calibtest.calibtest()