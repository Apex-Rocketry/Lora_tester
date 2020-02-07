import serial
import time

# pegar um pacote com tamanho definido e ir aumentando a frequencia de envio até falhar

b = 0
delay = 1
a = 0
ser = serial.Serial(port="COM31", baudrate=115000)  # open serial port
while b < 200:

    # message = "Pacote: " + str(b) + " Delay: " + str("{:.8f}".format(delay)) + "\n
    if b < 10:
        message = str(b) + "_1234560123456789012345678901234567890123456789012345678901234567890123456789\n"
    elif 10 <= b < 100:
        message = str(b) + "_123450123456789012345678901234567890123456789012345678901234567890123456789\n"
    elif 100 <= b:
        message = str(b) + "_12340123456789012345678901234567890123456789012345678901234567890123456789\n"

    time.sleep(0.41)
    ser.write(str(message).encode('ascii'))
    print(message)
    b += 1

ser.close()
print(ser.name)  # check which port was really usedser.write(b'hello')     # write a string
# close port
