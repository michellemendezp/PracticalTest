import fitz  # install with 'pip install pymupdf'
from itertools import groupby

document_filename = "STATEMENT136866 (2).pdf"

def print_hightlight_text(page, rect):
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
        print(" ".join(w[4] for w in gwords))

doc = fitz.Document(document_filename)
print(len(doc))

for i in range(len(doc)):
  page = doc[i]
  # print(type(page))
  # print(page.first_annot)
  annot = page.first_annot
  while annot:
      if annot.type[0] in (8, 9, 10, 11): # one of the 4 types above
          rect = annot.rect # this is the rectangle the annot covers
          # extract the text within that rect ...
          print_hightlight_text(page, rect)
      annot = annot.next # None returned after last annot

