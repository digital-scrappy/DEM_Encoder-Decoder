import torch
import torch.nn as nn
import torch.nn.functional as F

class ConvAE(nn.Module):

    def __init__(self):
        super(ConvAE, self).__init__()

        # shape (1001, 1251, 1)
        self.conv1 = nn.Conv2d(1, 24, 3, padding=1)
        self.conv2 = nn.Conv2d(24, 16, 3, padding=1)
        self.conv3 = nn.Conv2d(16, 4, 3, padding=1)

        self.pool = nn.MaxPool2d(2,2)

        self.t_conv1= nn.ConvTranspose2d(4, 16, 2, stride=2)
        self.t_conv2= nn.ConvTranspose2d(16, 24, 2, stride=2)
        self.t_conv3= nn.ConvTranspose2d(24, 1, 2, stride=2)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.pool(x)
        x = F.relu(self.conv2(x))
        x = self.pool(x)
        x = F.relu(self.conv3(x))
        x = self.pool(x)


        x = F.relu(self.t_conv1(x))
        x = F.relu(self.t_conv2(x))
        # linear output layer for reconstruction
        x = self.t_conv3(x)

        return x
