from actuatorInterface import actuatorInterface


class heaterActuator(actuatorInterface):

    def enable(self):
        # do something
        print('Heater actuator is active')

    def disable(self):
        # do something
        print('Heater actuator is not active')
