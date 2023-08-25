First, you need to install Tesseract from this link https://github.com/UB-Mannheim/tesseract/wiki. I strongly recommend installing all additional languages. Please do not change the default installation location, it should be "C:\Program Files\Tesseract-OCR". After installation, apply the command ```python pip install -r ./requirements.txt ```. The installation is now complete.

All your images should be placed in a folder named "images" and should be in PNG, JPG or TIFF format. You can now run "main.py", which will translate all your images into text and write them to files of the same name in the "out" folder. Note that if your images have the same name, only one of them will be written to text.

Enjoy using it!
