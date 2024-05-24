# Text Detection and Recognition using EasyOCR and OpenCV

![Example Output](example_output.png)

## Overview

This Python script utilizes EasyOCR and OpenCV to detect and recognize text in images. It draws bounding boxes around the detected text and displays the result visually.

## Requirements

- **Python 3.x**
- **OpenCV**: For image processing tasks.
- **EasyOCR**: For optical character recognition.
- **Matplotlib**: For displaying the processed image.

You can install the required libraries using pip:

```bash
pip install opencv-python easyocr matplotlib
```

## Usage

1. **Clone or Download**: Obtain a copy of this repository.
2. **Navigate to Directory**: Open your terminal and navigate to the directory containing the script.
3. **Specify Input Image**: Replace `'test.png'` with the path to your input image within the script.
4. **Run Script**: Execute the script by running the following command:

    ```bash
    python text_detection_recognition.py
    ```

## Output

The script will display the input image with bounding boxes drawn around the detected text. The recognized text will be overlaid on top of the image.

## Customization

- **Threshold Adjustment**: Modify the `threshold` variable to control the minimum confidence score for displaying text. Lower values show more text but may include false positives.

## Example Output

![Example Output](example_output.png)

---
