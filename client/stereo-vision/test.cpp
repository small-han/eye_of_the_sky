#include "opencv2/core/core.hpp"
#include "opencv2/calib3d/calib3d.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/core/utility.hpp"
#include "opencv2/ximgproc/disparity_filter.hpp" 

#include "calibracao.h"
#include "disparidade.h"
#include <stdio.h>
#include <iostream>
#include <string.h>
#include <vector>
#include <iostream>
#include <dirent.h>
#include <sys/types.h>
#include <algorithm>
#include <unistd.h>


int main()
{
    cv::Mat imLeft =  cv::imread("/home/jetbot/eye_of_the_sky/client/stereo-vision/data/outL.jpg");
    cv::Mat imRight = cv::imread("/home/jetbot/eye_of_the_sky/client/stereo-vision/data/outR.jpg");
    cv::Mat imOut, lo;
    stereovis::calibracao c(imLeft, imRight);
    c.iniciaCalibracaoCamera();
    // c.recitify(imLeft, imRight, imOut);
    // imshow("Recitied",imOut);
    // auto key=waitKey(0);
    stereovis::disparidade d(imLeft, imRight);
    d.iniciaDisparidade();
    d.getDisparity();
    d.get3DLocation(lo);
    auto p = cv::Point(500, 500);
    std::cout<<"corrdinate"<<lo.at<cv::Vec3f>(p)<<std::endl;
    return 0;
}
/*
#include "stereo.h"
int main()
{
    stereo my_stereo = stereo();
    my_stereo.run("../data/outL.jpg","../data/outR.jpg");

}
*/