# Made By Bl4ky113

import pywhatkit
from datetime import datetime

celNumber = input("Ingrese su Celular:  ")
currentTime = {
  "time": datetime.now(),
  "hour": datetime.now().hour,
  "min": datetime.now().minute,
  "sec": datetime.now().second
}
try:
  pywhatkit.sendwhatmsg(celNumber, "Quiubo", currentTime["hour"], currentTime["min"] + 1)

except:
  print("No se pudo contactar a su Número")
