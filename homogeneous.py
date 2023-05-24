import cv2
import numpy as np
import os
import csv

coor = []
landing = []

train_cd = './video/draw'
files = os.listdir(train_cd)

for f in files:
	if f[-1] == 'v':
		with open('./train/' + f[:5] + '/' + f[:5] + '_S2.csv') as eventfile:
			event = csv.reader(eventfile)

			for e in event:
				if e[1] != 'HitFrame':
					flag = False
					
					# find the e[1] value that in the reader.
					with open(train_cd + '/' + f) as csvfile:
						reader = csv.reader(csvfile)
						
						for row in reader:
							if row[0] == e[1] or flag:
								if row[1] == '1':
									coor.append([int(row[2]), int(row[3])])
									landing.append([int(e[6]), int(e[7])])
									break
								else:
									break

						
train_cd = './video/draw2'
files = os.listdir(train_cd)

for f in files:
	if f[-1] == 'v':
		with open('./train/' + f[:5] + '/' + f[:5] + '_S2.csv') as eventfile:
			event = csv.reader(eventfile)

			for e in event:
				if e[1] != 'HitFrame':
					flag = False
					
					# find the e[1] value that in the reader.
					with open(train_cd + '/' + f) as csvfile:
						reader = csv.reader(csvfile)

						for row in reader:
							if row[0] == e[1] or flag:
								if row[1] == '1':
									coor.append([int(row[2]), int(row[3])])
									landing.append([int(e[6]), int(e[7])])
									break
								else:
									break


#print(landing[:10])
#print()
#print(coor[:10])
#print(len(coor))

# 校準資料：球場圖片上的已知點像素座標和球場平面上的實際座標
image_points = np.array(coor, dtype=np.float32)  # 圖片上的已知點像素座標
world_points = np.array(landing, dtype=np.float32)  # 球場平面上的實際座標

# 計算轉換矩陣
transformation_matrix, _ = cv2.findHomography(image_points[:30], world_points[:30])

# 定義轉換函式
def image_to_world_coordinates(image_point):
    # 將圖片座標轉換為齊次座標
    homogeneous_point = np.array([image_point[0], image_point[1], 1], dtype=np.float32)
    
    # 進行透視變換，將圖片座標轉換為球場平面上的座標
    world_point = np.dot(transformation_matrix, homogeneous_point)

    # 歸一化，除以最後一個元素
    world_point /= world_point[2]

    return (world_point[0], world_point[1])

test = []

files = os.listdir('./test_event')
for f in files:
	with open('./test_event/' + f) as csvfile:
		reader = csv.reader(csvfile)

		for row in reader:
			with open('./test/' + f[:5] + '_predict.csv') as ballfile:
				ball = csv.reader(ballfile)
				flag = False

				for b in ball:
					if b[0] == row[0]:
						if b[1] == '1' or flag:
							test.append([f[:5] + str(b[0]), int(b[2]), int(b[3])])
							break
						else:
							flag = True

for t in test:
	# 測試轉換函式
	pixel_x = t[1]  # 球在圖片上的像素x座標
	pixel_y = t[2]  # 球在圖片上的像素y座標
	world_coordinates = image_to_world_coordinates((pixel_x, pixel_y))
	#print("球在球場平面上的座標：", int(world_coordinates[0]), int(world_coordinates[1]))
	data = []

	with open('result.csv', 'r') as submit:
		reader = csv.reader(submit)

		for row in reader:
			if row[0][:5] == t[0][:5] and int(row[2]) == int(t[0][5:]):
				row[6] = int(world_coordinates[0])
				row[7] = int(world_coordinates[1])
				print(row)
			
			data.append(row)
					
	with open('result.csv', 'w', newline='') as output:
		writer = csv.writer(output)
		writer.writerows(data)
		
