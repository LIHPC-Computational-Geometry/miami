import numpy as np
import os


from pylatex import Document, Command, Section, Subsection, Figure, Alignat, NoEscape, SubFigure
from pylatex.utils import italic
import os

def getStepFiles(d):
    l=[]
    for sdp,Lsd, Lnf in os.walk(d):
        for f in Lnf:
            if(f.endswith(".step")):
               l.append(f)
    l.sort()
    return l


def fillModel(doc,model_name):
    doc.append(NoEscape("\medskip"))
    img_X = model_name+'_X.png'
    img_Y = model_name+'_Y.png'
    img_Z = model_name+'_Z.png'
    img_XYZ = model_name+'_XYZ.png'
    doc.append(NoEscape('{'))
    doc.append(Command('centering'))
    with doc.create(Figure(position='htbp')) as imgs:
        with doc.create(SubFigure(width=NoEscape(r'0.24\linewidth'))) as img:
            img.add_image(img_X)
        with doc.create(SubFigure(width=NoEscape(r'0.24\linewidth'))) as img:
            img.add_image(img_Y)
        with doc.create(SubFigure(width=NoEscape(r'0.24\linewidth'))) as img:
            img.add_image(img_Z)
        with doc.create(SubFigure(width=NoEscape(r'0.24\linewidth'))) as img:
            img.add_image(img_XYZ)
        imgs.add_caption("Model "+model_name)
    doc.append(Command('par'))
    doc.append(NoEscape('}'))

    
if __name__ == '__main__':

    
    current_dir = os.getcwd()

    geometry_options = {"rmargin": "1cm",
                        "lmargin": "1cm",
                        "tmargin": "1cm",
                        "bmargin": "2cm", }
    doc = Document(geometry_options=geometry_options)

    basic_dir = current_dir+"/../Basic"
    simple_dir = current_dir+"/../Simple"
    medium_dir = current_dir+"/../Medium"

    doc.append("Some illustrations of the different models available in the ManBO database\n")
    with doc.create(Section('Basic models')):
        for f in getStepFiles(basic_dir):
            base_f = f.replace(".step", "")
            fillModel(doc,base_f)

    doc.append(NoEscape("\pagebreak"))
    with doc.create(Section('Simple models')):
        for f in getStepFiles(simple_dir):
            base_f = f.replace(".step", "")
            fillModel(doc,base_f)

    doc.append(NoEscape("\pagebreak"))
    with doc.create(Section('Medium  models')):
        for f in getStepFiles(medium_dir):
            base_f = f.replace(".step", "")
            fillModel(doc,base_f)


    doc.generate_pdf('report')
