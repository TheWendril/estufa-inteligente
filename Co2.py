import time
from src.sensor.co2Sensor import CO2Sensor
from src.EITP.EITPMessenger import EITPMessengerSensor
from src.EITP.EITPBaseData import EITPType

if __name__ == '__main__':
    sensor = CO2Sensor()
    eitp = EITPMessengerSensor('127.0.0.1', 35000)
    my_id = eitp.connect(EITPType.SENSOR, 'CO2Sensor')

    while True:
        data = CO2Sensor.monitoring(self=None)
        time.sleep(4)
        eitp.send(data, my_id)

