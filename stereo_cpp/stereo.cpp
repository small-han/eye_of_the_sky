
#include <opencv2/opencv.hpp>  
#include <iostream>  

using namespace std;
using namespace cv;

const int imageWidth = 1280;                             //摄像头的分辨率  
const int imageHeight = 720;
Size imageSize = Size(imageWidth, imageHeight);

Mat rgbImageL, grayImageL;
Mat rgbImageR, grayImageR;
Mat rectifyImageL, rectifyImageR;

Rect validROIL;//图像校正之后，会对图像进行裁剪，这里的validROI就是指裁剪之后的区域  
Rect validROIR;

Mat mapLx, mapLy, mapRx, mapRy;     //映射表  
Mat Rl, Rr, Pl, Pr, Q;              //校正旋转矩阵R，投影矩阵P 重投影矩阵Q
Mat xyz;              //三维坐标

int blockSize = 0, uniquenessRatio = 0, numDisparities = 0;

/*
事先标定好的相机的参数
fx 0 cx
0 fy cy
0 0  1
*/
Mat cameraMatrixL = (Mat_<double>(3, 3) << 1288.7, 0, 674.2037,
	0, 1301.5, 308.2639,
	0, 0, 1);
//对应matlab里的左相机标定矩阵
Mat distCoeffL = (Mat_<double>(5, 1) << 0.1618, -0.0729, 0, 0, 0.00000);
//对应Matlab所得左i相机畸变参数

Mat cameraMatrixR = (Mat_<double>(3, 3) << 12838.3, 0, 591.5486,
	0, 1305.8, 325.2182,
	0, 0, 1);
//对应matlab里的右相机标定矩阵

Mat distCoeffR = (Mat_<double>(5, 1) << -0.0051, 0.2492, 0, 0, 0.00000);
//对应Matlab所得右相机畸变参数

Mat T = (Mat_<double>(3, 1) << -60.6342, 0.7088, 6.5490);//T平移向量
                                                    //对应Matlab所得T参数
Mat R=(Mat_<double>(3, 3) << 0.9987, -0.0034, 0.0508,
	0.0048, 0.9996, -0.0273,
	-0.0507, 0.275, 0.9983);
//R 旋转矩阵

void SGBM_compute(Mat &rectifyImageL,Mat &rectifyImageR,Mat &disp);
void BM_compute(Mat &rectifyImageL,Mat &rectifyImageR,Mat &disp);
/*****主函数*****/
int main()
{
	stereoRectify(cameraMatrixL, distCoeffL, cameraMatrixR, distCoeffR, imageSize, R, T, Rl, Rr, Pl, Pr, Q, CALIB_ZERO_DISPARITY,0, imageSize, &validROIL, &validROIR);
	initUndistortRectifyMap(cameraMatrixL, distCoeffL, Rl, Pr, imageSize, CV_32FC1, mapLx, mapLy);
	initUndistortRectifyMap(cameraMatrixR, distCoeffR, Rr, Pr, imageSize, CV_32FC1, mapRx, mapRy);
	grayImageL = imread("outL.jpg",IMREAD_GRAYSCALE );
	grayImageR = imread("outR.jpg",IMREAD_GRAYSCALE );

	remap(grayImageL, rectifyImageL, mapLx, mapLy, INTER_LINEAR);
	remap(grayImageR, rectifyImageR, mapRx, mapRy, INTER_LINEAR);


	Mat disp,disp8;
	//SGBM
	SGBM_compute(rectifyImageL,rectifyImageR,disp);
    imwrite("SGBM.jpg",disp);
	//BM
	BM_compute(rectifyImageL,rectifyImageR,disp);
    imwrite("BM.jpg",disp);

	/*
	disp.convertTo(disp8, CV_8U, 255 / ((numDisparities * 16 + 16)*16.));//计算出的视差是CV_16S格式
    imwrite("out.jpg",disp);
	reprojectImageTo3D(disp, xyz, Q, true); //在实际求距离时，ReprojectTo3D出来的X / W, Y / W, Z / W都要乘以16(也就是W除以16)，才能得到正确的三维坐标信息。
	xyz = xyz * 16;
	*/
    
	return 0;
}

void BM_compute(Mat &rectifyImageL,Mat &rectifyImageR,Mat &disp)
{
	Ptr<StereoBM> bm = StereoBM::create(16, 9);
	bm->setBlockSize(17);     //SAD窗口大小，5~21之间为宜
	bm->setROI1(validROIL);
	bm->setROI2(validROIR);
	bm->setPreFilterCap(31);
	bm->setMinDisparity(0);  //最小视差，默认值为0, 可以是负值，int型
	bm->setNumDisparities(numDisparities * 16 + 16);//视差窗口，即最大视差值与最小视差值之差,窗口大小必须是16的整数倍，int型
	bm->setTextureThreshold(10);
	bm->setUniquenessRatio(uniquenessRatio);//uniquenessRatio主要可以防止误匹配
	bm->setSpeckleWindowSize(100);
	bm->setSpeckleRange(32);
	bm->setDisp12MaxDiff(-1);
	bm->compute(rectifyImageL, rectifyImageR, disp);//输入图像必须为灰度图

}
void SGBM_compute(Mat &rectifyImageL,Mat &rectifyImageR,Mat &disp)
{
	int mindisparity = 0;
	int ndisparities = 64;  
	int SADWindowSize = 11; 
	cv::Ptr<cv::StereoSGBM> sgbm = cv::StereoSGBM::create(mindisparity, ndisparities, SADWindowSize);
	int P1 = 8 * rectifyImageL.channels() * SADWindowSize* SADWindowSize;
	int P2 = 32 * rectifyImageR.channels() * SADWindowSize* SADWindowSize;
	sgbm->setP1(P1);
	sgbm->setP2(P2);
	sgbm->setPreFilterCap(15);
	sgbm->setUniquenessRatio(10);
	sgbm->setSpeckleRange(2);
	sgbm->setSpeckleWindowSize(100);
	sgbm->setDisp12MaxDiff(1);
	//sgbm->setMode(cv::StereoSGBM::MODE_HH);
	sgbm->compute(rectifyImageL, rectifyImageR, disp);
}
