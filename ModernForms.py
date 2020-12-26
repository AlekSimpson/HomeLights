import modernforms

ip = '192.168.50.248'

fan = modernforms.ModernFormsFan(ip)

def controlLight(setting):
    fan.light_on = setting

def controlFan(speed, fanOn=True, direction=True):
    # Direction: 
    #   True is counter clockwise
    #   False is clock wise (winter)

    fan.fan_on = fanOn
    fan.fan_direction = direction
    fan.fan_speed = speed

controlLight(True)
# controlFan(0)

