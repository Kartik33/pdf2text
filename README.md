# A Package for converting pdf files to text files.

You must have the following dependencies installed.
 - pdf2image
 - cv2
 - pytesseract
  
There are four options to run the program

1 Put the pdf files in the /pdf folder and run the program using the command
      `python run.py`

2 You can also give path of the single pdf file 
      `python run.py -f pathToFile.pdf`

3 Or path to the directory of pdf files
      `python run.py -d pathToDirectory`

4 If you are converting documents like research papers and want to remove the footer
  then you can use the -l option
     <br>`python run.py -l`   
       It will remove the footer's content as shown below and then convert into text file

<p float="left">
  <img src="https://github.com/Kartik33/pdf2text/blob/master/sample/Screenshot%20from%202020-08-15%2017-35-47.png" width="300" />
  <img src=https://github.com/Kartik33/pdf2text/blob/master/sample/Screenshot%20from%202020-08-15%2017-36-07.png width="300" /> 
</p>

**The text files will be generated in the /txt folder** 
