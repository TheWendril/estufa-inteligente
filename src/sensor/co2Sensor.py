from src.sensor.sensorInterface import SensorInterface


class CO2Sensor(SensorInterface):

    def monitoring(self):
        return 1.3
