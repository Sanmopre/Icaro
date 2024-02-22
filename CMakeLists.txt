cmake_minimum_required(VERSION 3.10)
project(Icaro)

set(CMAKE_CXX_STANDARD 14)

link_directories(/usr/local/lib)
include_directories(/usr/local/include/RF24)

file(GLOB SOURCE_FILES 
     "./src/*.cpp" 
     "./src/*.h" 
     "./src/*.hpp" 
     "./src/*.c" 
     "./src/*.cc" 
     "./src/*.hh")


add_executable(Icaro ${SOURCE_FILES})

target_link_libraries(Icaro rf24)