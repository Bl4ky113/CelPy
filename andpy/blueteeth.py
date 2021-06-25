# Made By Bl4ky113

import androidhelper
droid = androidhelper.Android()

# Get the Bluetooth Name of the Device
def getBtLocalName():
  btLocalName = list(droid.bluetoothGetLocalName())
  btLocalName = str(btLocalName[1])
  return btLocalName

# Get the Bluetooth State
# Can return the state in bool or string
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
  return btState

# Get the Bluetooth Connections Data
# If there's any, get their name and ID
def getConnections():
  if getBtState("bool"):
    conectionData = []
    conectionState = ""

    btConectionState = list(droid.bluetoothActiveConnections()) # This thing return Nothing...
    btConectionState = str(btConectionState[1])

    # if droid.bluetoothActiveConnections():
    #   conectionState = True
    #   conectionData.append(conectionState)

    #   # Aparently this doesn't work in my device, but it's a problem of the Library, so I can't do anything about it
    #   # conectionDevice = droid.bluetoothGetConnectedDeviceName()
    # else: 
    #   conectionState = False
  else: 
    print("Please turn on your Bluetooth")
    pass

def getScanState():
  posibleStates = {
    "-1": "The Bluetooth is Disabled",
    "0": "The Device is non discoverable and non conectable",
    "1": "The Device is conectable, but non discoverable",
    "2": "The Device is descoverable, but non conectable (?",
    "3": "The Device is conectable and discoverable"
  }

  scanState = list(droid.bluetoothGetScanMode())
  scanState = str(scanState[1])

  if scanState in posibleStates.keys():
    scanState = posibleStates.get(scanState)
  else: 
    scanState = "ERROR"
  
  return scanState

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

# Show Bluetooth Name of the Device
# Choose which info will be shown to the user
def showBtLocalData(showName = False, showBtState = False, showScanState = False,):
  print("|".center(45, "="), "\n")
  if showName: print("Device's Name:  ", getBtLocalName(), "\n")
  else: pass
  if showBtState: print("Bluetooth State:  ", getBtState("str"), "\n")
  else: pass
  if showScanState: print("Scan State:  ", getScanState(), "\n")
  else: pass
  print("|".center(45, "="))

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

showBtLocalData(True, True, True)

""" Main Menu """
while True:
  command = input("Enter a Command:  ")

  if command == "show data":
    showBtLocalData(True, True, True)

  elif command == "show name":
    showBtLocalData(showName = True)

  elif command == "show btstate":
    showBtLocalData(showBtState = True)

  elif command == "show btconections":
    print("Srry This command isn't available")

  elif command == "show scanstate":
    showBtLocalData(showScanState = True)

  elif command == "change name":
    changeBTLocalName(getBtLocalName())

  elif command == "close":
    break

  elif command == "help":
    helpArr = [
      "Commands:".center(45, " "),
      "\n",
      "show data: Show all the device's data\n",
      "show name: Show the device's name\n",
      "show btstate: Show the device's Bluetooth State\n",
      "show scanstate: Show the device's Scan State\n",
      "change name: Changes the device's name\n",
      "close: Finish the program\n"
    ]
    print("".center(45, "="), "\n")
    print("".join(helpArr))
    print("\n", "".center(45, "="))

  else:
    print("That's not a command, you can get help with the 'help' command")

print("".center(45, "="))
print("".center(45, "-"),)
print("See you later ;)".center(45, "="))
print("".center(45, "-"))
print("".center(45, "="))