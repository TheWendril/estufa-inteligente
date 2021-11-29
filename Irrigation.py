import time
from src.actuators.IrrigationSystemActuator import IrrigationSystemActuator
from src.EITP.EITPMessenger import EITPType, EITPMessengerActuator

if __name__ == '__main__':
    actuator = IrrigationSystemActuator()
    eitp = EITPMessengerActuator('127.0.0.1', 35000)
    my_id = eitp.connect(EITPType.ACTUATOR, 'Irrigation')

    while True:
        response = eitp.sync(my_id)
        if response == 1:
            actuator.enable()
        elif response == 0:
            actuator.disable()

        time.sleep(2)