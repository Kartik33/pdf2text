# A Package for converting pdf files to text files.

You must have the following dependencies installed.
 - pdf2image
 - cv2
 - pytesseract
  
There are three options to run the program

    Put the pdf files in the /pdf folder and run the program using the below command
      `python run.py`

    You can also give path of the single pdf file 
      `python run.py -f pathToFile.pdf`

    or directory of pdf files
      `python run.py -d pathToDirectory`

The text files will be generated in the /txt folder 
