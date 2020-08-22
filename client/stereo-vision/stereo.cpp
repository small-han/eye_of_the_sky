#include "stereo.h"
namespace stereovis{
stereo::stereo()
{
    safe_distance=100;
}

stereo::~stereo()
{
}

void stereo::run(string left_addr, string right_addr)
{
    cv::Mat imLeft = cv::imread(left_addr);
    cv::Mat imRight = cv::imread(right_addr);
    // calibracao c(imLeft, imRight);
    // c.iniciaCalibracaoCamera();
    disparidade d(imLeft, imRight);
    d.iniciaDisparidade();
    d.getDisparity();
    d.get3DLocation(lo);
}

bool stereo::Compute_Distance(int x1, int y1, int x2, int y2)
{
    auto p1 = Point(y1, x1);
    auto p2 = Point(y2, x2);
    auto xyz1 = lo.at<Vec3f>(p1);
    auto xyz2 = lo.at<Vec3f>(p2);
    float distance = std::sqrt(std::pow(xyz1[0] - xyz2[0], 2)+ std::pow(xyz1[1] - xyz2[1], 2)+ std::pow(xyz1[2] - xyz2[2],2));
    if (distance < safe_distance)
    {
        return true;
    }
    else
    {
        return false;
    }
}
}