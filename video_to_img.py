import cv2
import os
import shutil


def video2imgs(videoPath, imgPath, f):
	if not os.path.exists(imgPath):
		os.makedirs(imgPath)
	
	cap = cv2.VideoCapture(videoPath)
	judge = cap.isOpened()
	fps = cap.get(cv2.CAP_PROP_FPS)
	#print('fps: ', fps)

	count = 1

	while (judge):
		flag, frame = cap.read()
		
		if not flag:
			print('Process finished!')
			break

		imgname = f + '_' + str(count) + '.jpg'
		newPath = imgPath + imgname

		cv2.imwrite(newPath, frame, [cv2.IMWRITE_JPEG_QUALITY, 100])
		count += 1

	cap.release()
	return count


num = 128470
flag = False
tmp = './train/'

files = os.listdir('./train')

for f in files:
	if flag == False and f != '00400':
		continue
	elif f == '00400':
		flag = True

	item = os.listdir('./train/' + f)

	print(item)

	for i in item:
		if i[-1] == '4':
			num += video2imgs('./train/' + f + '/' + i, './img/' + f + '/', f)
			print('imgs count:', num)

		elif i[-1] == 'v':
			shutil.copyfile('./train/' + f + '/' + i, './img/' + f + '/' + i)
