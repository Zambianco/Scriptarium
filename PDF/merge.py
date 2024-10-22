'''
Esse código faz a união de todos os arquivos PDF na pasta onde ele é executado,
gerando um único PDF chamado pdf_combinado.pdf
'''

import os  # Importa o módulo para interagir com o sistema operacional.
from PyPDF2 import PdfMerger  # Importa a classe para unir arquivos PDF.

# Obtém a lista de arquivos na pasta atual que terminam com ".pdf" (case insensitive).
arquivos_pdf = [arquivo for arquivo in os.listdir('.') if arquivo.lower().endswith('.pdf')]

# Verifica se há pelo menos dois arquivos PDF para unir.
if len(arquivos_pdf) < 2:
    print('Não há arquivos suficientes para unir.')  # Informa que não há PDFs suficientes.
else:
    merger = PdfMerger()  # Cria um objeto PdfMerger para gerenciar a união dos arquivos.

    # Itera sobre a lista de PDFs e adiciona cada um ao objeto merger.
    for arquivo in arquivos_pdf:
        merger.append(arquivo)  # Adiciona o arquivo ao PDF combinado.

    # Salva o PDF combinado com o nome 'pdf_combinado.pdf'.
    merger.write('pdf_combinado.pdf')  # Escreve o arquivo final.
    merger.close()  # Fecha o objeto PdfMerger para liberar recursos.

    print(f'Os arquivos PDF foram unidos com sucesso no arquivo "pdf_combinado.pdf".')  # Mensagem de sucesso.
