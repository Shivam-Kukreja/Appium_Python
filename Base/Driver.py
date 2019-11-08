from appium import webdriver
from Data_Source import XML_Reader

global driver
def invoke():

    try:
        DesiredCapabilies={}

        DesiredCapabilies["deviceName"]= XML_Reader.Element('Capabilities', 'dvc_name')
        DesiredCapabilies["platformName"]= XML_Reader.Element('Capabilities', 'ptf_name')
        DesiredCapabilies["platformVersion"]= XML_Reader.Element('Capabilities', 'ptf_vsn')
        DesiredCapabilies["appActivity"]= XML_Reader.Element('Capabilities', 'app_actvty')
        DesiredCapabilies["appPackage"]= XML_Reader.Element('Capabilities', 'app_pckg')
        global driver
        driver=webdriver.Remote('http://localhost:4723/wd/hub',DesiredCapabilies)
        driver.implicitly_wait(5)
        return True
    except Exception as e:
        print("Error:"+str(e))
        return False