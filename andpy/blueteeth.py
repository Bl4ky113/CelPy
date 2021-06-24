# Made By Bl4ky113

import androidhelper
droid = androidhelper.Android()

# Check Active connections with Bluetooth
if droid.bluetoothActiveConnections():
  btConectedDevice = droid.bluetoothGetConectedDeviceName()
else: 
  btConectedDevice = False

# Get the Bluetooth Name of the Device
def getBtLocalName() -> str:
  btLocalName = list(droid.bluetoothGetLocalName())
  btLocalName = str(btLocalName[1])
  return btLocalName

# Show Bluetooth Name of the Device
def showBtLocalData():

  print("|".center(45, "="), "\n")
  print("Device's Name:  ", getBtLocalName(), "\n")
  print("|".center(45, "="))

# Change Bluetooth Name of the Device
def changeBTLocalName(localName = ""): 
  answer = input("You want to change the Device's name? (y/n)")
  if answer.casefold() == "y" or answer.casefold() == "yes":
    new_localName = input("Enter your new Name:  ")
    if not new_localName == localName:
      droid.bluetoothSetLocalName()
      showBtLocalData()
    else:
      print("That is your current Device's Name")
      changeBTLocalName(localName)

""" Start the Program """

# Turn the Bluetooth On
if not droid.checkBluetoothState():
  droid.toggleBluetoothState(True, False)
  droid.vibrate(150)
else: 
  pass

print("|||".center(45, "="), "\n")
print("Wellcome to Blueteeth \n")
print("An Bluetooth example of the uses of Sl4A with Bluetooth on Android OS\n\n")
print("//Made By Bl4ky113".center(45), "\n")
print("|||".center(45, "="))

showBtLocalData()

""" Main Menu """
while True:
  print("".center(45, "="), "\n")
  command = input("Enter a Command:  ")
  print("".center(45, "="), "\n")

  if command.casefold == "change name":
    changeBTLocalName(getBtLocalName())
