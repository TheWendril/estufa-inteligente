import time
from src.actuators.CO2Actuator import CO2Actuator
from src.EITP.EITPMessenger import EITPType, EITPMessengerActuator

if __name__ == '__main__':
    actuator = CO2Actuator()
    eitp = EITPMessengerActuator('127.0.0.1', 35000)
    my_id = eitp.connect(EITPType.ACTUATOR, 'CO2 Injector')

    while True:
        response = eitp.sync(my_id)
        if response == 1:
            actuator.enable()
        elif response == 0:
            actuator.disable()

        time.sleep(4)
