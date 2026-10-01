# Real-Time Hand Gesture Recognition System

A real-time computer vision application that uses a webcam to detect hand landmarks and recognize predefined hand gestures using Python, OpenCV, MediaPipe, and NumPy.

## Overview

This project captures live video from a webcam and processes each frame to detect hand landmarks. The positions of the fingers are analyzed to identify predefined hand gestures.

The recognized gesture is displayed directly on the video feed along with the detected hand landmarks.

## Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy

## Features

- Real-time webcam-based hand detection
- Hand landmark detection and tracking
- Gesture recognition
- Live gesture display
- Support for multiple predefined gestures
- Visual hand landmark connections

## Recognized Gestures

| Gesture | Symbol |
|---|---|
| Peace | ✌️ |
| Point | ☝️ |
| Fist | ✊ |
| Open Palm | 🖐️ |
| Thumbs Up | 👍 |

## How It Works

1. The application accesses the system webcam.
2. Video frames are captured using OpenCV.
3. Each frame is converted into the required color format.
4. MediaPipe detects hand landmarks.
5. Finger positions are analyzed.
6. The detected finger configuration is compared with predefined patterns.
7. The recognized gesture is displayed on the video feed.

## Installation

Install the required Python libraries:

```bash
pip install opencv-python mediapipe numpy
