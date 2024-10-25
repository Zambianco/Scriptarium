import os

def renomear_pdfs():
    sufixo = "-M06-20240101-20240630.pdf"
    pasta_atual = os.getcwd()  # Obtém a pasta atual

    # Itera sobre todos os arquivos da pasta atual
    for arquivo in os.listdir(pasta_atual):
        if arquivo.endswith(".pdf"):
            nome_antigo = os.path.join(pasta_atual, arquivo)
            nome_novo = os.path.join(
                pasta_atual, arquivo.replace(".pdf", sufixo)
            )

            # Renomeia o arquivo
            os.rename(nome_antigo, nome_novo)
            print(f'{arquivo} -> {nome_novo}')

# Executa a função
renomear_pdfs()
