'''
import cv2

# Load the image
image = cv2.imread(r'C:\\Users\\HP\\OneDrive\\Desktop\\image.jpeg')  # Use double backslashes
# OR
# image = cv2.imread('C:/Users/HP/OneDrive/Desktop/image.jpeg')  # Use forward slashes
# OR
# image = cv2.imread('C:\\Users\\HP\\OneDrive\\Desktop\\image.jpeg')  # Use double backslashes

# Resize the image
resized_image = cv2.resize(image, (800, 600))

# Crop the image (x, y, width, height)
cropped_image = image[100:400, 100:400]

# Rotate the image
center = (image.shape[1] // 2, image.shape[0] // 2)
rotation_matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

# Save the edited images
cv2.imwrite('resized_image.jpg', resized_image)
cv2.imwrite('cropped_image.jpg', cropped_image)
cv2.imwrite('rotated_image.jpg', rotated_image)

# Display the images
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Cropped Image', cropped_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
import cv2

# Load the cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the image
image = cv2.imread(r'C:\Users\HP\OneDrive\Pictures\image.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around the detected faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Save and display the result
cv2.imwrite('detected_faces.jpg', image)
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

