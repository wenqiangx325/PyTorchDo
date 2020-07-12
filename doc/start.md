# Start of PyTorch

## Install Python

## Install VSCode

## install all package

All package in requirements.txt, just run below code to install

```PowerShell
# install packages in requirements.txt by pip
pip install -r .\requirements.txt
```

## Install VS Runtime (addition)

1. download VS Runtime [VC_redist](https://download.visualstudio.microsoft.com/download/pr/d60aa805-26e9-47df-b4e3-cd6fcc392333/7D7105C52FCD6766BEEE1AE162AA81E278686122C1E44890712326634D0B055E/VC_redist.x64.exe)

2. install that

## Test pytorch install
```python
import torch

x = torch.rand(5, 3)
print(x)
```