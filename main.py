import serial
import time

# pegar um pacote com tamanho definido e ir aumentando a frequencia de envio até falhar

b = 0
ser = serial.Serial(port="COM5", baudrate=115000)  # open serial port
while True:
    time.sleep(0.05)
    b += 1
    a = str(b) +   "\n"
    print(a)
    ser.write(str(a).encode('ascii'))
    '''
    ser.write(b":11111111111111111111111111111111111111111111111111111111111:\n")
    time.sleep(0.1)'''


ser.close()
print(ser.name)         # check which port was really usedser.write(b'hello')     # write a string
           # close port