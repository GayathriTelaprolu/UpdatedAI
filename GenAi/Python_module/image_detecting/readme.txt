This code snippet uses OpenCV to perform various image processing tasks, including image resizing, cropping, rotation, and face detection. It is divided into two sections:

1. Basic Image Manipulation:
Loading an image: The image is loaded from the specified file path using cv2.imread().
Resizing the image: The image is resized to 800x600 pixels using cv2.resize().
Cropping the image: A cropped version of the image is created using array slicing, selecting a region from coordinates (100, 100) to (400, 400).
Rotating the image: The image is rotated by 45 degrees around its center using a rotation matrix (cv2.getRotationMatrix2D()) and cv2.warpAffine() for the transformation.
Saving and displaying: The resized, cropped, and rotated images are saved to disk using cv2.imwrite() and displayed using cv2.imshow().
2. Face Detection:
Loading the face detection model: A pre-trained Haar Cascade classifier is used to detect faces (haarcascade_frontalface_default.xml).
Converting to grayscale: The input image is converted to grayscale using cv2.cvtColor() for better face detection performance.
Detecting faces: The cv2.CascadeClassifier.detectMultiScale() method detects faces in the image.
Drawing rectangles: Rectangles are drawn around the detected faces using cv2.rectangle().
Saving and displaying the result: The image with detected faces is saved and displayed.
The script processes images in different ways and performs face detection, with results shown visually through pop-up windows and saved files.