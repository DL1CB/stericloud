"""low memory footprint implementation of the APDS9960 in Proximity mode only """

from const import SDA, SCL
from machine import Pin, I2C
from micropython import const

#apds9960 ADDRESS
ADDRESS = const(0x39)

#APDS9960 register ADDRESSes
REG_ENABLE  = const(0x80)
REG_PILT    = const(0x89)
REG_PIHT    = const(0x8b)
REG_CONTROL = const(0x8f)
REG_PDATA   = const(0x9c)

#APDS9960 modes
MODE_POWER      = const(0)
MODE_PROXIMITY  = const(2)
MODE_ALL        = const(7)

# LED Drive values
LED_DRIVE_100MA = const(0)

# Proximity Gain (PGAIN) values
PGAIN_4X = const(2)

i2c=I2C(sda=Pin(SDA),scl=Pin(SCL))

def enable():
        """ initalize and enable the APDS9960 """

        # disbale all functions
        setMode(MODE_ALL, False)

        # set proximity gain
        drive = PGAIN_4X
        val = i2c.readfrom_mem(ADDRESS, REG_CONTROL, 1)[0]
        drive &= 0b00000011
        drive = drive << 2
        val &= 0b11110011
        val |= drive
        i2c.writeto_mem(ADDRESS, REG_CONTROL, bytes([val]))

        # set LED drive current
        drive = LED_DRIVE_100MA
        val = i2c.readfrom_mem(ADDRESS, REG_CONTROL, 1)[0]
        drive &= 0b00000011
        drive = drive << 6
        val &= 0b00111111
        val |= drive
        i2c.writeto_mem(ADDRESS, REG_CONTROL, bytes([val]))

        # set proximit interupt low threshold
        #val = 0
        #i2c.writeto_mem(ADDRESS, REG_PILT, bytes([val]))

        # set proximity interup high threshold
        #val = 100
        #i2c.writeto_mem(ADDRESS, REG_PIHT, bytes([val]))

        # enable proximity intterupt
        val = i2c.readfrom_mem(ADDRESS, REG_ENABLE, 1)[0]
        val &= 0b11011111
        val |= 0b00100000
        i2c.writeto_mem(ADDRESS, REG_ENABLE, bytes([val]))
      
        # enable power
        setMode(MODE_POWER, True)
        
        # set proximity mode
        setMode(MODE_PROXIMITY, True)

def setMode(mode, enable=True):
    """ utilty to set APDS9960 modes"""
    # read ENABLE register
    val = i2c.readfrom_mem(ADDRESS, REG_ENABLE, 1)[0]

    # change bit(s) in ENABLE register */
    if mode == MODE_ALL:
        if enable:
            val = 0x7f
        else:
            val = 0x00
    else:
        if enable:
            val |= (1 << mode)
        else:
            val &= ~(1 << mode)

    if isinstance(val, int):
                val = bytes([val]) #writeto_mem expects a buffer

    i2c.writeto_mem(ADDRESS, REG_ENABLE, val)

def readProximity():
    """ read the APDS9960 proximity distance"""
    return i2c.readfrom_mem(ADDRESS, REG_PDATA, 1)[0]

def enablePower():
    """ turn the APDS9960 on """
    setMode(MODE_POWER, True)

def disablePower():
    """ turn the APDS9960 off """
    setMode(MODE_POWER, False)

def disable():
    """ disable the APDS9960 """
    setMode(MODE_ALL,False)
