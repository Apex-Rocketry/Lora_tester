import serial
import time
# versao do teteu
ser = serial.Serial(port="COM4", baudrate=115000)  # open serial port
while True:
    ser.write(b":00000000000000000000000000000000000000000000000000000000000:\n")
    time.sleep(0.1)
    '''
    ser.write(b":11111111111111111111111111111111111111111111111111111111111:\n")
    time.sleep(0.1)'''


ser.close()
print(ser.name)         # check which port was really usedser.write(b'hello')     # write a string
           # close port