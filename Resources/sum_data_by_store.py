import pandas as pd
import os

# Lista para armazenar os DataFrames
dfs = []

# Caminho relativo CONSISTENTE
pasta_data = '../Data'  # Define o caminho base uma única vez

# Carregar todos os CSVs da pasta '../Data'
for arquivo in os.listdir(pasta_data):
    if arquivo.startswith('loja_') and arquivo.endswith('.csv'):
        caminho = os.path.join(pasta_data, arquivo)  # Usa o MESMO caminho base
        df = pd.read_csv(caminho)
        df['Loja'] = arquivo.replace('.csv', '')  
        dfs.append(df)

# Concatenar e calcular faturamento
if dfs:  # Só prossegue se encontrar arquivos
    dados_completos = pd.concat(dfs, ignore_index=True)
    faturamento = dados_completos.groupby('Loja')['Preço'].sum()
    print(faturamento)
else:
    print("Nenhum arquivo CSV encontrado em", pasta_data)
