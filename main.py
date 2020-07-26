"""
Esse bot funciona assim, voce seta oque quer mandar no arquivo texto
dai voce inicia o programa e ao apertar enter,
ele ira mandar oque tem escrito no arquivo texto
"""
import pyautogui, time
time.sleep(5)
t = open("texto", 'r')
for palavras in t:
    pyautogui.typewrite(palavras)
    pyautogui.press("enter")
