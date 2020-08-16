# Convert PDF to text

Install dependencies
```python
pip install pdf2image opencv-python==4.0.0.21 pytesseract
```
  
Run Instructions <br>
* Text files are generated in the **txt** folder.
* Default, all pdf files in **pdf** folder would be processed <br>
```python
python run.py
```
* Single File Processing
```python
python run.py -f <pathToFile.pdf>
```
* Directory Processing <br>
```python
python run.py -d <pathToDirectory>
```
* Options
```python
-l Remove the footer from research paper pdf
```
Sample <br>
<html>
  <body>
    <div><label style='margin-right:20px;'> Input File </label> <label style="margin-left:20px;">Internal Processing </label><label> Output File </label> </div>
    <div>
      <img src="https://github.com/Kartik33/pdf2text/blob/new/sample/Screenshot%20from%202020-08-15%2017-35-47.png" width="300" />
      <img src=https://github.com/Kartik33/pdf2text/blob/new/sample/binary.png width="200" height="200" />
      <img src=https://github.com/Kartik33/pdf2text/blob/new/sample/Screenshot%20from%202020-08-15%2017-36-07.png width="300" /> 
    </div>
    
  </body>
</html>
