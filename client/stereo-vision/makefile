LIB=-L/usr/local/lib/
INC=-I/usr/local/include/opencv4
CFLAGS=-std=c++11

default: clean test

test: test.cpp calibracao.cpp disparidade.cpp
	g++ $(LIB) $(INC) $(CFLAGS) test.cpp stereo.cpp calibracao.cpp disparidade.cpp -lopencv_core -lopencv_videoio -lopencv_highgui -lopencv_imgcodecs -lopencv_imgproc -lopencv_calib3d -lopencv_features2d -lopencv_ximgproc -o test

clean: 
	rm -rf test
