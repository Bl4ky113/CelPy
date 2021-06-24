# Made By Bl4ky113

import androidhelper
droid = androidhelper.Android()

# Check Active connections with Bluetooth
if droid.bluetoothActiveConnections():
  btConectedDevice = droid.bluetoothGetConectedDeviceName()
else: 
  btConectedDevice = False

# Get the Bluetooth Name of the Device
def getBtLocalName():
  btLocalName = list(droid.bluetoothGetLocalName())
  btLocalName = str(btLocalName[1])
  return btLocalName

# Get the Bluetooth State
def getBtState(type = "bool"):
  btState = ""
  if type == "bool":
    if droid.checkBluetoothState(): 
      btState = True
    else:
      btState = False

  elif type == "str":
    if droid.checkBluetoothState():
      btState = "Enabled"
    else: 
      btState = "Disabled"

  elif type == "number":
    if droid.checkBluetoothState():
      btState = 1
    else:
      btState = 0
  return btState

# Show Bluetooth Name of the Device
def showBtLocalData(showName, showBtState):
  print("|".center(45, "="), "\n")
  if showName: print("Device's Name:  ", getBtLocalName(), "\n")
  else: pass
  if showBtState: print("Bluetooth State:  ", getBtState("str"), "\n")
  else: pass
  print("|".center(45, "="))

# Change Bluetooth Name of the Device
def changeBTLocalName(localName): 
  answer = input("You want to change the Device's name? (y/n)")
  if answer.casefold() == "y" or answer.casefold() == "yes":
    new_localName = input("Enter your new Name:  ")
    if not new_localName == localName:
      droid.bluetoothSetLocalName(new_localName)
      print("Now the Device's name is:  ", new_localName)
    else:
      print("That is your current Device's Name")
      changeBTLocalName(localName)
  else:
    pass

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

showBtLocalData(True, True)

""" Main Menu """
while True:
  command = input("Enter a Command:  ")

  if command == "show data":
    showBtLocalData(True, True)

  if command == "show name":
    showBtLocalData(True, False)

  if command == "show btstate":
    showBtLocalData(False, True)

  if command == "change name":
    changeBTLocalName(getBtLocalName())

  if command == "close":
    break

print("".center(45, "="))
print("".center(45, "-"),)
print("See you later ;)".center(45, "="))
print("".center(45, "-"))
print("".center(45, "="))
