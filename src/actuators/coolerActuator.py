from actuatorInterface import actuatorInterface


class coolerActuator(actuatorInterface):

    def enable(self):
        # do something
        print('Cooler actuator is active')

    def disable(self):
        # do something
        print('Cooler actuator is not active')
