import cv2
import numpy as np
import os
from numba import jit, cuda

@jit(target_backend='cuda')
def run(path, name):
	img = cv2.imread(path)

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	lower_white = np.array([66,0,230])
	upper_white = np.array([170,255,255])
	mask = cv2.inRange(hsv, lower_white, upper_white)

	for i in range(len(mask)):
		for j in range(len(mask[0])):
			mask[i][j] = abs(255 - mask[i][j])

	dst = os.path.join('./test_court', name[:-4] + '_1.jpg')
	cv2.imwrite(dst, mask)


fold_cd = './test_court'
data = os.listdir(fold_cd)

for name in data:
	img = os.path.join(fold_cd, name)
	run(img, name)
