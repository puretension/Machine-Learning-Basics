import time
import pyautogui
import pyperclip

# 1. 

# 2. 키보드 입력(키)
pyautogui.press('enter')
pyautogui.press('up')

# 3. 키보드 입력(여러개 동시에)
pyautogui.hotkey('ctrl', 'c')

# 4. 한글 입력 방법
pyperclip.copy('크롤링')
pyautogui.hotkey('ctrl', 'v') # mac은 cmd