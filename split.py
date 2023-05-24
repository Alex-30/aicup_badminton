import os
import shutil

'''
train = './train'
fold = os.listdir(train)
cnt = 0

for data in fold:
	file = os.listdir(os.path.join(train, data))

	for f in file:
		if f[-1] == '4':
			src = os.path.join(os.path.join(train, data), f)
			dst = os.path.join('tmp', f)
			shutil.copy(src, dst)
			cnt += 1

print(cnt)
print('done....')
'''

tmp = './tmp'
file = os.listdir(tmp)
num = 0
cnt = 0
lis = ['1_50', '51_100', '101_150', '151_200', '201_250', '251_300', '301_350', '351_400', '401_450', '451_500', '501_550','551_600', '601-650', '651_600', '601_750', '751_800']

os.makedirs(os.path.join(tmp, lis[cnt]))

for f in file:
	src = os.path.join(tmp, f)
	dst = os.path.join(os.path.join(tmp, lis[cnt]), f)
	shutil.move(src, dst)
	num += 1

	if num == 50:
		num = 0
		cnt += 1
		os.makedirs(os.path.join(tmp, lis[cnt]))
