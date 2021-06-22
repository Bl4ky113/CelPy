# Made By Bl4ky113

#import androidhelper

conditional = True

while conditional:
  response = input("Ingrese que Información quiere ver: ")

  if response == "level":
    batteryData = batteryGetLevel()
    batteryData_Name = "nivel"

  elif response == "plug":
    batteryData = batteryGetPlugType()
    batteryData_Name = "Plug Micro USB"

  elif response == "status":
    batteryData = batteryGetStatus()
    batteryData_Name = "estatus"

  elif response == "health":
    batteryData = batteryGetHealth()
    batteryData_Name = "estado de salud"

  elif response == "tech":
    batteryData = batteryGetTechnology()
    batteryData_Name = "dato tecnologíco"

  elif response == "temp":
    batteryData = batteryGetTemperature()
    batteryData_Name = "grado de temperatura"

  elif response == "volt":
    batteryData = batteryGetVoltage()
    batteryData_Name = "voltaje"

  elif response == "close":
    conditional = False

  elif response == "help":
    print("fuck u")

  else: 
    print("Opción no aceptada, intenta escribir 'help' para ver las opciones disponibles")
  
  if batteryData and batteryData_Name:
    print("El", batteryData_Name ,"de la Bateria es de: ", batteryData)