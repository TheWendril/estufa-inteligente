from src.actuators.actuatorInterface import actuatorInterface


class CoolerActuator(actuatorInterface):

    def enable(self):
        # do something
        print('Cooler actuator is active')

    def disable(self):
        # do something
        print('Cooler actuator is not active')
