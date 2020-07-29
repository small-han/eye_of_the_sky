#include "opencv2/core/core.hpp"
#include "opencv2/calib3d/calib3d.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/core/utility.hpp"
#include "opencv2/ximgproc/disparity_filter.hpp" 

#include <stdio.h>
#include <iostream>
#include <string.h>
#include <vector>
#include <iostream>
#include <dirent.h>
#include <sys/types.h>
#include <algorithm>
#include <unistd.h>
#include "stero-vision/calibracao.h"
#include "stero-vision/disparidade.h"


class Client()
{
    public:
        Client(std:string path):boardPath(path){}
        ~Client(){

            if(cal) delete cal;
            if(dis) delete dis;
            
            //camera management
            SAFE_DELETE(camera_left);
	        SAFE_DELETE(camera_right);
        }
        initClient();
        VideoCapture();
    
    
    private:
        // camera 
          
	    gstCamera* camera_left //load camera_left and cameraleft
	    gstCamera* camera_right //load camera_left and cameraleft
	
        //stereo-vision
        calibracao* cal;
        disparidade* dis;
        std:string boardPath;
        //human detection
}
