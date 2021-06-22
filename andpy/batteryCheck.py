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
    batteryData = list(droid.batteryGetLevel())
    batteryData = batteryData[1] + "%"
    batteryData_Name = "nivel"

  elif response == "plug":
    batteryResults = {
      "-1": "desconocido",
      "0": "desconectado",
      "1": "conectado a AC",
      "2": "conectado a USB"
    }

    batteryData = list(droid.batteryGetPlugType())
    batteryData = str(batteryData[1])
    batteryData_Name = "Plug Micro USB"

    if batteryData in batteryResults.keys():
      batteryData = batteryResults.get(batteryData)

  elif response == "status":
    batteryResults = {
      "1": "desconocido",
      "2": "cargando",
      "3": "descargando",
      "4": "no cargando",
      "5": "completa"
    }

    batteryData = list(droid.batteryGetStatus())
    batteryData = batteryData[1]
    batteryData_Name = "estatus"

    if batteryData in batteryResults.keys():
      batteryData = batteryResults.get(batteryData)

  elif response == "health":
    batteryResults = {
      "1": "desconocido",
      "2": "bien",
      "3": "sobrecalentado",
      "4": "muerta",
      "5": "sobre voltaje",
      "6": "error sin especificar"
    }

    batteryData = list(droid.batteryGetHealth())
    batteryData = batteryData[1]
    batteryData_Name = "estado de salud"

    if batteryData in batteryResults.keys():
      batteryData = batteryResults.get(batteryData)

  elif response == "tech":
    batteryData = list(droid.batteryGetTechnology())
    batteryData = batteryData[1]
    batteryData_Name = "dato tecnologíco"

  elif response == "temp":
    batteryData = list(droid.batteryGetTemperature())
    batteryData = list(str(batteryData[1]))
    batteryData.insert(-1, ".")
    batteryData = "".join(batteryData) + "°C"
    batteryData_Name = "grado de temperatura"

  elif response == "volt":
    batteryData = list(droid.batteryGetVoltage())
    batteryData = batteryData[1] + "mv"
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