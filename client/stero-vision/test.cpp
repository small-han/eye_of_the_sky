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
#include <cstring>

int main(){
    char buf[200]={'0'};
    getwd(buf);
    std::string s(buf);
    std::cout<<s<<std::endl;

    if(s.back()!='d')
        s+=("/data/");
    else    
        s+=("/../data/");
    
    cv::Mat imLeft =  cv::imread(s+"outL.jpg");
    cv::Mat imRight = cv::imread(s+"outR.jpg");
    cv::Mat imOut, lo;
    calibracao c(imLeft, imRight);
    c.iniciaCalibracaoCamera();
    // c.recitify(imLeft, imRight, imOut);
    // imshow("Recitied",imOut);
    // auto key=waitKey(0);
    disparidade d(imLeft, imRight);
    d.iniciaDisparidade();
    d.getDisparity();
    d.get3DLocation(lo);
    auto p = Point(500, 500);
    cout<<"corrdinate"<<lo.at<Vec3f>(p)<<endl;
    return 0;
}