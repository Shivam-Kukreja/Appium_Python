from Base import Driver
from BusineesLogic import Display
from BusineesLogic import Animation
import pytest

@pytest.mark.first
def test_launch():
    assert Driver.invoke()==True
@pytest.mark.second
def test_verify_hide_functionality():
    assert Animation.animation_hidetest()==True
@pytest.mark.third
def test_verify_show_functionality():
    assert Animation.animation_showtest()==True
@pytest.mark.last
def test_verify_showtitle_functionality():
    assert Display.Display_Options()==True