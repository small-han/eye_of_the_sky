LIB=-L/usr/local/opt/opencv@3/lib
INC=-I/usr/local/opt/opencv@3/include
CFLAGS=-std=c++11

default: clean test

test: test.cpp calibracao.cpp disparidade.cpp
	g++ $(LIB) $(INC) $(CFLAGS) test.cpp calibracao.cpp disparidade.cpp -lopencv_core -lopencv_videoio -lopencv_highgui -lopencv_imgcodecs -lopencv_imgproc -lopencv_calib3d -lopencv_features2d -lopencv_ximgproc -o test

clean: 
	rm -rf test
