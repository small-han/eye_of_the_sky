#include <jetson-inference/detectNet.h>
#include <jetson-utils/loadImage.h>
#include <jetson-utils/imageIO.h>
#include <jetson-utils/gstCamera.h>
#include <opencv2/opencv.hpp>
#include <string>

class detect
{
private:
    detectNet *net;

    gstCamera *camera_left;
    gstCamera *camera_right;

    float *imgRGBA_left;
    float *imgRGBA_right;

    detectNet::Detection *detections;

public:
    int numDetections;
    detect();
    ~detect();
    void CaptureRGBA();
    void detect_left();
    std::string Get_ID(int index);
    void Get_Pos(int index, float &top, float &down, float &left, float &right);
    void OverLay_Left(int index);
    void Save_RGBA(std::string left_str,std::string right_str);
};

