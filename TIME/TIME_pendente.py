"""
TIME_pendente_0.py - Relatório de Faltantes

Este script analisa profissionais faltantes em um período específico, comparando dados de presença
(planilha 'Times') com o cadastro de profissionais ativos e produtivos (planilha 'Pessoas').

Funcionalidades principais:
- Identifica profissionais ativos e produtivos
- Verifica presença em datas específicas
- Gera relatórios por período com estatísticas
- Interface interativa para solicitação de datas

Uso:
Execute o script diretamente e siga as instruções para informar o período desejado.
"""

import pandas as pd
from datetime import datetime

def obter_iddvs_ativos_produtivos(file_path, sheet_name='Pessoas'):
    """
    Obtém lista de IDs de profissionais que estão ativos E produtivos.
    
    Args:
        file_path (str): Caminho completo do arquivo Excel
        sheet_name (str, optional): Nome da planilha a ser lida. Defaults to 'Pessoas'.
    
    Returns:
        list: Lista de IDs (IDDV) dos profissionais ativos e produtivos
    
    Processo:
        1. Lê a planilha especificada
        2. Filtra registros onde 'Ativo' = 1.0 e 'Produtivo' = 1.0
        3. Retorna lista dos IDs encontrados
    """
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    df.columns = df.columns.str.strip()  # Remove espaços em branco dos nomes das colunas
    
    # Filtra por ativos e produtivos, remove valores nulos e converte para lista
    lista_iddv = df[(df['Ativo'] == 1.0) & (df['Produtivo'] == 1.0)]['IDDV'].dropna().tolist()
    
    return lista_iddv

def obter_produtivos_faltantes(file_path, data_consulta, formato_data='%Y-%m-%d'):
    """
    Identifica profissionais produtivos que não registraram presença em uma data específica.
    
    Args:
        file_path (str): Caminho do arquivo Excel
        data_consulta (str/datetime.date): Data para consulta (string ou objeto date)
        formato_data (str, optional): Formato da data se for string. Defaults to '%Y-%m-%d'.
    
    Returns:
        dict: Dicionário com:
            - data_consulta: Data analisada
            - total_produtivos: Total de ativos+produtivos
            - presentes: Lista de IDs presentes
            - faltantes: Lista de IDs faltantes
            - contagens totais
            - erro (opcional): Mensagem de erro se ocorrer
    
    Processo:
        1. Obtém lista de ativos+produtivos
        2. Busca registros de presença na data especificada
        3. Compara listas para identificar faltantes
    """
    try:
        # Converte string para objeto date se necessário
        if isinstance(data_consulta, str):
            data_consulta = datetime.strptime(data_consulta, formato_data).date()
        
        # 1. Obtém profissionais ativos e produtivos
        df_pessoas = pd.read_excel(file_path, sheet_name='Pessoas')
        df_pessoas.columns = df_pessoas.columns.str.strip()
        
        iddvs_ativos_produtivos = df_pessoas[
            (df_pessoas['Ativo'] == 1.0) & 
            (df_pessoas['Produtivo'] == 1.0)
        ]['IDDV'].dropna().tolist()
        
        # 2. Obtém presentes na data especificada
        df_times = pd.read_excel(file_path, sheet_name='Times')
        df_times.columns = df_times.columns.str.strip()
        
        # Converte e filtra por data
        df_times['Data Time'] = pd.to_datetime(df_times['Data Time']).dt.date
        df_data_filtrada = df_times[df_times['Data Time'] == data_consulta]
        iddvs_presentes = df_data_filtrada['IDProdutivo'].dropna().tolist()
        
        # 3. Identifica faltantes (ativos+produtivos não presentes)
        iddvs_faltantes = [iddv for iddv in iddvs_ativos_produtivos if iddv not in iddvs_presentes]
        
        return {
            'data_consulta': data_consulta,
            'total_produtivos': len(iddvs_ativos_produtivos),
            'presentes': iddvs_presentes,
            'faltantes': iddvs_faltantes,
            'total_presentes': len(iddvs_presentes),
            'total_faltantes': len(iddvs_faltantes)
        }
        
    except Exception as e:
        print(f"Erro: {str(e)}")
        return {
            'data_consulta': data_consulta,
            'total_produtivos': 0,
            'presentes': [],
            'faltantes': [],
            'total_presentes': 0,
            'total_faltantes': 0,
            'erro': str(e)
        }

