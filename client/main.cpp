#include "stereo.h"
#include "detect.h"
#include "soc.h"
int main()
{
    detect my_detect = detect();
    stereovis::stereo my_stereo = stereovis::stereo();
    Comm my_com=Comm();

    char buf[200]={'0'};
    getcwd(buf,200);
    std::string s(buf);
    s+=("/../data/");
    std::cout<<"hello"<<std::endl;

    while (1)
    {
        my_detect.CaptureRGBA();//capture frame from two cameras
        my_detect.detect_left();//detect the frame from left camera
        std::cout<<"num of detections is"<<my_detect.numDetections<<std::endl;
        my_detect.Save_RGBA(s+"out1.jpg", s+"out2.jpg");//save frame
        my_stereo.run(s+"out1.jpg", s+"out2.jpg");//stereo 
        std::cout<<"finish stereo"<<std::endl;

        int flags[30]={0};
        for (int i = 0; i < my_detect.numDetections; i++) // compute the distance between every two person
        {
            for (int j = i+1; j < my_detect.numDetections; j++) 
            {
                if ((my_detect.Get_ID(i) == "person") && (my_detect.Get_ID(j) == "person"))//make sure the detection is "person" instead of "dog",etc...
                {
                    float top, bottom, left, right;
                    my_detect.Get_Pos(i, top, bottom, left, right);//get the position of i
                    int i_x = int((left + right) / 2), i_y = int((top + bottom) / 2);

                    my_detect.Get_Pos(j, top, bottom, left, right);//get the position of j
                    int j_x = int((left + right) / 2), j_y = int((top + bottom) / 2);

                    if(my_stereo.Compute_Distance(i_x,i_y,j_x,j_y))//if the computed distance smaller than safe distance
                    {
                        flags[i]=1;
                        flags[j]=1;
                    }

                }
            }
        }
        std::cout<<"finish computing distance"<<std::endl;
        for (int i=0;i<my_detect.numDetections;i++)
        {
            if(my_detect.Get_ID(i)=="person")
            {
                float top, bottom, left, right;
                my_detect.Get_Pos(i, top, bottom, left, right);//get the position of i
                if(flags[i]==1)
                    my_stereo.Overlay_Red(top,bottom,left,right);
                else 
                    my_stereo.Overlay_Green(top,bottom,left,right);
            }
        }
        std::cout<<"finish overlay"<<std::endl;
        my_stereo.Save(s+"out.jpg");
        std::cout<<"finish save"<<std::endl;
        //TODO:we need to trans the "out1.jpg" from jetbot to server
	my_com.run();
    }
}
