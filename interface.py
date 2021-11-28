from src.sensor.sensorInterface import sensorInterface
from src.EITP.EITPMessengerBase import EITPMessengerBaseSensor
from src.EITP.EITPBaseData import EITPType

if __name__ == '__main__':
    sensor = sensorInterface()
    eitp = EITPMessengerBaseSensor('', 13)
    my_id = eitp.connect(EITPType.SENSOR, 'sensorInterface')

    while True:
        data = moistureSensor.monitoring()
        eitp.send(my_id, data)