import pyautogui
import time
import pyperclip
import pytesseract
from pytesseract import Output
import json
import locale
from datetime import datetime

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

contatos_encontrados = []
contatos_nao_encontrados = []

def carregar_debitos(caminho_arquivo):
    with open(caminho_arquivo, 'r') as file:
        return json.load(file)

def verificar_contato_na_lista(nome_formatado):
    try:
        time.sleep(2)
        # Coordenadas originais
        x, y, largura, altura = 760, 100, 527, 350

        # Para descer mais a captura, aumente o valor de 'y'
        y_novo = y + 90  # Isso descerá a captura em 50 pixels

        # Você também pode querer ajustar a altura se precisar de uma região maior ou menor
        altura_nova = altura + 1  # Isso aumentará a altura da captura em 50 pixels

        # Captura com as novas coordenadas
        captura = pyautogui.screenshot(region=(x, y_novo, largura, altura_nova))

        texto = pytesseract.image_to_string(captura, lang='por')

        return nome_formatado in texto
    except Exception as e:
        print(f"Erro ao verificar o contato {nome_formatado}: {e}")
        return False

def carregar_mensagem(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as file:
        return file.read()

def enviar_mensagem_no_teams(nome, nome_formatado, debito):
    global contatos_encontrados, contatos_nao_encontrados
    try:
        time.sleep(5)
        mes_atual = "dezembro"
        template_mensagem = carregar_mensagem('mensagem.txt')
        mensagem = template_mensagem.format(nome=nome, mes_atual=mes_atual, debito=debito)

        pyautogui.click(x=910, y=123)
        pyautogui.write(nome_formatado)

        if verificar_contato_na_lista(nome_formatado):
            pyautogui.click(x=957, y=232)
            time.sleep(1)

            pyautogui.click(x=1147, y=969)
            time.sleep(1)

            pyautogui.press('delete')
            pyperclip.copy(mensagem)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')

            pyautogui.click(x=910, y=123)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')

            print(f"Mensagem enviada com sucesso para {nome}.")
            contatos_encontrados.append(nome_formatado)
        else:
            print(f"Contato {nome_formatado} não encontrado na lista.")
            pyautogui.click(x=910, y=123)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
            contatos_nao_encontrados.append(nome_formatado)

    except Exception as e:
        print(f"Erro ao enviar mensagem para {nome_formatado}: {e}")

def main():
    caminho_arquivo = 'D:\\PROJETOS\\AutomatizacaoBebidas\\debitos.json'
    nomes_e_debitos = carregar_debitos(caminho_arquivo)

    for item in nomes_e_debitos:
        enviar_mensagem_no_teams(item['nome'], item['nome_formatado'], item['debito'])

    print("\nRelatório de Envio de Mensagens:")
    print("Contatos Encontrados e Mensagens Enviadas:")
    for contato in contatos_encontrados:
        print(contato)

    print("\nContatos Não Encontrados:")
    for contato in contatos_nao_encontrados:
        print(contato)

    with open('relatorio_contatos.txt', 'w') as file:
        file.write("Contatos Encontrados e Mensagens Enviadas:\n")
        file.write('\n'.join(contatos_encontrados))
        file.write("\n\nContatos Não Encontrados:\n")
        file.write('\n'.join(contatos_nao_encontrados))

if __name__ == "__main__":
    main()
