import cv2
import pytesseract


def demo(a):
    # tesseract path
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    custom_config = r'--oem 3 --psm 6'
    img = cv2.imread(a)
    masage = pytesseract.image_to_string(img, config=custom_config)
    return masage


img = r'C:\Users\vicky\Desktop\images\enti.PNG'  # image file path
# img = cv2.imread('1.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
res = demo(img)
print(res)
