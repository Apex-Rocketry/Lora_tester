import serial
import time


# pegar um pacote com tamanho definido e ir aumentando a frequencia de envio até falhar

b = 0
delay = 0.4
a= 0
ser = serial.Serial(port="COM4", baudrate=115000)  # open serial port
while b < 400:
    while a < 10:
        message = "Sequencia: " + str(b) + " Pacote: " + str(a) + " Delay: " + str("{:.8f}".format(delay)) + "\n"
        a += 1
        round(delay, 4)
        time.sleep(delay)
        ser.write(str(message).encode('ascii'))
        print(message)
    a = 0
    b += 1
    delay = delay * 0.8


ser.close()
print(ser.name)         # check which port was really usedser.write(b'hello')     # write a string
           # close port

# diminuir airdatarate e ver quanto conseguimos mandar
