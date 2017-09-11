import ctypes
import os

SPI_SETDESKWALLPAPER = 20
print("set_background")
path = os.path.abspath(r'./102_0228.JPG')
#ok = ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path, 2)
ok = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)
print(ok)
print(path)