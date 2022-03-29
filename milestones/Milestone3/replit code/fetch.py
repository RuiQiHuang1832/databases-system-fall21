def grab(msg):
  val = int(msg[18:-3])
  return val

def grabblood(msg):
  value = msg[19:-4]
  return value  

def grabdate(msg):
    thedate = msg[-4:25]
    return thedate

def getyear(msg):
   theyear = msg[16:27]
   return theyear

def getbloodtype(msg):
    bloodtype = msg[27:29]
    return bloodtype

def getamount(msg):
    words = msg.split()
    return words[-1]

def passorfail(msg):
    word = msg[21:25]
    return word

def getwalkin(msg):
    word = msg.split()
    return word[-1]

def getincentive(msg):
  word = msg.split()
  return word[-2]        

  