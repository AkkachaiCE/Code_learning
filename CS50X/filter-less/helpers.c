#include "helpers.h"
#include <math.h>
// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average_color = 0;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            average_color = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = average_color;
            image[i][j].rgbtGreen = average_color;
            image[i][j].rgbtBlue = average_color;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int sepiaRed = 0;
    int sepiaGreen = 0;
    int sepiaBlue = 0;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            sepiaRed = round(0.393 * image[i][j].rgbtRed + 0.769 * image[i][j].rgbtGreen + 0.189 * image[i][j].rgbtBlue);
            sepiaGreen = round(0.349 * image[i][j].rgbtRed + 0.686 * image[i][j].rgbtGreen + 0.168 * image[i][j].rgbtBlue);
            sepiaBlue = round(0.272 * image[i][j].rgbtRed + 0.534 * image[i][j].rgbtGreen + 0.131 * image[i][j].rgbtBlue);
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int swapRed[width];
    int swapGreen[width];
    int swapBlue[width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            swapRed[j] = image[i][j].rgbtRed;
            swapGreen[j] = image[i][j].rgbtGreen;
            swapBlue[j] = image[i][j].rgbtBlue;
        }
        for (int k = 0; k < width; k++)
        {
            image[i][k].rgbtRed = swapRed[width - k - 1];
            image[i][k].rgbtGreen = swapGreen[width - k - 1];
            image[i][k].rgbtBlue = swapBlue[width - k - 1];
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    int copy_image_Red[height][width];
    int copy_image_Green[height][width];
    int copy_image_Blue[height][width];
    RGBTRIPLE copy[height][width];
    // Copy the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
            // copy_image_Red[i][j] = image[i][j].rgbtRed;
            // copy_image_Green[i][j] = image[i][j].rgbtGreen;
            // copy_image_Blue[i][j] = image[i][j].rgbtBlue;
        }
    }
    // Blur Operation
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // inside Operation with Loop to calculate Average
            float Pixel_pass = 0.0; // Pixel count to Divided
            int Accu_Red = 0;
            int Accu_Green = 0;
            int Accu_Blue = 0;
            // count pixel process
            for (int m = -1; m < 2; m++)
            {
                for (int n = -1; n < 2; n++)
                {
                    if ((i + m) < 0 || (i + m) > (height - 1) || (j + n) < 0 || (j + n) > (width - 1))
                    {
                        Pixel_pass = Pixel_pass + 0;
                    }
                    else
                    {
                        Accu_Red = Accu_Red + copy[i + m][j + n].rgbtRed;
                        Accu_Green = Accu_Green + copy[i + m][j + n].rgbtGreen;
                        Accu_Blue = Accu_Blue + copy[i + m][j + n].rgbtBlue;
                        Pixel_pass++;
                    }
                }
            }
            // Average of each color the divide
            //  Red / pixel_pass
            //  Green / pixel_pass
            //  Blue / pixel_pass
            //  Update Blur Pixel
            image[i][j].rgbtRed = round(Accu_Red / Pixel_pass);
            image[i][j].rgbtGreen = round(Accu_Green / Pixel_pass);
            image[i][j].rgbtBlue = round(Accu_Blue / Pixel_pass);
        }
    }
    return;
}
