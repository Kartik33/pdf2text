import argparse
from glob import glob
import Pdf_to_text

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="If file path", required=False)
parser.add_argument("-d", "--dir", help="If Dir path", required=False)
parser.add_argument("-l","--line", help="If want to remove the footer", required=False, action='store_true')

args = parser.parse_args()

isLine = False
DEFAULT_PATH = "pdf/"

if args.line:
    isLine = True

if args.file and args.dir:
    exit("can not use file and dir option at the same time")
elif args.file:
    pdf2text = Pdf_to_text.PDF_TO_TEXT(args.file, "file", isLine)
elif args.dir:
    pdf2text = Pdf_to_text.PDF_TO_TEXT(args.dir, "dir", isLine)
else:
    path_li = glob(DEFAULT_PATH+"*.pdf")
    if path_li:
        pdf2text = Pdf_to_text.PDF_TO_TEXT(DEFAULT_PATH, "dir",isLine)
    else:
        exit("Please place the files in the pdf folder"\
        " or specify the path using -f or -d option")
        
pdf2text.convert()