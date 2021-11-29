from src.sensor.sensorDataInterface import sensoDataInterface
from src.EITP.EITPMessenger import EITPMessengerSensor
from src.EITP.EITPBaseData import EITPType

if __name__ == '__main__':
    sensor = sensoDataInterface()
    eitp = EITPMessengerSensor('', 14)
    my_id = eitp.connect(EITPType.SENSOR, 'sensorDataInterface')

    while True:
        data = moistureSensor.monitoring()
        eitp.send(my_id, data)