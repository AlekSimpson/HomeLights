from IP import ip
import modernforms
from datetime import date, datetime

Y = 2000 # dummy leap year to allow input X-02-29 (leap day)
seasons = [('winter', (date(Y,  1,  1),  date(Y,  3, 20))),
           ('spring', (date(Y,  3, 21),  date(Y,  6, 20))),
           ('summer', (date(Y,  6, 21),  date(Y,  9, 22))),
           ('autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
           ('winter', (date(Y, 12, 21),  date(Y, 12, 31)))]

fanDirections = {'winter' : False, 'summer' : True, 'autumn' : False, 'spring' : True}

fan = modernforms.ModernFormsFan(ip)

def get_season(now):
    if isinstance(now, datetime):
        now = now.date()
    now = now.replace(year=Y)
    return next(season for season, (start, end) in seasons
                if start <= now <= end)

currentSeason = get_season(date.today())

def toggleLight():
    fan.light_on = not fan.light_on

def controlLight(brightness=100):
    fan.light_on = True
    fan.light_brightness = brightness

def toggleFan():
    fan.fan_on = not fan.fan_on
    # fan.fan_speed = speed

def controlFan(speed, on=True, direction=fanDirections[currentSeason]):
    # Direction: 
    #   True is counter clockwise
    #   False is clock wise (winter)
    fan.fan_on = on
    fan.fan_direction = direction
    fan.fan_speed = speed
