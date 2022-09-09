import fitz  # install with 'pip install pymupdf'
import glob
import os
from pathlib import Path
from itertools import groupby

csv_filename = "Reporte Titanium 2022"

def print_and_get_hightlight_text(page, rect):
    """Return text containted in the given rectangular highlighted area.

    Args:
        page (fitz.page): the associated page.
        rect (fitz.Rect): rectangular highlighted area.
    """
    words = page.get_text("words")  # list of words on page
    words.sort(key=lambda w: (w[3], w[0]))  # ascending y, then x
    mywords = [w for w in words if fitz.Rect(w[:4]).intersects(rect)]
    group = groupby(mywords, key=lambda w: w[3])
    for y1, gwords in group:
        highlighted_text = " ".join(w[4] for w in gwords)
        print(highlighted_text)
        return highlighted_text


def list_of_highlighted_text_from(document_filename:str):
    doc = fitz.Document(document_filename)
    print(len(doc))
    list_of_words = []
    for i in range(len(doc)):
      page = doc[i]
      # print(type(page))
      # print(page.first_annot)
      annot = page.first_annot
      while annot:
          if annot.type[0] in (8, 9, 10, 11): # one of the 4 types above
              rect = annot.rect # this is the rectangle the annot covers
              # extract the text within that rect ...
              words = print_and_get_hightlight_text(page, rect)
              list_of_words.append(words)
          annot = annot.next # None returned after last annot
    return list_of_words

file_extension = ".pdf"
path = "./*"+file_extension
files = glob.glob(path)

with open(csv_filename + ".csv", "w") as f:
    for docpath in files:
        doc_filename = Path(os.path.basename(docpath)).stem
        list_words = list_of_highlighted_text_from(docpath)
        f.write(doc_filename+file_extension)
        f.write(",")
        f.write(",".join(list_words))
        f.write("\n")

