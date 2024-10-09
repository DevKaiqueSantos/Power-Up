

import pandas
import time
import pyautogui

pyautogui.PAUSE = 0.5


pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)


pyautogui.click(x=835, y=459)

pyautogui.write("kaique.dsosantos@gmail.com")
pyautogui.press("tab")
pyautogui.write("minha senha")
pyautogui.click(x=964, y=666)
time.sleep(3)


tabela = pandas.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index:
    pyautogui.click(x=729, y=317)

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # OBS
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    # clicar botao enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)
