cmake_minimum_required(VERSION 2.8)

set(CMAKE_CXX_FLAGS "${CAMKE_CXX_FLAGS} -std=c++11 ")
project(Jetson)

find_package(OpenCV REQUIRED)
INCLUDE_DIRECTORIES({OpenCV_INCLUDE_DIRS})
add_executable(out ./calibracao.cpp ./disparidade.cpp  ./test.cpp)

target_link_libraries(out ${OpenCV_LIBS})