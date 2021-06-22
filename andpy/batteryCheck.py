# Made By Bl4ky113

import androidhelper
droid = androidhelper.Android()

conditional = True

while conditional:
  batteryData = ""
  batteryData_Name = ""

  response = input("Ingrese que Información quiere ver: ")
  droid.batteryStartMonitoring()

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
    droid.batteryStopMonitoring()

  elif response == "help":
    message = [
      "Ingresa 'level' para ver el % de tu batería\n", 
      "Ingresa 'plug' para ver el estado del plug Micro USB\n", 
      "Ingresa 'status' para ver el estado de tu bateria\n", 
      "Ingresa 'health' para ver el estado de salud de tu bateria\n", 
      "Ingresa 'tech' para ver la tecnologia de tu bateria\n",
      "Ingresa 'temp' para ver la temperatura de tu celular\n",
      "Ingresa 'volt' para ver el voltaje de tu celular\n",
      "Ingresa 'close' para terminar el programa\n"
    ]
    print("".join(message))

  else: 
    print("Opción no aceptada, intenta escribir 'help' para ver las opciones disponibles")

  if conditional == True and batteryData != "" or batteryData_Name != "":  
    print("El", batteryData_Name ,"de la Bateria es de: ", batteryData)

print("Hasta luego ;)")