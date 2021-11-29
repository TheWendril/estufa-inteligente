import time
from src.sensor.temperatureSensor import temperatureSensor
from src.EITP.EITPMessenger import EITPMessengerSensor
from src.EITP.EITPBaseData import EITPType


if __name__ == '__main__':
    sensor = temperatureSensor('127.0.0.1', 35000)
    eitp = EITPMessengerSensor()
    my_id = eitp.connect(EITPType.SENSOR, 'TemperatureSensor')

    while True:
        data = temperatureSensor.monitoring()
        time.sleep(2)
        eitp.send(data, my_id)
