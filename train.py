from utils import dataloader as dl
from model import dem_ae as dem
from pathlib import Path
import torch
import torch.nn as nn
model = dem.ConvAE()
print(model)

loss_function = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

tif_dir = Path("data/")
test = dl.DataLD(tif_dir)
data_loader = test.get_loader()
for index, test_data in enumerate(data_loader):
    print(index)
    model.batch_size = 1
    output = model(test_data[None, ...])
    print(f"output:{output.shape} input:{test_data.shape}")
    loss = loss_function(output, test_data)
    loss.backward()
    optimizer.step()
    print(loss.item())
