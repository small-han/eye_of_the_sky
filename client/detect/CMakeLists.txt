cmake_minimum_required(VERSION 2.8)

# declare my-recognition project
project(my-recognition)

include_directories(/usr/include/gstreamer-1.0 /usr/lib/aarch64-linux-gnu/gstreamer-1.0/include /usr/include/glib-2.0 /usr/include/libxml2 /usr/lib/aarch64-linux-gnu/glib-2.0/include/ /usr/include/opencv4)

# import jetson-inference and jetson-utils packages.
# note that if you didn't do "sudo make install"
# while building jetson-inference, this will error.
find_package(jetson-utils)
find_package(jetson-inference)

# CUDA is required
find_package(CUDA)

# compile the my-recognition program
cuda_add_executable(detect detect.cpp detect.h test1.cpp)

# link my-recognition to jetson-inference library
target_link_libraries(detect jetson-inference)