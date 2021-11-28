import time
from src.sensor.temperatureSensor import temperatureSensor
from src.EITP.EITPMessengerBase import EITPMessengerBaseSensor
from src.EITP.EITPBaseData import EITPType


if __name__ == '__main__':
    sensor = temperatureSensor('187.19.149.17', 10)
    eitp = EITPMessengerBaseSensor()
    my_id = eitp.connect(EITPType.SENSOR, 'TemperatureSensor')

    while True:
        data = temperatureSensor.monitoring()
        time.sleep(2)
        eitp.send(my_id, data)