def obter_faltantes_periodo(file_path, data_inicio, data_fim):
    """
    Gera relatório de faltantes para um intervalo de datas.
    
    Args:
        file_path (str): Caminho do arquivo Excel
        data_inicio (str): Data inicial no formato 'YYYY-MM-DD'
        data_fim (str): Data final no formato 'YYYY-MM-DD'
    
    Returns:
        dict: Dicionário com relatório por data, onde cada entrada contém:
            - Mesma estrutura retornada por obter_produtivos_faltantes()
    """
    try:
        # Converte strings para objetos date
        data_inicio = datetime.strptime(data_inicio, '%Y-%m-%d').date()
        data_fim = datetime.strptime(data_fim, '%Y-%m-%d').date()
        
        relatorio = {}
        data_atual = data_inicio
        
        # Processa cada dia do período
        while data_atual <= data_fim:
            resultado = obter_produtivos_faltantes(file_path, data_atual.strftime('%Y-%m-%d'))
            relatorio[data_atual.strftime('%Y-%m-%d')] = resultado
            data_atual += pd.Timedelta(days=1)  # Avança um dia
        
        return relatorio
        
    except Exception as e:
        print(f"Erro: {str(e)}")
        return {}

def validar_data(data_str):
    """
    Valida se uma string está no formato de data YYYY-MM-DD.
    
    Args:
        data_str (str): String contendo a data
    
    Returns:
        bool: True se válida, False caso contrário
    """
    try:
        datetime.strptime(data_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def solicitar_datas():
    """
    Solicita datas inicial e final ao usuário com validação.
    
    Returns:
        tuple: (data_inicio, data_fim) como strings válidas
    
    Processo:
        - Solicita datas até receber entradas válidas
        - Garante que data final >= data inicial
    """
    print("=== RELATÓRIO DE FALTANTES POR PERÍODO ===")
    print("Digite as datas no formato: YYYY-MM-DD (exemplo: 2025-01-15)")
    
    # Solicita data inicial com validação
    while True:
        data_inicio = input("\nDigite a data INICIAL: ").strip()
        if validar_data(data_inicio):
            break
        else:
            print("❌ Data inválida! Use o formato YYYY-MM-DD (exemplo: 2025-01-15)")
    
    # Solicita data final com validação adicional
    while True:
        data_fim = input("Digite a data FINAL: ").strip()
        if validar_data(data_fim):
            if datetime.strptime(data_fim, '%Y-%m-%d') >= datetime.strptime(data_inicio, '%Y-%m-%d'):
                break
            else:
                print("❌ A data final deve ser maior ou igual à data inicial!")
        else:
            print("❌ Data inválida! Use o formato YYYY-MM-DD (exemplo: 2025-01-15)")
    
    return data_inicio, data_fim

def gerar_relatorio_interativo():
    """
    Função principal que executa o relatório de forma interativa.
    
    Fluxo:
        1. Solicita período ao usuário
        2. Processa os dados
        3. Exibe resumo
        4. Oferece opção de detalhamento
    """
    # Caminho fixo do arquivo de dados
    file_path = r"V:\PCP\TIME\time.xlsx"
    
    try:
        # 1. Solicita datas ao usuário
        data_inicio, data_fim = solicitar_datas()
        
        print(f"\n🔄 Processando período de {data_inicio} até {data_fim}...")
        
        # 2. Obtém relatório do período
        relatorio_periodo = obter_faltantes_periodo(file_path, data_inicio, data_fim)
        
        # 3. Exibe cabeçalho do relatório
        print(f"\n{'='*60}")
        print(f"📊 RELATÓRIO DE FALTANTES - {data_inicio} a {data_fim}")
        print(f"{'='*60}")
        
        # Calcula estatísticas
        total_dias = len(relatorio_periodo)
        dias_com_faltantes = 0
        
        # Exibe status por dia
        for data, resultado in relatorio_periodo.items():
            if 'erro' not in resultado:
                status = "✅" if resultado['total_faltantes'] == 0 else "⚠️"
                print(f"{status} {data}: {resultado['total_faltantes']} faltantes de {resultado['total_produtivos']} produtivos")
                if resultado['total_faltantes'] > 0:
                    dias_com_faltantes += 1
            else:
                print(f"❌ {data}: ERRO - {resultado['erro']}")
        
        # 4. Exibe resumo consolidado
        print(f"\n{'='*40}")
        print(f"📈 RESUMO DO PERÍODO:")
        print(f"   Total de dias analisados: {total_dias}")
        print(f"   Dias com faltantes: {dias_com_faltantes}")
        print(f"   Dias sem faltantes: {total_dias - dias_com_faltantes}")
        
        # 5. Oferece detalhamento se houver faltantes
        if dias_com_faltantes > 0:
            ver_detalhes = input(f"\n❓ Deseja ver os detalhes dos faltantes? (s/n): ").strip().lower()
            if ver_detalhes in ['s', 'sim', 'yes', 'y']:
                print(f"\n{'='*50}")
                print("📋 DETALHES DOS FALTANTES:")
                print(f"{'='*50}")
                
                for data, resultado in relatorio_periodo.items():
                    if 'erro' not in resultado and resultado['total_faltantes'] > 0:
                        print(f"\n📅 {data}:")
                        print(f"   Faltantes ({resultado['total_faltantes']}): {resultado['faltantes']}")
        
    except KeyboardInterrupt:
        print("\n\n⏹️ Operação cancelada pelo usuário.")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {str(e)}")

# Ponto de entrada principal
if __name__ == "__main__":
    gerar_relatorio_interativo()