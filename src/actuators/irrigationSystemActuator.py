from actuatorInterface import actuatorInterface


class irrigationSystemActuator(actuatorInterface):

    def enable(self):
        # do something
        print('Irrigations System actuator is active')

    def disable(self):
        # do something
        print('Irrigations System actuator is not active')
