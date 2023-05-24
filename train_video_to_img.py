import cv2
import os
import shutil
import csv
from numba import jit, cuda

def video2imgs(videoPath, imgPath, f):
	cap = cv2.VideoCapture(videoPath)
	judge = cap.isOpened()
	fps = cap.get(cv2.CAP_PROP_FPS)
	cnt = 0

	while (judge):
		flag, frame = cap.read()
		cnt += 1
		
		if not flag:
			#print('Process finished!')
			break

		with open('./train/' + f + '/' + f + '_S2.csv') as csvfile:
			reader = csv.reader(csvfile)

			for row in reader:
				if row[1] == str(cnt):
					imgname = f + '_' + row[1] + '.jpg'
					newPath = imgPath + imgname

					point_size = 6
					point_color = (0, 0, 255)
					thickness = -1

					with open('./video/draw2/' + f + '_predict.csv') as bafile:
						ba = csv.reader(bafile)
						flag = False

						for r in ba:
							if r[0] == str(cnt) or flag:
								print(f, 'ok')
								if r[1] == '1':
									points = (int(r[2]), int(r[3]))
									cv2.circle(frame, points, point_size, point_color, thickness)	
									cv2.imwrite(newPath, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
									break
								else:
									flag = True


					break

	cap.release()

tmp = './frame'
files = os.listdir(tmp)

for f in files:
	if f[-1] == '4':
		video2imgs('./frame/' + f, './train_frame/' , f[8:13])
		print(f)
