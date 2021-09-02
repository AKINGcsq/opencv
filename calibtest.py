import cv2

import cv2
import numpy as np
import glob
import difTheImg

def calibtest():
    # 设置寻找亚像素角点的参数，采用的停止准则是最大循环次数30和最大误差容限0.001
    criteria = (cv2.TERM_CRITERIA_MAX_ITER | cv2.TERM_CRITERIA_EPS, 30, 0.001)
    x = 15
    y = 8
    # 获取标定板角点的位置
    objp = np.zeros((x * y, 3), np.float32)
    objp[:, :2] = np.mgrid[0:x, 0:y].T.reshape(-1, 2)  # 将世界坐标系建在标定板上，所有点的Z坐标全部为0，所以只需要赋值x和y

    obj_points = []  # 存储3D点
    img_points = []  # 存储2D点
 
    images = glob.glob("F:/vsc_workspace/opencv/calib/*.BMP")
    for fname in images:
        fname = fname.replace("\\","/")
        print(fname)
        img = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
        cv2.imshow('i',img)

        gray = img
        size = gray.shape[::-1]
        ret, corners = cv2.findChessboardCorners(gray, (x,y), None)
        print(ret)

        if ret:

            obj_points.append(objp)

            corners2 = cv2.cornerSubPix(gray, corners, (5, 5), (-1, -1), criteria)  # 在原角点的基础上寻找亚像素角点
            #print(corners2)
            if [corners2]:
                img_points.append(corners2)
            else:
                img_points.append(corners)

            cv2.drawChessboardCorners(img, (x, y), corners, ret)  # 记住，OpenCV的绘制函数一般无返回值
            cv2.imshow('img', img)
            cv2.waitKey(20000)

    cv2.destroyAllWindows()