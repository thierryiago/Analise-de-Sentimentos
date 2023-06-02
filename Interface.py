import time

import PySimpleGUI as sg


def interfaceFrases():
    sentences = []
    layout = [
        [sg.Text("Adicione suas frases para análise")],
        [sg.InputText(key="frase")],
        [sg.Button("Adicionar"), sg.Button("Sair")],
        [sg.Text("", key="frase_adicionada")],
    ]

    janela = sg.Window("Análise de Sentimentos", layout)

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED or evento == "Sair":
            break
        if evento == "Adicionar":
            frases = valores["frase"]
            sentences.append(frases)
            janela["frase_adicionada"].update(f"Frase adicionada com sucesso")
            janela["frase"].update(f"")

    janela.close()

    return sentences

def interfaceIdioma():
    idioma = ""
    layout = [
        [sg.Text("Digite o idioma de sua preferência: ")],
        [sg.InputText(key="idioma")],
        [sg.Button("Salvar"), sg.Button("Sair")],
        [sg.Text("", key="idioma")],
    ]

    janela = sg.Window("Análise de Sentimentos", layout)

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED or evento == "Sair":
            break
        if evento == "Salvar":
            idioma = valores["idioma"]
            break

    janela.close()

    return idioma


def interfaceNula():
    sg.popup("Lista de frases está vazia! Execute novamente e adicione frases.")
