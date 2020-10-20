import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Read the image file
image = cv2.imread('11.jpg')
cv2.imshow("Image",image)
cv2.waitKey(0)

# Use tesseract convert image to string
text=pytesseract.image_to_string(image,lang='eng')
print(text)
