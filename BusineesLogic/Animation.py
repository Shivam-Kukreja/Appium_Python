from Data_Source import XML_Reader
from Library import Common_Functionalities
from Object_Repository import Elements

def get_visibleBttns():
    visiblebutton = Elements.bttn_coln()
    List =visiblebutton.find_elements_by_class_name(XML_Reader.Element("button", "sub_class"))
    size=len(List)
    return size

def animation_hidetest():
    try:
        Common_Functionalities.press(Elements.getAnimation_tab())
        Common_Functionalities.press(Elements.getHideShow())
        Common_Functionalities.press(Elements.HideShow_Tab())
        bttnnumbrs=get_visibleBttns()
        Common_Functionalities.press(Elements.hide0())
        bttnnumbrs=bttnnumbrs-1
        Common_Functionalities.press(Elements.hide1())
        bttnnumbrs=bttnnumbrs-1
        bttnsleft=get_visibleBttns()
        if bttnnumbrs==bttnsleft:
            return True
        else:
            return False
    except Exception as e:
        print("Error:"+ str(e))
        return False

def animation_showtest():
    try:
        Common_Functionalities.press(Elements.show_btn())
        numbbttns=get_visibleBttns()
        if numbbttns==4:
            return True
        else:
            return False
    except Exception as e:
        return False