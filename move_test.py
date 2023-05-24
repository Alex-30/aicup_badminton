import os
import shutil
import numpy as np

data_ds = './part2/part2/test'
dirs = os.listdir(data_ds)

for d in dirs:
    src = os.path.join(os.path.join(data_ds, d), d + '.mp4')
    dst = os.path.join('./test', d + '.mp4')
    shutil.copy(src, dst)