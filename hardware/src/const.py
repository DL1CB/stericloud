from micropython import const

"""
Micropython | NodeMCU Board
-----------------------------------------
        0   | D3
        2   | D4 (also Led1 but inverse)*
        4   | D2
        5   | D1
        9   | SD2
        10  | SD3
        12  | D6
        13  | D7
        14  | D5
        15  | D8
        16  | D0 (also Led2 but inverse)*
"""

#GPIO
SCL = const(5) #D1 [output mode]
SDA = const(4) #D2 [input & output mode]

DAT = const(13) #D7 [input mode]
SCK = const(15) #D8 [output mode]

LED = const(2) #D4 [output mode]

# Currently unused gpio
D0 = const(16) #D0
D3 = const(0) #D3 
D5 = const(14) #D5
D6 = const(12) #D6

#wifi credentials
essid = 'SummerTime'
password = 'Calmhat436'

#server api url
url = 'https://tryhasura.herokuapp.com/v1/graphql'
deviceid = "ec656488-f941-4e19-ab54-d3853361a86a"
token = None

#versioning
version = const(1)

