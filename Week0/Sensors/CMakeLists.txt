cmake_minimum_required(VERSION 3.15)
project(Sensors)

set(CMAKE_CXX_STANDARD 14)

add_executable(Sensors main.cpp sensor.cpp sensor.h sensors.cpp sensors.h)