#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace std;

String folder = "/home/lmc/aiot/OpenCV/cppTest/data/";

int main()
{
    Mat src = imread(folder + "sudoku.bmp", IMREAD_GRAYSCALE);
    Mat dst1, dst2, dst3;
    threshold(src, dst1, 0, 255, THRESH_OTSU);
    threshold(src, dst1, 150, 255, THRESH_BINARY);
    adaptiveThreshold(src, dst3, 255, ADAPTIVE_THRESH_GAUSSIAN_C, THRESH_BINARY, 10, 5);
    imshow("src", src);
    imshow("dst1", dst1);
    imshow("dst2", dst2);
    imshow("dst3", dst3);

    waitKey();
    return 0;
}