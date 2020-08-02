#include "opencv2/core/core.hpp"
#include "opencv2/calib3d/calib3d.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include "opencv2/core/utility.hpp"
#include "opencv2/ximgproc/disparity_filter.hpp"

#include <stdio.h>
#include <math.h>
#include <iostream>
#include <string.h>
#include <vector>
#include <iostream>
#include <dirent.h>
#include <sys/types.h>
#include <algorithm>
#include <unistd.h>
#include "calibracao.h"
#include "disparidade.h"

namespace stereovis{
class stereo
{
private:
    cv::Mat lo;
    float safe_distance;

public:
    stereo();
    ~stereo();

    void run(string left_addr,string right_addr);
    bool Compute_Distance(int x1,int y1,int x2,int y2);
};
}