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

	dst = os.path.join('./court', f)
	cv2.imwrite(dst, mask)


num = 0
total = 266314
fold_cd = './img'
data = os.listdir(fold_cd)

for name in data:
	img_cd = os.path.join(fold_cd, name)
	files = os.listdir(img_cd)

	for f in files:
		if f[-1] == 'g':
			run(os.path.join(img_cd, f), f)
			
			num += 1
			print(f, ": {:.5f}".format((num / total) * 100))

