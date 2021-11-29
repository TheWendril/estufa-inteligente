import time
from src.actuators.HeaterActuator import HeaterActuator
from src.EITP.EITPMessenger import EITPType, EITPMessengerActuator

if __name__ == '__main__':
    actuator = HeaterActuator()
    eitp = EITPMessengerActuator('127.0.0.1', 35000)
    my_id = eitp.connect(EITPType.ACTUATOR, 'Heater')

    while True:
        response = eitp.sync(my_id)
        if response == 1:
            actuator.enable()
        elif response == 0:
            actuator.disable()

        time.sleep(2)
