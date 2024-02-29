sudo apt-get install python3-dev libboost-python-dev python3-setuptools python3-rpi.gpio raspi-config
sudo raspi-config
echo
echo "REBOOTING IS NECESARY TO CONTINUE"
echo
sleep 5

git clone https://github.com/nRF24/RF24 nrf24
cd nrf24
./configure --driver=SPIDEV
make
sudo make install