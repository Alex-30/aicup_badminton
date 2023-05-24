import os
import shutil
import numpy

dirs = os.listdir('./court')

for path in dirs:
    files = os.listdir(os.path.join('./court', path))
    
    print(files[0])
    shutil.copy('./court/' + path + '/' + files[0], './get_court/' + files[0])