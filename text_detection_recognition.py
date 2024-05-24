import cv2
import easyocr
import matplotlib.pyplot as plt

# read image
image_path = 'test.png'

img = cv2.imread(image_path)
reader = easyocr.Reader(['en'], gpu=False)

# detect text on images
text_ = reader.readtext(img)
threshold = 0.25

for t in text_:
    bbox, text, score = t
    print(f"Detected text: {text} (Score: {score})")
    
    # Draw bounding box
    top_left = tuple(bbox[0])
    bottom_right = tuple(bbox[2])
    
    if score > threshold:
	    img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
	    
	    # Put detected text
	    img = cv2.putText(img, text, top_left, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 3)

# Convert BGR image to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Display the image
plt.figure(figsize=(10, 10))
plt.imshow(img_rgb)
plt.axis('off') 
plt.show()

