import cv2
import os


def video2imgs(path):
	cap = cv2.VideoCapture(path)
	judge = cap.isOpened()

	if not judge:
		return 1

	return 0


num = 0
save = []

files = os.listdir('./img')

for f in files:
	item = os.listdir('./img/' + f)

	for i in item:
		print(i)

		if i[-1] == 'g':
			if video2imgs('./img/' + f + '/' + i) == 1:
				num += 1
				save.append('./img/' + f + '/' + i)

print(save)
print("num:", num)
