# NOTE: These functions have been overly-commented so as to explain
# them to people unfamiliar with OpenCV.

# NOTE: In the comments, "OpenCV image" means "numpy.ndarray object
# containing image data that OpenCV works with."

import cv2
import numpy as np

def open(filename):
    """Returns an OpenCV image of an image file."""
    cv2_im = cv2.imread(filename)
    if cv2_im is None:
        raise FileNotFileError('No image file named ' + filename)
    return cv2_im

def save(cv2_im, filename='image.png'):
    """Saves the OpenCV image in cv2_im as an image file.
    The file extension in the filename string determines the
    image format (.png, .jpg, .bmp, .webp, etc.)"""
    cv2.imwrite(filename, cv2_im)

def grayscale(cv2_im):
    """Returns an OpenCV image of cv2_im as a grayscale image."""
    return cv2.cvtColor(cv2_im, cv2.COLOR_BGR2GRAY)

def binarize(cv2_im, threshold=127):
    """Returns an OpenCV image of cv2_im as a black and white bitmap.
    Any pixels lighter than (that is, greater than) threshold
    will be set to 255. (255 is white, 0 is black.)"""
    cv2_im = grayscale_image(cv2_im)
    return cv2.threshold(cv2_im, threshold, 255, cv2.THRESH_BINARY)[1]

def brightness(cv2_im, setting):
    """Returns an OpenCV image of cv2_im with changed brightness.
    The brightness value can range from -1.0 to 1.0. Negative
    values darken the image and positive values brighten it."""
    setting = min(max(setting, -1.0), 1.0)
    cv2_im = cv2_im.astype(np.float32) / 255.0
    cv2_im = cv2_im + setting
    cv2_im = np.clip(cv2_im, 0, 1)
    return (cv2_im * 255).astype(np.uint8)

def contrast(cv2_im, setting):
    """Returns an OpenCV image of cv2_im with changed contrast.
    A contrast value greater than 1 increase contrast, while
    values between 0 and 1 decrease contrast."""
    setting = max(setting, 0)
    cv2_im = cv2_im.astype(np.float32) / 255.0
    mean = np.mean(cv2_im)
    cv2_im = (cv2_im - mean) * setting + mean
    cv2_im = np.clip(cv2_im, 0, 1)
    return (cv2_im * 255).astype(np.uint8)

def invert(cv2_im):
    """Returns an OpenCV image of cv2_im with the colors inverted."""
    return cv2.bitwise_not(cv2_im)

def thin_lines(cv2_im):
    """Returns an OpenCV image of cv2_im with black lines thinned."""
    kernel = np.ones((2, 2), np.uint8)
    return cv2.dilate(cv2_im, kernel)

def thicken_lines(cv2_im):
    """Returns an OpenCV image of cv2_im with black lines thickened."""
    kernel = np.ones((2, 2), np.uint8)
    return cv2.erode(cv2_im, kernel)

def denoise(cv2_im):
    """Returns an OpenCV image of cv2_im denoise."""
    kernel = np.ones((1, 1), np.uint8)
    cv2_im = cv2.morphologyEx(cv2_im, cv2.MORPH_OPEN, kernel)
    cv2_im = cv2.morphologyEx(cv2_im, cv2.MORPH_CLOSE, kernel)
    cv2_im = cv2.medianBlur(cv2_im, 3)
    return cv2_im

def crop(cv2_im, crop_size=10):
    """Returns an OpenCV image of cv2_im with cropped edges."""
    height, width = cv2_im.shape[:2]
    new_height = height - crop_size
    new_width = width - crop_size
    return cv2_im[crop_size:new_height, crop_size:new_width]

def add_border(cv2_im, border_size=None, border_color=(255, 255, 255), top=10, bottom=10, left=10, right=10):
    """Returns an OpenCV image of cv2_im with an added white border."""
    if border_size is not None:
        top = border_size
        bottom = border_size
        left = border_size
        right = border_size

    return cv2.copyMakeBorder(cv2_im,
        top=top, bottom=bottom,
        left=left, right=right,
        borderType=cv2.BORDER_CONSTANT,
        value=border_color)  # White color. Uses BGR, not RGB.









#https://becominghuman.ai/how-to-automatically-deskew-straighten-a-text-image-using-opencv-a0c30aed83df
import numpy as np

def getSkewAngle(cvImage) -> float:
    # Prep image, copy, convert to gray scale, blur, and threshold
    newImage = cvImage.copy()
    gray = cv2.cvtColor(newImage, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (9, 9), 0)
    thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

    # Apply dilate to merge text into meaningful lines/paragraphs.
    # Use larger kernel on X axis to merge characters into single line, cancelling out any spaces.
    # But use smaller kernel on Y axis to separate between different blocks of text
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (30, 5))
    dilate = cv2.dilate(thresh, kernel, iterations=2)

    # Find all contours
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key = cv2.contourArea, reverse = True)
    for c in contours:
        rect = cv2.boundingRect(c)
        x,y,w,h = rect
        cv2.rectangle(newImage,(x,y),(x+w,y+h),(0,255,0),2)

    # Find largest contour and surround in min area box
    largestContour = contours[0]
    print (len(contours))
    minAreaRect = cv2.minAreaRect(largestContour)
    cv2.imwrite("temp/boxes.jpg", newImage)
    # Determine the angle. Convert it to the value that was originally used to obtain skewed image
    angle = minAreaRect[-1]
    if angle < -45:
        angle = 90 + angle
    return -1.0 * angle

# Rotate the image around its center
def rotateImage(cvImage, angle: float):
    newImage = cvImage.copy()
    (h, w) = newImage.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    newImage = cv2.warpAffine(newImage, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return newImage

def _deskew(cvImage):
    angle = getSkewAngle(cvImage)
    return rotateImage(cvImage, -1.0 * angle)


im = open_image()

"""
def ocr(filename):
    import pytesseract as tess
    from PIL import Image

    img = Image.open(filename)
    return tess.image_to_string(img)
"""

"""
# Automated border detection, but it doesn't work very well.
def remove_borders(image):
    contours, heiarchy = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cntsSorted = sorted(contours, key=lambda x:cv2.contourArea(x))
    cnt = cntsSorted[-1]
    x, y, w, h = cv2.boundingRect(cnt)
    crop = image[y:y+h, x:x+w]
    return (crop)
"""




'''
import os

# Convert all jpgs in folder to png
for filename in os.listdir():
    if filename.endswith('.jpg'):
        print(f'Converting {filename} to {filename[0:-4] + '.png'}...')
        im = open_cv2_image(filename)
        save_cv2_image(im, filename[0:-4] + '.png')

'''
