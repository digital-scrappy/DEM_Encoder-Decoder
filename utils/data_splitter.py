import os
from pathlib import Path
import random
from seed import seed
from shutil import copyfile

random.seed = seed
train_size = 0.8
valid_size = 0.1

data_path = Path('/home/scrappy/data/')
files = os.listdir(data_path / 'combined')

num_files = len(files)
random.shuffle(files)
train = ['train'] * int(num_files * train_size)
dev = ['dev'] * int(num_files * valid_size)
test =['test'] * int(num_files * valid_size)
split = train + dev + test
for  file_name, folder in zip(files,split):
    copyfile( (data_path / 'combined' / file_name) , (data_path / folder / file_name))
