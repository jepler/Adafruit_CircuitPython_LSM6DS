import time
import board
import busio
import adafruit_lsm6dsox
from adafruit_debug_i2c import DebugI2C

#i2c = busio.I2C(board.SCL, board.SDA)
i2c = DebugI2C(busio.I2C(board.SCL, board.SDA))

"""
FS = ±2 g 0.061
mg/LSB
FS = ±4 g 0.122
FS = ±8 g 0.244
FS = ±16 g 0.488
"""
sox = adafruit_lsm6dsox.LSM6DSOX(i2c)
sox.gyro_range = adafruit_lsm6dsox.GyroRange.RANGE_250_DPS
sox.range = adafruit_lsm6dsox.Range.RANGE_4G
# print(sox._raw_gyro_data[0][0])
# print(sox._raw_temp)256 LSB/°C
for i in range(2):
# while True:
    # print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2"%(sox.acceleration))
    # print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s"%(sox.gyro))
    # print("Temperature: %.2f C"%sox._raw_temp)
    # print("")
    print("(%.2f, %.2f, %.2f)"%(sox.acceleration))
    #print("(%.2f, %.2f, %.2f)"%(sox.gyro))
    # print("Gyro X:%.2f, Y: %.2f, Z: %.2f degrees/s"%(sox.gyro))
    # print("Temperature: %.2f C"%sox._raw_temp)
    # print("")
    time.sleep(0.2)