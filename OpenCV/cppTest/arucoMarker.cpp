#include "opencv2/opencv.hpp"
#include "opencv2/aruco.hpp"
#include <iostream>

using namespace cv;
using namespace std;

String folder = "/home/lmc/aiot/OpenCV/cppTest/data/";
ptr<aruco::Dictionary>dictionary(aruco::DICT_6X6_250);


int main()
{
    Mat src = imread(folder + "frame.png");
    imshow("src", src);

    vector<int> markerIds;
    vector<vector<point2f>> markerCorners;

    aruco::drawDetectedMarkers(frame, markerCorners, markerIds);
    
    waitKey();
    return 0;
}
