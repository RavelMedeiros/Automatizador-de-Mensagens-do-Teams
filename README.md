# Automatizador de Mensagens do Teams

![Banner](https://www.empowerit.com.au/wp-content/uploads/2017/06/Microsoft-Teams-750x290.png)

## :sparkles: Descrição
Este repositório contém um script em Python projetado para automatizar o envio de mensagens personalizadas no Microsoft Teams. Ideal para gestores e equipes que necessitam comunicar-se regularmente com um grande número de contatos, como enviar lembretes de débitos ou avisos importantes. O script utiliza bibliotecas como `pyautogui`, `pytesseract`, e `pyperclip` para interagir com a interface gráfica, reconhecer texto em imagens e manipular a área de transferência, respectivamente.

## :toolbox: Recursos
- **Automatização de Interface Gráfica**: Envia mensagens automaticamente através da interface do Teams.
- **Reconhecimento Óptico de Caracteres**: Identifica contatos na lista do Teams usando OCR.
- **Relatórios de Envio**: Gera relatórios listando contatos que receberam a mensagem e aqueles não encontrados.
- **Personalização de Mensagens**: Permite enviar mensagens personalizadas com base em dados de um arquivo JSON.

## :computer: Pré-Requisitos
- Python 3.x
- Bibliotecas: `pyautogui`, `pytesseract`, `pyperclip`, `time`, `json`, `locale`
- Tesseract OCR instalado no seu sistema

## :wrench: Instalação
1. Clone o repositório: git clone https://github.com/RavelMedeiros/Automatizador-de-Mensagens-do-Teams
2. Instale as dependências: pip install pyautogui pytesseract pyperclip

## :gear: Configuração
- Certifique-se de ajustar as coordenadas de clique e captura de tela conforme a resolução e layout do seu sistema.
- Defina o caminho correto para o executável do Tesseract OCR em seu script.

## :rocket: Uso
1. Prepare seu arquivo JSON com os dados dos contatos e débitos.
2. Execute o script: python index.py
3. Verifique o arquivo `relatorio_contatos.txt` após a execução para ver o resultado do envio das mensagens.

## :warning: Aviso
Este script foi desenvolvido para fins educacionais e de automação de tarefas administrativas. Sempre respeite os termos de serviço e políticas de uso do Microsoft Teams.

## :handshake: Contribuições
Contribuições, sugestões e melhorias são bem-vindas! Por favor, sinta-se à vontade para forkar o repositório e enviar pull requests.

## :page_facing_up: Licença
Este projeto está sob a licença MIT, o que permite uso, distribuição e modificação sob certos termos.

