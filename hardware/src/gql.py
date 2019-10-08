
from const import url,deviceid
from gqlclient import execute

def ping_mutate():

    print('ping_mutate')
    execute('''
        mutation {
            insert_ping(objects: {deviceid: "12345678"}) {
                returning {
                created_at
                }
            }
        }
    ''')
    

def devicehistory_mutate():
    """ inserts a devices device history record """

    import store
    print('devicehistory_mutate ...')
    
    result = execute('''
        mutation insert_devicehistory($batterylevel: Int, $charging: Boolean, $deviceid: uuid, $dosage: Int, $fluidlevel: Int, $lightcolor: String, $lightluminosity: Int, $lighton: Boolean, $maintenance: Boolean, $passersby: Int, $signalstrength: Int, $uses: Int){
            insert_devicehistory(objects: {batterylevel: $batterylevel, charging: $charging, deviceid: $deviceid, dosage: $dosage, fluidlevel: $fluidlevel, lightcolor: $lightcolor, lightluminosity: $lightluminosity, lighton: $lighton, maintenance: $maintenance, passersby: $passersby, signalstrength: $signalstrength, uses: $uses}) {
                returning {
                    eventid
                }
            }
        }
    ''', store.state())

    print(result)