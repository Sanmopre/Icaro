from lib_nrf24 import NRF24
import virtGPIO as GPIO
import time

#https://github.com/A33J/virtual-GPIO.git

pipes = [ 0x52, 0x78, 0x41, 0x41, 0x41 ] 
pipesbytes = bytearray(pipes)
radio = NRF24(GPIO, GPIO.SpiDev())
radio.begin(25, 0)
radio.setDataRate(NRF24.BR_250KBPS)

radio.setRetries(3,5)
radio.setPALevel(NRF24.PA_MAX)
radio.openWritingPipe(pipesbytes)
radio.powerUp()
radio.printDetails()
while True:
  print(radio.write(b"Hola"))
  time.sleep(1)
