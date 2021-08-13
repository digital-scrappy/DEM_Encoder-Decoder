from pathlib import Path
import rasterio
import os
import numpy as np

import torch.autograd as autograd
from torch.utils.data.dataset import Dataset
from torch.utils.data.dataloader import DataLoader


class lazy_DEM_Data(Dataset):

    def __init__(self, tif_dir, cuda=False):
        files = os.listdir(tif_dir)
        self.paths = [(tif_folder / i) for i in files if i.endswith(".tif")]
        self.total_files = len(self.paths)
        self.cuda = cuda

    def __get_item__(self, idx):
        file_path = self.paths[idx]
        with rasterio.open(file_path) as handle:
            dem_array = handle.read(1)

        if self.cuda:
            return torch.cuda.ShortTensor(dem_array)
        else:
            return torch.ShortTensor(dem_array)

    def __len__(self):
        return self.total_files


class DataLD(object):
    def __init__(self, tif_dir, cuda=False):
        self.dataset = lazy_DEM_Data(tif_dir, cuda)

    def get_loader(self, shuf=True, batch_size=1):
        data_loader = DataLoader(dataset=self.dataset,
                                 batch_size=batch_size,
                                 shuffle=shuf,
                                 num_workers=1)
        return data_loader
