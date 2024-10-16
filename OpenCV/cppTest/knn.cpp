#include "opencv2/opencv.hpp"
#include <iostream>

using namespace cv;
using namespace cv::ml;
using namespace std;

String folder = "/home/lmc/aiot/OpenCV/cppTest/data/";
Ptr<KNearest> train_knn();

int main()
{
    Ptr<KNearest> knn = train_knn();

    Mat img = Mat::zeros(400, 400, CV_8U);
    imshow("img", img);

    waitKey();

    return 0;
}

Ptr<KNearest> train_knn(){
    Mat digits = imread(folder + "digits.png", IMREAD_GRAYCOLOR);
    Mat train_images, train_labels;

    for (int j = 0; j < 50; j++){
        for (int i = 0; i<100; i++){
            Mat roi, roi_float, roi_flatten;
            roi = digits(Rect(i * 20, j * 20, 20, 20));
            roi.convertTo(roi_float, CV_32F);
            roi_flatten = roi_float.reshape(-1, 1);

            train_images.push_back(roi_flatten);
            train_label.push_back(j/5);
        }
    }

    Ptr<KNearest>
}