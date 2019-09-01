import argparse
import os

from .css.parser import parseCSS
from .html.parse import buildTree

ap = argparse.ArgumentParser()
ap.add_argument("document", help="HTML document to render")
ap.add_argument("--stylesheet", help="Optional stylesheet to use with the document", default="__None__")
args = ap.parse_args()

# Check for a valid document file
if not os.path.exists(args.document):
    print("Invalid document file")
    exit(1)

with open(args.document, "r") as fp:
    doc_file = fp.read()
    fp.close()

# Check if a stylesheet has been supplied
if args.stylesheet != "__None__":
    # Check for a valid stylesheet
    if not os.path.exists(args.stylesheet):
        print("Invalid stylesheet file")
        exit(1)

    with open(args.stylesheet, "r") as fp:
        style_file = fp.read()
        fp.close()
else:
    style_file = ""

# Parse the document
# doc_parser = ElementTreeBuilder()
# doc_parser.feed(doc_file)


buildTree(doc_file)
print(parseCSS(style_file))