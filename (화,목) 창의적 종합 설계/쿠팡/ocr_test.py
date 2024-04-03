from paddleocr import PaddleOCR

ocr=PaddleOCR(lang="korean")

img_path="Untitled.jpg"
result=ocr.ocr(img_path, cls=False)

ocr_result=result[0]
print(ocr_result)