
import ujson
from const import deviceid

store = {
    "deviceid" : deviceid, 
    "batterylevel" : 0, 
    "charging" : False,
    "dosage" : 0, 
    "fluidlevel" : 0, 
    "lightcolor" : "", 
    "lightluminosity" : 0, 
    "lighton" : False, 
    "maintenance" : False, 
    "passersby" : 0, 
    "signalstrength" : 0, 
    "uses" : 0
}

def mutate(newstate):
    if newstate is not None:
        store.update(newstate)
        ujson.dump(store, open("device.json", "wb"))
    return store

def state(key=None):
    if key is not None:
        return store[key]
    return store

try:
    persisdedstore = ujson.load(open("device.json", "rb"))
except:
    ujson.dump(store, open("device.dat", "wb"))
else:
    store = mutate(persisdedstore)