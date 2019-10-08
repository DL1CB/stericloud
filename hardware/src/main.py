import uasyncio as asyncio  #https://github.com/peterhinch/micropython-async/blob/master/TUTORIAL.md

import store
from const import version
from states import StateMachine
from tasks import connect, wakereason, isHandInserted , ledflash, insert_devicehistory,isFluidLow

print('\n\n hygenie - v',version, ' id:', store.state('deviceid'))

# start a statemachine that represents the differing states that the device can be in
state = StateMachine()

# the async event loop prevents tasks from blocking each other
loop = asyncio.get_event_loop()

loop.create_task( insert_devicehistory() )

loop.create_task( wakereason(state) )
loop.create_task( isHandInserted(state) )
loop.create_task( isFluidLow(state) )  
loop.create_task( ledflash() )  

loop.run_forever()

