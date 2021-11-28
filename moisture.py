import time
from src.sensor.moistureSensor import moistureSensor
from src.EITP.EITPMessengerBase import EITPMessengerBaseSensor
from src.EITP.EITPBaseData import EITPType

if __name__ == '__main__':
    sensor = moistureSensor()
    eitp = EITPMessengerBaseSensor('187.19.149.17', 11)
    my_id = eitp.connect(EITPType.SENSOR, 'moistureSensor')

    while True:
        data = moistureSensor.monitoring()
        time.sleep(2)
        eitp.send(my_id, data)
