import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def main():
    """
    Script para importar um arquivo Excel com atividades produtivas,
    filtrar por um IDProdutivo informado pelo usuário, somar as horas
    diárias agrupadas por PE/Equipamento, e exibir os resultados
    alinhando os decimais na saída de texto. Também permite customizar
    o filtro via input.

    Requer:
        - pandas
        - numpy
        - matplotlib (opcional, só é usado se quiser gerar gráficos)

    Autor: Seu nome
    Data: 2025-07-16
    """

    # Caminho do arquivo Excel
    file_path = r"V:\PCP\TIME\time.xlsx"

    # Leitura da planilha e limpeza dos nomes das colunas
    df = pd.read_excel(file_path, sheet_name='Times')
    df.columns = df.columns.str.strip()

    # Função para limpar strings (remove espaços extras)
    def clean_string(s):
        try:
            return str(s).strip()
        except Exception:
            return s

    # Limpar e preparar as colunas de texto e datas
    df['PE/Equip'] = df['PE/Equip'].apply(clean_string)
    df['IDProdutivo'] = df['IDProdutivo'].apply(clean_string)
    df['Data Time'] = pd.to_datetime(df['Data Time'], errors='coerce')

    # Renomear coluna de horas lançadas para 'Horas' para facilitar manipulação
    df.rename(columns={'Hora lançada': 'Horas'}, inplace=True)

    # Solicitar ao usuário o IDProdutivo a ser filtrado
    id_filtrado = input("Informe o IDProdutivo desejado: ").strip()

    # Filtrar DataFrame pelo IDProdutivo informado
    df_filtrado = df[df['IDProdutivo'] == id_filtrado]

    # Agrupar pelo PE/Equip e somar as horas
    horas_por_item = df_filtrado.groupby('PE/Equip')['Horas'].sum().reset_index()

    # Calcular o total geral de horas
    total_horas = horas_por_item['Horas'].sum()

    # Determina o tamanho do maior código para alinhar corretamente
    tamanho_codigo = max(horas_por_item['PE/Equip'].astype(str).apply(len).max(), 6) + 2

    # Exibir resultados alinhando os decimais
    print(f"\nIDProdutivo: {id_filtrado}")
    for _, row in horas_por_item.iterrows():
        codigo_formatado = f"{row['PE/Equip']}:".ljust(tamanho_codigo)
        horas_formatadas = f"{row['Horas']:>7.2f}"
        print(f"{codigo_formatado}{horas_formatadas}")

    print(f"{'TOTAL:'.ljust(tamanho_codigo)}{total_horas:>7.2f}")

if __name__ == "__main__":
    main()
