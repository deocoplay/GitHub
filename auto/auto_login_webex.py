import pyautogui
from time import sleep  # , time
# import keyboard

sleep(2)
pyautogui.PAUSE = 1
# 比對所有圖片，取得顯示在桌面的圖片物件 (pillow / PIL Image)
pyautogui_webexdesktop_location = pyautogui.locateOnScreen(
    './images/webex_desktop.png', confidence=0.9)
btn_webexdesktop_point = pyautogui.center(pyautogui_webexdesktop_location)
pyautogui.doubleClick(btn_webexdesktop_point.x, btn_webexdesktop_point.y)

sleep(1)

pyautogui_webextomeet_location = pyautogui.locateOnScreen(
    './images/webex_to_meet.png', confidence=0.9)
btn_webextomeet_point = pyautogui.center(pyautogui_webextomeet_location)
pyautogui.click(btn_webextomeet_point.x, btn_webextomeet_point.y)

pyautogui.hotkey('ctrl', 'space')
pyautogui.write('room number', interval=0.1)
pyautogui.typewrite(['tab', 'tab'])

pyautogui.hotkey('ctrl', 'space')
pyautogui.typewrite('name', interval=0.1)
pyautogui.typewrite(['enter'])
pyautogui.typewrite(['tab', 'tab'])

pyautogui.hotkey('ctrl', 'space')
pyautogui.typewrite('e-mail', interval=0.1)
pyautogui.typewrite(['tab', 'tab'])
pyautogui.typewrite(['enter'])

sleep(5)

# pyautogui_webexguest_location = pyautogui.locateOnScreen('./images/webex_guest.png', confidence=0.8)
# btn_webexguest_point= pyautogui.center(pyautogui_webexguest_location)
# pyautogui.click(btn_webextoguest_point.x, btn_webexguest_point.y)
pyautogui.typewrite(['tab', 'tab', 'tab'])
pyautogui.typewrite(['enter'])

pyautogui.typewrite('password', interval=0.1)
pyautogui.typewrite(['tab', 'tab'])
pyautogui.typewrite(['enter'])

sleep(3)

pyautogui_webexjoinmeet_location = pyautogui.locateOnScreen(
    './images/webex_join_meet.png', confidence=0.9)
btn_webexjoinmeet_point = pyautogui.center(pyautogui_webexjoinmeet_location)
pyautogui.click(btn_webexjoinmeet_point.x, btn_webexjoinmeet_point.y)
