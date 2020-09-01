#include <jetson-inference/detectNet.h>
#include <jetson-utils/loadImage.h>
#include <jetson-utils/imageIO.h>
#include <jetson-utils/gstCamera.h>
#include <opencv2/opencv.hpp>
int main()
{
	//load ssd_mobilenet_v2
	detectNet* net = detectNet::Create(detectNet::SSD_MOBILENET_V2);
	// check to make sure that the network model loaded properly
	if( !net )
	{
		printf("failed to load image recognition network\n");
		return 0;
	}

	//load camera_left and cameraleft
	gstCamera* camera_left = gstCamera::Create("0");
	gstCamera* camera_right = gstCamera::Create("1");
	
	float* imgRGBA_left = NULL;
	float* imgRGBA_right = NULL;
	
	//capture a frame from camera,and convert it to RGBA
	if( !camera_left->CaptureRGBA(&imgRGBA_left, 1000,1) )
		printf("detectnet-camera:  failed to capture RGBA image from camera\n");

	if( !camera_right->CaptureRGBA(&imgRGBA_right, 1000,1) )
		printf("detectnet-camera:  failed to capture RGBA image from camera\n");

	//detect the RGBA from left camera
	detectNet::Detection* detections = NULL;
	const int numDetections = net->Detect(imgRGBA_left, camera_left->GetWidth(), camera_left->GetHeight(), &detections, detectNet::OVERLAY_NONE);

/*
	const uint32_t overlayFlags = detectNet::OverlayFlagsFromStr("box,labels,conf");
	net->Overlay( imgRGBA_left, imgRGBA_left, camera_left->GetWidth(), camera_left->GetHeight(), detections,  overlayFlags);
	*/

	//print the info about detections
	for( int n=0; n < numDetections; n++ )
	{
		printf("detected obj %u  class #%u (%s)  confidence=%f\n", detections[n].Instance, detections[n].ClassID, net->GetClassDesc(detections[n].ClassID), detections[n].Confidence);
		printf("bounding box %u  (%f, %f)  (%f, %f)  w=%f  h=%f\n", detections[n].Instance, detections[n].Left, detections[n].Top, detections[n].Right, detections[n].Bottom, detections[n].Width(), detections[n].Height()); 
	}

	//save the left RGBA
	if( !saveImageRGBA("outL.jpg", (float4*)imgRGBA_left, camera_left->GetWidth(), camera_left->GetHeight(), 255.0f) )
		printf("detectnet-console:  failed saving %ix%i image to '%s'\n", camera_left->GetWidth(), camera_left->GetHeight(), "outL.jpg");

	//save the right RGBA
	if( !saveImageRGBA("outR.jpg", (float4*)imgRGBA_right, camera_right->GetWidth(), camera_right->GetHeight(), 255.0f) )
		printf("detectnet-console:  failed saving %ix%i image to '%s'\n", camera_left->GetWidth(), camera_left->GetHeight(), "outR.jpg");
	SAFE_DELETE(camera_left);
	SAFE_DELETE(camera_right);
	
}