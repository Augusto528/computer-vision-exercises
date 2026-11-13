# Exercise 02 - Homography Estimation using RANSAC

## Overview

This exercise focuses on estimating a homography matrix between two images using the **Normalized Direct Linear Transformation (DLT)** algorithm combined with **RANSAC (Random Sample Consensus)**.

The implementation uses feature detection and matching to identify corresponding points between images, estimate a geometric transformation, and align one image with another through perspective warping.

## Objectives

- Implement point normalization for improved numerical stability.
- Construct the DLT equation system to estimate a homography matrix.
- Implement the Normalized DLT algorithm using Singular Value Decomposition (SVD).
- Develop a RANSAC algorithm to identify inliers and reject outliers.
- Detect and match image features using SIFT and FLANN.
- Apply the estimated homography to perform perspective transformation.

## Methodology

The implementation is divided into the following stages:

### 1. Feature Detection and Matching

- Detect keypoints and compute descriptors using SIFT.
- Match descriptors between the two images using FLANN.
- Apply Lowe's ratio test to filter unreliable matches.

### 2. Normalized DLT

- Calculate the centroid of the corresponding points.
- Normalize the points so that their average distance from the origin is √2.
- Construct the DLT matrix.
- Estimate the homography using Singular Value Decomposition (SVD).
- Denormalize the resulting homography matrix.

### 3. RANSAC

- Randomly select four pairs of corresponding points.
- Estimate a candidate homography using Normalized DLT.
- Evaluate the candidate model against all corresponding points.
- Classify points as inliers or outliers based on a distance threshold.
- Update the required number of iterations according to the current inlier ratio and desired confidence level.
- Re-estimate the final homography using all selected inliers.

### 4. Image Alignment

- Apply the estimated homography using OpenCV's `warpPerspective()`.
- Compare the original images and the resulting perspective transformation.

## Technologies and Libraries

- Python
- NumPy
- OpenCV
- Matplotlib
- Math (Python standard library)

## Requirements

Install the required dependencies:

```bash
pip install numpy matplotlib opencv-contrib-python
```

**Note:** The implementation uses `cv.SIFT_create()`. The OpenCV installation must provide SIFT support.

## Input Files

The application example uses two grayscale images:

- `box.jpg` - Reference image.
- `photo01a.jpg` - Image in which the reference object is located.

Both files must be available in the working directory when executing the script, or their paths must be adjusted accordingly.

## Parameters

The RANSAC implementation uses the following parameters in the application example:

| Parameter | Value | Description |
|---|---:|---|
| `dis_threshold` | 5.0 | Maximum reprojection distance for an inlier |
| `N` | 2000 | Maximum number of iterations |
| `s` | 4 | Minimum number of point correspondences |
| `confianca` | 0.99 | Desired confidence level |
| `MIN_MATCH_COUNT` | 10 | Minimum number of accepted feature matches |

## Expected Results

The application displays:

1. Feature matches between the two images.
2. The original reference image.
3. The second image.
4. The reference image after applying the estimated perspective transformation.

The resulting transformation should align the reference object with its corresponding location in the second image.

## Authors

- [Augusto Lopes Zanotelli](https://github.com/Augusto528)
- [Fernanda Coutinho Correa Calazans](https://github.com/)

## Academic Context

Developed collaboratively as part of a Computer Vision course assignment.

---

*This exercise was developed for educational purposes, focusing on geometric transformations, feature matching, homography estimation, and robust model fitting.*