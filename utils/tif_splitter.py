import rasterio
import numpy as np
from pathlib import Path
data_folder = Path("/home/scrappy/data/combined")

county = "kaernten"
dataset = rasterio.open('/home/scrappy/data/als_dgm_5m.asc')

width = dataset.width
height = dataset.height
nodata = dataset.nodata
count = dataset.count
dtype = dataset.dtypes[0]
# we will have 2.5km squares
square_dim = 500
x_indices = [ (i*500, ( (i+1) *500) -1) for i in range((width // square_dim))]
y_indices = [ (i*500, ( (i+1) *500) -1) for i in range((height // square_dim))]



print("reading …")

img = dataset.read(1)
print("splitting …")
for x_0, x_1 in x_indices:
    for y_0, y_1 in y_indices:
        square = img[ x_0 : x_1, y_0 : y_1]
        if square.mean() > 0:
            name = f"{county}-({x_0}_{y_0})-({x_1}_{y_1}).tif"
            path = data_folder / name
            print(name)

            with rasterio.open(
                    path,
                    'w',
                    driver='GTiff',
                    height = square_dim,
                    width = square_dim,
                    count = 1,
                    dtype = dtype
            ) as new_tif:
                new_tif.write(square, 1)
