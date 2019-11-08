from Base import Driver
from Data_Source import XML_Reader
from selenium.common.exceptions import NoSuchElementException

def getAnimation_tab():
    try:
        return Driver.driver.find_element_by_xpath(XML_Reader.Element("button", "get_animation"))
    except NoSuchElementException:
        print("animation tab not found")
        return None

def getHideShow():
    try:
        return Driver.driver.find_element_by_xpath(XML_Reader.Element("button", "hide_show"))
    except NoSuchElementException:
        print("HideShow tab not found")
        return None

def HideShow_Tab():
    try:
        return Driver.driver.find_element_by_xpath(XML_Reader.Element("button", "btn_hide"))
    except NoSuchElementException:
        print("Hide tab not found")
        return None

def bttn_coln():
    try:
        return Driver.driver.find_element_by_xpath(XML_Reader.Element("button", "get_btns"))
    except NoSuchElementException:
        print("bttn column not found")
        return None

def hide0():
    try:
        return Driver.driver.find_element_by_xpath(XML_Reader.Element("button", "hide_0"))
    except NoSuchElementException:
        print("zero bttn not found")
        return None

def hide1():
    try:
        return Driver.driver.find_element_by_xpath(XML_Reader.Element("button", "hide_1"))
    except NoSuchElementException:
        print("bttn one not found")
        return None

def hide2():
    try:
        return Driver.driver.find_element_by_xpath(XML_Reader.Element("button", "hide_2"))
    except NoSuchElementException:
        print("bttn two not found")
        return None

def hide3():
    try:
        return Driver.driver.find_element_by_xpath(XML_Reader.Element("button", "hide_3"))
    except NoSuchElementException:
        print("bttn three not found")
        return None

def show_btn():
    try:
        return Driver.driver.find_element_by_xpath(XML_Reader.Element("button", "show"))
    except NoSuchElementException:
        print("show bttn not found")
        return None

def getApp_tab():
    try:
        return Driver.driver.find_element_by_xpath(XML_Reader.Element("button", "get_app"))
    except NoSuchElementException:
        print("app tab not found")
        return None

def actn_bar():
    try:
        return Driver.driver.find_element_by_xpath(XML_Reader.Element("button", "action_bar"))
    except NoSuchElementException:
        print("action bar not found")
        return None

def dsp_optn():
    try:
        return Driver.driver.find_element_by_xpath(XML_Reader.Element("button", "display_options"))
    except NoSuchElementException:
        print("display option not found")
        return None

def show_TtlBtn():
    try:
        return Driver.driver.find_element_by_xpath(XML_Reader.Element("button", "show_title"))
    except NoSuchElementException:
        print("title bttn not found")
        return None

def get_Title():
    try:
        Driver.driver.find_element_by_xpath(XML_Reader.Element("button", "Text_view"))
        return True
    except Exception as e:
        print("Error:"+ str(e))
        return False