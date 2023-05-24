import os
import numpy as np
import shutil
import subprocess

data_ds = './part2/test_5/hi'
data = os.listdir(data_ds)
cnt = 1

for d in data:
	if d[-1] == '4':
		command = f'python event.py --input_video={data_ds + "/" + d} --input_csv={data_ds + "/" + d[:-4] + ".csv"}'
		output = subprocess.run(command, shell = True)
		print(cnt)
		cnt += 1

		src = os.path.join(data_ds, d[:-4] + '_event.csv')
		dst = './test_event/' + d[:-4] + '_event.csv'
		shutil.move(src, dst)
