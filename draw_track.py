import csv
import matplotlib.pyplot as plt

with open('00001_predict.csv', 'r') as csvfile:
	reader = csv.reader(csvfile)
	data = []
	frame = []
	col = []
	#mty = []
	#tim = []
	data2 = []
	frame2 = []
	num = 0

	with open('00001_S2.csv', 'r') as file:
		reader2 = csv.reader(file)

		for row in reader2:
			if row[1] != 'HitFrame':
				frame2.append(int(row[1]))

	print(frame2)

	for row in reader:
		if row[1] != '0' and row[1] != 'Visibility':
			if row[3] != 'Y':
				data.append(int(row[3]))

				'''
				if (row[3] == '0'):
					data[-1] = data[-2]
					mty.append(0)
					tim.append(int(row[0]))
				'''

			if row[0] != 'Frame':
				frame.append(int(row[0]))

			if row[2] != 'X':
				col.append(int(row[2]))

		if num < len(frame2) and row[0] != 'Frame' and int(row[0]) == frame2[num]:
			print(num, 'hi')
			num += 1
			data2.append(int(row[2]))

	plt.figure()
	plt.subplot(2, 1, 1)
	line = plt.plot(frame, data) 	# y
	line2 = plt.plot(frame2, data2, c='r')
	plt.setp(line, marker = 'o', linewidth = 1)
	plt.setp(line2, marker = 'o', linewidth = 0)
	plt.grid()

	plt.subplot(2, 1, 2)
	line = plt.plot(frame, col) 	# x
	line2 = plt.plot(frame2, data2, c='r')
	plt.setp(line, marker = 'o', linewidth = 1)
	plt.setp(line2, marker = 'o', linewidth = 0)
	plt.grid()
	plt.show()
