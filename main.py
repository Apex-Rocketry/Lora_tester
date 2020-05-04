import serial
import time
# pegar um pacote com tamanho definido e ir aumentando a frequencia de envio até falhar
b = 0

'''
80 bytes:

  19.2 Kbps: delay 0.2
  9.6 Kbps: delay 0.28
  4.8 Kbps: delay 0.42
  2.4 Kbps: delay 0.3
  1.2 Kbps: delay 0.4
  0.3 Kbps: delay 0.5

'''

delay = 0.4 
a= 0
ser = serial.Serial(port="COM3", baudrate=115000)  # open serial port
while b < 200:
    while a < 10:
        message = "Sequencia: " + str(b) + " Pacote: " + str(a) + " Delay: " + str("{:.2f}".format(delay)) + " _1234567891011121314151617181920212223242526\n"
        a += 1
        round(delay, 4)
        time.sleep(delay)
        ser.write(str(message).encode('ascii'))
        print(message)
    a = 0
    b += 1
ser.close()
print(ser.name)         # check which port was really usedser.write(b'hello')     # write a string
           # close port
# diminuir airdatarate e ver quanto conseguimos mandar