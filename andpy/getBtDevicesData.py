# Made By Bl4ky113 

import time
import androidhelper
droid = androidhelper.Android()

while True:
  print("Conection ?:  ", droid.bluetoothActiveConnections())
  if droid.bluetoothActivceConnections().result == True:
    print("Name:  ", droid.bluetoothGetConnectedDeviceName())

  time.sleep(1)