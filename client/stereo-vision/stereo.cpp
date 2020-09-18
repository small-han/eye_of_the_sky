#include "stereo.h"
namespace stereovis{
stereo::stereo()
{
    safe_distance=500;
}

stereo::~stereo()
{
}

void stereo::run(string left_addr, string right_addr)
{
    imLeft = cv::imread(left_addr);
    imRight = cv::imread(right_addr);
    // imwrite("../data/1.jpg", imLeft);
    //calibracao c(imLeft, imRight);
    //c.iniciaCalibracaoCamera();
    disparidade d(imLeft, imRight);
    d.iniciaDisparidade();
    d.getDisparity();
    d.get3DLocation(lo);
}

bool stereo::Compute_Distance(int x1, int y1, int x2, int y2)
{
	std::cout<<"begin compute disctance"<<std::endl;
    auto p1 = Point(x1, y1);
    auto p2 = Point(x2, y2);
    auto xyz1 = lo.at<Vec3f>(p1);
    auto xyz2 = lo.at<Vec3f>(p2);
    std::cout<<xyz1[0]<<" "<<xyz2[0]<<" "<<xyz1[1]<<" "<<xyz2[1]<<" "<<xyz1[2]<<" "<<xyz2[2]<<std::endl;
    float distance = std::sqrt(std::pow(xyz1[0] - xyz2[0], 2)+ std::pow(xyz1[1] - xyz2[1], 2)+ std::pow(xyz1[2] - xyz2[2],2));
	std::cout<<"finish cmopute disctance"<<std::endl;
	std::cout<<"distance:"<<distance<<std::endl;
    if (distance < safe_distance)
    {
        return true;
    }
    else
    {
        return false;
    }
}

void stereo::Overlay_Red(int top,int bottom,int left,int right)
{
    cv::rectangle(imLeft,cvPoint(left,top),cvPoint(right,bottom),cvScalar(0,0,255),2);
}

void stereo::Overlay_Green(int top,int bottom,int left,int right)
{
    cv::rectangle(imLeft,cvPoint(left,top),cvPoint(right,bottom),cvScalar(0,255,0),2);
}

void stereo::Save(std::string addr)
{
    cv::imwrite(addr,imLeft);
}
}
