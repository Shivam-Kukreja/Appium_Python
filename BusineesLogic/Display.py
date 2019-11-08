from Base import Driver
from Library import Common_Functionalities
from Object_Repository import Elements

def Display_Options():
    try:
        Driver.driver.back()
        Driver.driver.back()
        Common_Functionalities.press(Elements.getApp_tab())
        Common_Functionalities.press(Elements.actn_bar())
        Common_Functionalities.press(Elements.dsp_optn())
        Common_Functionalities.press(Elements.show_TtlBtn())
        if not Elements.get_Title():
            Common_Functionalities.press(Elements.show_TtlBtn())
            if Elements.get_Title():
                return True
        else:
            return False
    except Exception as e:
        print(str(e))
        return False