#include<opencv2/imgproc.hpp>
#include<opencv2/highgui.hpp>
#include<iostream>

using namespace cv;
using namespace std;

int main(){

    //Read image
    Mat image = imread("../assets/putin.jpg", IMREAD_GRAYSCALE);

    //check if image is empty
    if(image.empty()){
        cout<<"can not find image"<<endl;
        return 0;
    }

    Mat gradientX, gradientY;

    //apply sobel filter for X gradient
    Sobel(image, gradientX, CV_32F, 1, 0);

    //apply sobel filter for Y gradient
    Sobel(image, gradientY, CV_32F, 0, 1);

    //normalize gradient X and gradient Y to display images
    normalize(gradientX, gradientX, 0, 1, NORM_MINMAX);
    normalize(gradientY, gradientY, 0, 1, NORM_MINMAX);

    //create windows to display image
    namedWindow("image", WINDOW_NORMAL);
    namedWindow("imagex", WINDOW_NORMAL);
    namedWindow("imagey", WINDOW_NORMAL);

    //display images
    imshow("image", image);
    imshow("imagex", gradientX);
    imshow("imagey", gradientY);

    //press esc to exit program
    waitKey(0);

    //close all the opened windows
    destroyAllWindows();
    return 0;
}