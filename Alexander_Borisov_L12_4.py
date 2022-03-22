# HOME WORK 12.4

print('\n----------------\nHOME WORK 12.4\n----------------\n')


print('\nLogger sample program\n')

# my modules

import logging
import random

FORMAT = '%(levelname)s - %(message)s'

# my classes & variables

class BatterySimulation:
    def __init__(self, logger):
        self.logger = logger

    def simulate_last_hour(self):
        for minute in range(1, 60+1):
            temperature = random.randint(20,40)

            if temperature < 30:
                self.logger.debug('{0} C'.format(temperature))
            elif temperature >= 30 and temperature <=35:
                self.logger.warning('{0} C'.format(temperature))
            elif temperature > 35:
                self.logger.critical('{0} C'.format(temperature))
            else:
                raise Exception('Temperature out of range.')

# my program

logger = logging.getLogger('battery.temperature')
logger.setLevel(logging.DEBUG)

handler = logging.FileHandler('battery_temperature.log', mode='w')
handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

battery_simulation = BatterySimulation(logger)
battery_simulation.simulate_last_hour()

input('see the log saved in fie "battery_temperature.log", ok?')
print('\nBye')
