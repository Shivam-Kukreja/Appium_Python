import xml.dom.minidom
import xml.etree.ElementTree as ET
from pathlib import Path
import os

def Element(Header,Key):
    try:
        path = Path(__file__).parent.parent
        path = os.path.join(path,'Resources')
        os.chdir(path)
        with open("ELement.xml") as file:
            root = ET.parse(file).getroot()
        type_tag = root.find(Header)
        attribute=type_tag.find(Key)
        return(attribute.text)
    except FileNotFoundError:
        print("File not in directory")
        return None