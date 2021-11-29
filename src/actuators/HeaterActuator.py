from src.actuators.actuatorInterface import actuatorInterface


class HeaterActuator(actuatorInterface):

    def enable(self):
        # do something
        print('Heater actuator is active')

    def disable(self):
        # do something
        print('Heater actuator is not active')
