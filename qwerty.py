import keyboard, pyautogui, time, pyperclip

print("Ile raz?")
kol_vo = int(input(">>>>  "))

pyautogui.click(x=319, y=1060)
time.sleep(3)
x = 466
pos = pyautogui.position()
y = pos.y

for click in range(kol_vo):
    y = y+20
    pyautogui.click(x, y)
    time.sleep(3)
    pyautogui.click(button='middle', x=885, y=933)

time.sleep(1)
site_x = 207
site_y = 15

for click in range(1, kol_vo+1):
    site_x = site_x+240
    pyautogui.click(site_x, site_y)
    time.sleep(0.5)
    keyboard.press_and_release("ctrl + a")
    time.sleep(0.2)
    keyboard.press_and_release("ctrl + c")
    time.sleep(1)
    f = open("Words.txt", "a", encoding='utf-8')
    f.write(pyperclip.paste())
    f.close()
    time.sleep(1)


