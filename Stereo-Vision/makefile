LIB=-L/usr/local/opt/opencv@3/lib
INC=-I/usr/local/opt/opencv@3/include
CFLAGS=-std=c++11

default: clean demo test

demo:
	g++ $(LIB) $(INC) $(CFLAGS) filteredDisparityMap.cpp -lopencv_core -lopencv_videoio -lopencv_highgui -lopencv_imgcodecs -lopencv_imgproc -lopencv_calib3d -lopencv_features2d -lopencv_ximgproc -o demo

test: 
	./demo

clean: 
	rm -rf demo
