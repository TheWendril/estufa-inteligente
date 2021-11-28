from src.sensor.sensorDataInterface import sensoDataInterface
from src.EITP.EITPMessengerBase import EITPMessengerBaseSensor
from src.EITP.EITPBaseData import EITPType

if __name__ == '__main__':
    sensor = sensoDataInterface()
    eitp = EITPMessengerBaseSensor('', 14)
    my_id = eitp.connect(EITPType.SENSOR, 'sensorDataInterface')

    while True:
        data = moistureSensor.monitoring()
        eitp.send(my_id, data)