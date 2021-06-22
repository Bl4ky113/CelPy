# Made By Bl4ky113

import androidhelper
droid = androidhelper.Android()

conditional = True

while conditional:
  response = input("Ingrese que Información quiere ver: ")

  if response == "level":
    batteryData = droid.batteryGetLevel()
    batteryData_Name = "nivel"

  elif response == "plug":
    batteryData = droid.batteryGetPlugType()
    batteryData_Name = "Plug Micro USB"

  elif response == "status":
    batteryData = droid.batteryGetStatus()
    batteryData_Name = "estatus"

  elif response == "health":
    batteryData = droid.batteryGetHealth()
    batteryData_Name = "estado de salud"

  elif response == "tech":
    batteryData = droid.batteryGetTechnology()
    batteryData_Name = "dato tecnologíco"

  elif response == "temp":
    batteryData = droid.batteryGetTemperature()
    batteryData_Name = "grado de temperatura"

  elif response == "volt":
    batteryData = droid.batteryGetVoltage()
    batteryData_Name = "voltaje"

  elif response == "close":
    conditional = False

  elif response == "help":
    print("fuck u")

  else: 
    print("Opción no aceptada, intenta escribir 'help' para ver las opciones disponibles")
  
  print("El", batteryData_Name ,"de la Bateria es de: ", batteryData)
