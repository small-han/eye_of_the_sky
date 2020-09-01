cmake_minimum_required(VERSION 2.8)

# declare my-recognition project
project(Jetson)

include_directories(/usr/include/gstreamer-1.0 /usr/lib/aarch64-linux-gnu/gstreamer-1.0/include /usr/include/glib-2.0 /usr/include/libxml2 /usr/lib/aarch64-linux-gnu/glib-2.0/include/ /usr/include/opencv4 ./detect /usr/local/include/opencv4 ./stereo-vision ./com ./com/easywsclient)

# CUDA is required
find_package(CUDA)
find_package(jetson-utils)
find_package(jetson-inference)
find_package(OpenCV REQUIRED)


# compile the my-recognition program
cuda_add_executable(out ./stereo-vision/calibracao.cpp ./stereo-vision/disparidade.cpp ./stereo-vision/stereo.cpp ./com/com.cpp ./com/easywsclient/easywsclient.cpp main.cpp ./detect/detect.cpp )

# link my-recognition to jetson-inference library
target_link_libraries(out PRIVATE jetson-inference)
target_link_libraries(out PRIVATE ${OpenCV_LIBS})
