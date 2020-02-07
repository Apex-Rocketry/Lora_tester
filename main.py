import serial
import time

# pegar um pacote com tamanho definido e ir aumentando a frequencia de envio até falhar

b = 0
delay = 1
a= 0
ser = serial.Serial(port="COM4", baudrate=115000)  # open serial port
while b < 200:
    while a < 10:
        message = "pacote: " + str(a) + " delay: " + str(delay) + "  00000000000000000000000000000000000000000000000000"
        a += 1
        time.sleep(delay)
        ser.write(str(message).encode('ascii'))
        print(message)
    a = 0
    b += 1
    delay = delay * 0.5


ser.close()
print(ser.name)         # check which port was really usedser.write(b'hello')     # write a string
           # close port