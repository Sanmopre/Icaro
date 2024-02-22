#!/bin/bash

# Build RF24 library
cd RF24
make
sudo make install
cd ..

# Build Icaro
mkdir -p build
cd build
cmake ..
make
