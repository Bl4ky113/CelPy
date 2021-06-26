# Made By Bl4ky113

import androidhelper
import time
droid = androidhelper.Android()

macAd = input("Enter the Mac Address of the Bluetooth Module:  \n")
print(droid.bluetoothRemoteDeviceName(macAd))
droid.bluetoothConnect(address = macAd)
print(droid.bluetoothConnect(address = None))

# print("Enter a valid Mac Address, look here's a list of them:  \n")
print("Connected to:  ", macAd)

while True:
  droid.bluetoothWrite('t')
  time.sleep(1)
  droid.bluetoothWrite('f')
  time.sleep(1)
  droid.bluetoothWrite('t')
  time.sleep(1)
  droid.bluetoothWrite('f')