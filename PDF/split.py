'''
Objetivo: Este script percorre todos os arquivos PDF da pasta atual e separa
cada uma de suas páginas em arquivos PDF individuais.

Funcionamento:
    A função separar_paginas_pdf lê cada página de um PDF e cria um novo arquivo
    para cada uma delas.

    A função processar_pdfs_na_pasta busca todos os arquivos PDF na pasta atual
    e aplica a função de separação para cada um.

'''

import PyPDF2  # Biblioteca para manipulação de arquivos PDF.
import os  # Biblioteca para interagir com o sistema operacional.

def separar_paginas_pdf(nome_arquivo):
    """
    Função que separa cada página de um arquivo PDF em arquivos PDF individuais.
    """
    # Abrir o arquivo PDF em modo leitura binária.
    arquivo_pdf = open(nome_arquivo, 'rb')

    # Criar um objeto PdfReader para ler o conteúdo do PDF.
    leitor_pdf = PyPDF2.PdfReader(arquivo_pdf)

    # Obter o número total de páginas no PDF.
    total_paginas = len(leitor_pdf.pages)

    # Iterar por cada página do PDF.
    for numero_pagina in range(total_paginas):
        # Criar um objeto PdfWriter para escrever uma nova página.
        escritor_pdf = PyPDF2.PdfWriter()

        # Obter a página atual do PDF.
        pagina_atual = leitor_pdf.pages[numero_pagina]

        # Adicionar a página atual ao escritor.
        escritor_pdf.add_page(pagina_atual)

        # Definir o nome do novo arquivo PDF para a página separada.
        nome_novo_arquivo = f'pagina_{numero_pagina + 1}.pdf'

        # Criar e abrir o novo arquivo PDF em modo escrita binária.
        with open(nome_novo_arquivo, 'wb') as novo_arquivo:
            # Escrever a página atual no novo arquivo.
            escritor_pdf.write(novo_arquivo)

    # Fechar o arquivo PDF original.
    arquivo_pdf.close()

def processar_pdfs_na_pasta():
    """
    Função que percorre todos os arquivos da pasta atual e separa as páginas dos PDFs
    encontrados.
    """
    # Obtém o diretório atual.
    pasta_atual = os.getcwd()

    # Itera sobre todos os arquivos na pasta atual.
    for arquivo in os.listdir(pasta_atual):
        # Verifica se o arquivo tem a extensão .pdf.
        if arquivo.endswith('.pdf'):
            # Obtém o caminho completo do arquivo.
            caminho_completo = os.path.join(pasta_atual, arquivo)
            # Chama a função para separar as páginas do PDF.
            separar_paginas_pdf(caminho_completo)

# Exemplo de uso: Processar os PDFs na pasta atual.
processar_pdfs_na_pasta()
