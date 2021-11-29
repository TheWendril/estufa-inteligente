from src.actuators.actuatorInterface import actuatorInterface


class CO2Actuator(actuatorInterface):

    def enable(self):
        # do something
        print('CO2 actuator is active')

    def disable(self):
        # do something
        print('CO2 actuator is not active')
