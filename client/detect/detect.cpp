#include"detect.h"

detect::detect()
{
    net = detectNet::Create(detectNet::SSD_MOBILENET_V2);
    if (!net)
    {
        printf("failed to load image recognition network\n");
        return ;
    }
    camera_left = gstCamera::Create("0");
    camera_right = gstCamera::Create("1");
    imgRGBA_left = NULL;
    imgRGBA_right = NULL;
}

detect::~detect()
{
    SAFE_DELETE(camera_left);
    SAFE_DELETE(camera_right);
}

void detect::CaptureRGBA()
{
    if (!camera_left->CaptureRGBA(&imgRGBA_left, 1000, 1))
        printf("detectnet-camera:  failed to capture RGBA image from camera\n");

    if (!camera_right->CaptureRGBA(&imgRGBA_right, 1000, 1))
        printf("detectnet-camera:  failed to capture RGBA image from camera\n");
}

void detect::detect_left()
{
    numDetections = net->Detect(imgRGBA_left, camera_left->GetWidth(), camera_left->GetHeight(), &detections, detectNet::OVERLAY_NONE);
}

std::string detect::Get_ID(int index)
{
    if(index>=numDetections)
    {
        return "none";
    }
    std::string str=net->GetClassDesc(detections[index].ClassID);
    return str;
}

void detect::Get_Pos(int index, float &top, float &bottom, float &left, float &right)
{
    if(index>=numDetections)
    {
        return ;
    }
    top = detections[index].Top;
    bottom = detections[index].Bottom;
    left = detections[index].Left;
    right = detections[index].Right;
}

void detect::OverLay_Left(int index)
{
    if(index>=numDetections)
    {
        return ;
    }
    const uint32_t overlayFlags = detectNet::OverlayFlagsFromStr("box");/*label,conf*/
    int j=-1;
    for(int i=0;i<numDetections;i++)
    {
        std::cout<<Get_ID(i)<<std::endl;
        if(Get_ID(i)=="person")
        {
            std::cout<<j<<"   "<<index<<std::endl;
            j++;
            if(index==j)
            {
                std::cout<<"hello";
                detectNet::Detection detection = detections[i];
                net->Overlay(imgRGBA_left, imgRGBA_left, camera_left->GetWidth(), camera_left->GetHeight(), &detection, 1, overlayFlags);
                return;
            }
        }
    }
}

void detect::Save_RGBA(std::string left_str,std::string right_str)
{
    char *left_addr=(char*)left_str.data();
    char *right_addr=(char*)right_str.data();
    if( !saveImageRGBA(left_addr, (float4*)imgRGBA_left, camera_left->GetWidth(), camera_left->GetHeight(), 255.0f) )
		printf("detectnet-console:  failed saving %ix%i image to '%s'\n", camera_left->GetWidth(), camera_left->GetHeight(), "outL.jpg");

	//save the right RGBA
    if(right_str!="none")
        if( !saveImageRGBA(right_addr, (float4*)imgRGBA_right, camera_right->GetWidth(), camera_right->GetHeight(), 255.0f) )
            printf("detectnet-console:  failed saving %ix%i image to '%s'\n", camera_left->GetWidth(), camera_left->GetHeight(), "outR.jpg");
}