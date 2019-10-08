import uasyncio as asyncio

async def connect():
    """ connects to a wifi network """
    
    import network
    import store
    from const import essid, password

    sta_if = network.WLAN( network.STA_IF )
    ap_if = network.WLAN( network.AP_IF )

    sta_if.active( True ) # enable staion mode
    ap_if.active( False ) # disable accesspoint mode

    if not sta_if.isconnected():
        print('connecting to wifi')
        sta_if.connect( essid, password )
        while not sta_if.isconnected():
            await asyncio.sleep(1)

    store.mutate({'signalstrength': (100 + sta_if.status('rssi')) })
    print('wifi connected rssi:', store.state('signalstrength'))

async def wakereason(state):
    """ determines the waking reaspn """
    from machine import reset_cause, DEEPSLEEP_RESET, WDT_RESET

    if reset_cause() == DEEPSLEEP_RESET:
        print('woken from deep sleep')
        state.emit('deepsleepwake')
    
    elif reset_cause() == WDT_RESET:
        print('woken from watch dog reset')
        state.emit('watchdogwake')

    else:
        print('woken by hard reset')
        state.emit('resetwake')

async def isHandInserted(state):
    """ polling: the APDS9960 proximity sensor to see if a hand is inserted"""
    
    import apds9960 
    
    proximityhigh = 10       # the proximity value where a hand is inserted
    proximitylow = 2         # the proximity value where a hand is removed
    proximitypolltime = 0.1  # how often the proximity is polled (seconds)

    apds9960.enable()

    while 1:
        
        proximity = apds9960.readProximity()
      
        if proximity > proximityhigh :
            state.emit('handinserted')
          
        if proximity < proximitylow :
            state.emit('handremoved')

        await asyncio.sleep( proximitypolltime )



async def isFluidLow(state):
    """ polling: is the fluid low """
    import store
    from const import SCK, DAT
    from hx711 import read, scale
    
    high = 95
    low = 5
    polltime = 10
    rawmin = 0
    rawmax = 32000
    rangemin = 0
    rangemax = 100
  
    read(SCK, DAT) # initialize the sensor
    await asyncio.sleep(1) # let the sensor settle

    while 1:

        # read a value and 
        fluidvalue = read(SCK, DAT)
         
        # scale the raw value to a usefull value 
        fluidlevel = scale(
            fluidvalue, 
            rawmin,
            rawmax,
            rangemin,
            rangemax
        )

        print('fluidlevel ', fluidlevel)

        # update the fluid level
        store.mutate({'fluidlevel': fluidlevel })

        if fluidlevel > high :
            state.emit('fluidfull')
        
        if fluidlevel < low :
            state.emit('fluidlow')

        await asyncio.sleep( polltime ) #seconds

async def insert_devicehistory():
    """ inserts a devices device history record """
    from gql import devicehistory_mutate
    
    while True:
        await connect()
        devicehistory_mutate()
        await asyncio.sleep(30)

async def dispense():
    """ dispences an amount of fluid"""
    import store

    print('valve on')
    print('pump on')
    await asyncio.sleep_ms( 500 )
    print('pump off')
    print('valve off')

    # increment the uses count
    store.mutate({'uses': store.state('uses') + 1})
    


async def ledflash():
    """ flashes the led """
    from const import LED
    from machine import Pin
    led = Pin( LED, Pin.OUT )
    while 1:
        led.value( 0 )
        await asyncio.sleep_ms( 1 )
        led.value( 1 )
        await asyncio.sleep( 5 )

async def sleep():
    """ pushes the device into a deep sleep mode  """
    from machine import RTC, DEEPSLEEP, deepsleep

    await asyncio.sleep(3)

    print('.... in deep sleep zzZz')
    # configure RTC.ALARM0 to be able to wake the device
    rtc = RTC()
    rtc.irq(trigger=rtc.ALARM0, wake=DEEPSLEEP)

    # set RTC.ALARM0 to fire after 10 seconds (waking the device)
    rtc.alarm(rtc.ALARM0, 10000)

    # put the device to sleep
    deepsleep()
    

