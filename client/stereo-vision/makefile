LIB=-L/usr/local/lib/
INC=-I/usr/local/include/opencv4
# LIB=-L/usr/local/Cellar/opencv@3/3.4.10_4/lib
# INC=-I/usr/local/Cellar/opencv@3/3.4.10_4/include
CFLAGS=-std=c++11

default: clean test

test: test.cpp calibracao.cpp disparidade.cpp
	g++ -g $(LIB) $(INC) $(CFLAGS) test.cpp calibracao.cpp disparidade.cpp -lopencv_core -lopencv_videoio -lopencv_highgui -lopencv_imgcodecs -lopencv_imgproc -lopencv_calib3d -lopencv_features2d -lopencv_ximgproc -o test

clean: 
	rm -rf test
