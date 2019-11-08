
def press(Element):
    Element.click()

def isDisplayed(Element):
    if Element !=None:
        Flag=Element.isDisplayed();
    if Flag==True:
        return True
    else:
        return False