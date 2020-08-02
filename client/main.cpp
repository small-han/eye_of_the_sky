#include "stereo.h"
#include "detect.h"
int main()
{
    detect my_detect = detect();
    stereo my_stereo = stereo();
    char buf[200]={'0'};
    getcwd(buf,200);
    std::string s(buf);
    s+=("/../data/");
    while (1)
    {
        my_detect.CaptureRGBA();//capture frame from two cameras
        my_detect.detect_left();//detect the frame from left camera
        my_detect.Save_RGBA(s+"out1.jpg", s+"out2.jpg");//save frame
        my_stereo.run(s+"out1.jpg", s+"out2.jpg");//stereo 

        for (int i = 0; i < my_detect.numDetections; i++) // compute the distance between every two person
        {
            for (int j = i; j < my_detect.numDetections; j++) 
            {
                if ((my_detect.Get_ID(i) == "person") && (my_detect.Get_ID(j) == "person"))//make sure the detection is "person" instead of "dog",etc...
                {
                    float top, bottom, left, right;
                    my_detect.Get_Pos(i, top, bottom, left, right);//get the position of i
                    int i_x = int((left + right) / 2), i_y = int((top + bottom) / 2);

                    my_detect.Get_Pos(j, top, bottom, left, right);//get the position of j
                    int j_x = int((left + right) / 2), j_y = int((top + bottom) / 2);

                    if(!my_stereo.Compute_Distance(i_x,i_y,j_x,j_y))//if the computed distance smaller than safe distance
                    {
                        my_detect.OverLay_Left(i);
                        my_detect.OverLay_Left(j);
                    }

                }
            }
        }
        my_detect.Save_RGBA(s+"out1.jpg",s+"out2.jpg");
        //TODO:we need to trans the "out1.jpg" from jetbot to server
    }
}