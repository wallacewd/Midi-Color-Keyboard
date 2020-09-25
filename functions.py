def printData(myPress, myNote, raw):
   if myPress == 144:
      status = "Key Pressed  >> " 
   elif myPress == 128:
      status = "Key Released >> "
   print(status, "Note: ",myNote)
