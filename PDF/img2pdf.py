import os
from PIL import Image

def converter_imagens_para_pdf():
    # Obtém a pasta atual do script
    pasta_atual = os.getcwd()

    # Itera sobre todos os arquivos na pasta atual
    for arquivo in os.listdir(pasta_atual):
        # Verifica se o arquivo é uma imagem (JPEG, PNG, etc.)
        if arquivo.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff')):
            nome_pdf = os.path.splitext(arquivo)[0] + '.pdf'  # Define o nome do PDF
            
            try:
                # Abre a imagem e converte para RGB (para evitar problemas com PNG/transparência)
                imagem = Image.open(arquivo).convert('RGB')
                # Salva a imagem como PDF
                imagem.save(nome_pdf, 'PDF', resolution=100.0)
                print(f'{arquivo} -> {nome_pdf} convertido com sucesso!')
            except Exception as e:
                print(f'Erro ao converter {arquivo}: {e}')

if __name__ == "__main__":
    converter_imagens_para_pdf()
