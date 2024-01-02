import json
import locale
import pyautogui
import pyperclip
import pytesseract
import time
from datetime import datetime
from pytesseract import Output

# Configurações do Tesseract e Localização
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

# Coordenadas e dimensões da captura de tela
COORDENADAS_CAPTURA = (760, 100, 527, 350)
AJUSTE_Y = 90
AJUSTE_ALTURA = 1

# Coordenadas de interação no Teams
COORDENADA_CLIQUE_NOME = (910, 123)
COORDENADA_CLIQUE_MENSAGEM = (957, 232)
COORDENADA_ESCRITA_MENSAGEM = (1147, 969)

def carregar_json(caminho_arquivo):
    """Carrega um arquivo JSON e retorna seu conteúdo."""
    with open(caminho_arquivo, 'r') as file:
        return json.load(file)

def verificar_contato_na_lista(nome_formatado):
    """Verifica se um contato está na lista do Teams."""
    try:
        time.sleep(2)
        x, y, largura, altura = COORDENADAS_CAPTURA
        captura = pyautogui.screenshot(region=(x, y + AJUSTE_Y, largura, altura + AJUSTE_ALTURA))
        texto = pytesseract.image_to_string(captura, lang='por')
        return nome_formatado in texto
    except Exception as e:
        print(f"Erro ao verificar o contato {nome_formatado}: {e}")
        return False

def enviar_mensagem_no_teams(nome, nome_formatado, debito, mensagem_template):
    """Envia uma mensagem no Microsoft Teams."""
    try:
        time.sleep(5)
        mes_atual = "dezembro"
        mensagem = mensagem_template.format(nome=nome, mes_atual=mes_atual, debito=debito)

        pyautogui.click(*COORDENADA_CLIQUE_NOME)
        pyautogui.write(nome_formatado)

        if verificar_contato_na_lista(nome_formatado):
            pyautogui.click(*COORDENADA_CLIQUE_MENSAGEM)
            time.sleep(1)

            pyautogui.click(*COORDENADA_ESCRITA_MENSAGEM)
            time.sleep(1)

            pyautogui.press('delete')
            pyperclip.copy(mensagem)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.press('enter')

            pyautogui.click(*COORDENADA_CLIQUE_NOME)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')

            print(f"Mensagem enviada com sucesso para {nome}.")
            return True
        else:
            print(f"Contato {nome_formatado} não encontrado na lista.")
            pyautogui.click(*COORDENADA_CLIQUE_NOME)
            pyautogui.hotkey('ctrl', 'a')
            pyautogui.press('delete')
            return False

    except Exception as e:
        print(f"Erro ao enviar mensagem para {nome_formatado}: {e}")
        return False

def main():
    caminho_arquivo_debitos = 'D:\\PROJETOS\\AutomatizacaoBebidas\\debitos.json'
    caminho_arquivo_mensagem = 'mensagem.txt'
    nomes_e_debitos = carregar_json(caminho_arquivo_debitos)
    mensagem_template = carregar_json(caminho_arquivo_mensagem)

    contatos_encontrados = []
    contatos_nao_encontrados = []

    for item in nomes_e_debitos:
        sucesso = enviar_mensagem_no_teams(item['nome'], item['nome_formatado'], item['debito'], mensagem_template)
        if sucesso:
            contatos_encontrados.append(item['nome_formatado'])
        else:
            contatos_nao_encontrados.append(item['nome_formatado'])

    # Geração de relatório
    with open('relatorio_contatos.txt', 'w') as file:
        file.write("Contatos Encontrados e Mensagens Enviadas:\n")
        file.write('\n'.join(contatos_encontrados))
        file.write("\n\nContatos Não Encontrados:\n")
        file.write('\n'.join(contatos_nao_encontrados))

if __name__ == "__main__":
    main()
