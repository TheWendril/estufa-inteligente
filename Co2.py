import time
from src.sensor.co2Sensor import CO2Sensor
from src.EITP.EITPMessengerBase import EITPMessengerBaseSensor
from src.EITP.EITPBaseData import EITPType

if __name__ == '__main__':
    sensor = CO2Sensor()
    eitp = EITPMessengerBaseSensor('187.19.149.17', 35000)
    my_id = eitp.connect(EITPType.SENSOR, 'CO2Sensor')

    while True:
        data = CO2Sensor.monitoring()
        time.sleep(2)
        eitp.send(my_id, data)
