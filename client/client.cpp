#include "client.h"



void Client::iniClient(){

    // init camera to load camera_left and cameraleft
	amera_left = gstCamera::Create("0");
	camera_right = gstCamera::Create("1");
    //human detection
    
    //steoreo-vision
    cv::Mat imLeft =  cv::imread(boardPath + "outL.jpg");
    cv::Mat imRight = cv::imread(boardPath + "outR.jpg");
    cal = new calibracao(imLeft,imRight);
    c.iniciaCalibracaoCamera();
        
    dis = new disparidade(); /disparity init
    d.iniciaDisparidade();
};


void Client::VideoCapture(){
	float* imgRGBA_left = NULL;
	float* imgRGBA_right = NULL;

	//capture a frame from camera,and convert it to RGBA
	if( !camera_left->CaptureRGBA(&imgRGBA_left, 1000,1) )
		printf("detectnet-camera:  failed to capture RGBA image from camera\n");

	if( !camera_right->CaptureRGBA(&imgRGBA_right, 1000,1) )
		printf("detectnet-camera:  failed to capture RGBA image from camera\n");
    
    // send it to detection
    /*detection module*/
    
    //send it to steoreo vision
    cv::Mat imLeft = cv::Mat(camera_left->GetWidth(), camera_left->GetHeight(), CV_32F, imgRGBA_left);
    cv::Mat imRight = cv::Mat(camera_left->GetWidth(), camera_left->GetHeight(), CV_32F, imgRGBA_right);
    cv::Mat XYZ3D;
    dis->setInput(imLeft,  imRight)
    dis->getDisparity();       // disparity calculation
    dis->get3DLocation(XYZ3D); //location of all pixels in the picture
}

void Client::Transport()
{
    
}