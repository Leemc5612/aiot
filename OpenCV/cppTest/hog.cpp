#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

String folder = "/home/lmc/aiot/OpenCV/cppTest/data/";

int main()
{
    Mat src = imread(folder + "kids.png");
    HOGDescriptor hog;
    hog.setSVMDetector(HOGDescriptor::getDefaultPeopleDetector());
    vector<Rect> detected;
    hog.detectMultiScale(src, detected);
    rectangle(src, detected[0], Scalar(0,0,255), 3);
    
    waitKey();
    return 0;
}