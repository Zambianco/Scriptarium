import PyPDF2

def dividir_pdf_rodar_pagina(input_pdf):
    with open(input_pdf, 'rb') as arquivo:
        leitor = PyPDF2.PdfReader(arquivo)
        total_paginas = len(leitor.pages)

        # Processa a cada duas páginas
        for i in range(0, total_paginas, 2):
            escritor = PyPDF2.PdfWriter()

            # Primeira página - Rotaciona para paisagem (90°)
            pagina1 = leitor.pages[i]
            pagina1.rotate(0)
            escritor.add_page(pagina1)

            # Segunda página - Rotaciona para paisagem + 180° (inverso)
            if i + 1 < total_paginas:
                pagina2 = leitor.pages[i + 1]
                pagina2.rotate(0)  # Coloca em paisagem
                pagina2.rotate(0)  # Inverte o conteúdo
                escritor.add_page(pagina2)

            # Salva o novo PDF
            nome_arquivo = f'saida_{i // 2 + 1}.pdf'
            with open(nome_arquivo, 'wb') as novo_pdf:
                escritor.write(novo_pdf)
                print(f'{nome_arquivo} criado com sucesso.')

# Exemplo de uso
dividir_pdf_rodar_pagina('seu_arquivo.pdf')
