#pip install pyautogui
#pip install pyperclip

import pyautogui
import pyperclip
import time
import webbrowser

destinatario = "gohanxd571@gmail.com"

asunto = "Curriculum - Ingeniero en Informática | Andres Ramirez"

cuerpo = """Estimados responsables de selección:

Reciban un cordial saludo. Les escribo con mucha motivación para presentarles mi perfil profesional. Soy Ingeniero en Informática recién titulado y, me encantaría tener la oportunidad de integrarme a su equipo de tecnología.

Durante mi formación, me he enfocado en construir una base técnica sólida y desarrollar una gran capacidad para resolver problemas. Más allá de mis conocimientos académicos, tengo muchísimas ganas de aprender de profesionales con experiencia, aportar mi energía y comprometerme con los proyectos y objetivos que tengan en marcha.

Adjunto mi currículum para que puedan conocer los lenguajes y herramientas con los que he trabajado durante mi carrera. Quedo a su entera disposición para conversar en una entrevista y que puedan conocer mis aptitudes de cerca.

Agradeciendo de antemano su atención y el tiempo dedicado a leer mi propuesta.

Atentamente,
Ing. Andres Ramirez
San Francisco, Edo. Zulia
"""

webbrowser.open("https://mail.google.com/")

time.sleep(3)

#pyautogui.PAUSE = 3

pyautogui.click(100, 176)
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyperclip.copy(asunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")
pyperclip.copy(cuerpo)
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")
pyautogui.hotkey("ctrl", "w")
