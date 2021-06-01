# -*- coding:utf-8 -*- 
# author: LIUWENYU
# datetime: 2020/11/17 14:41
# describe: 
import numpy as np
import cv2

img = cv2.imread('./flower.jpg',flags=3)
print(img.shape)
print(img.size)

# cv2.namedWindow('FLOWER')
# cv2.imshow('FLOWER',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
