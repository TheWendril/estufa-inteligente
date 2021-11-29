import time
from src.sensor.moistureSensor import moistureSensor
from src.EITP.EITPMessenger import EITPMessengerSensor
from src.EITP.EITPBaseData import EITPType

if __name__ == '__main__':
    sensor = moistureSensor()
    eitp = EITPMessengerSensor('127.0.0.1', 35000)
    my_id = eitp.connect(EITPType.SENSOR, 'moistureSensor')

    while True:
        data = moistureSensor.monitoring()
        time.sleep(2)
        eitp.send(data, my_id)
