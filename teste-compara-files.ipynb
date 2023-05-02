import pandas as pd
from pandasql import sqldf

# Leitura dos arquivos excel
fotografia_Funded = pd.read_excel(r'C:\Users\luanzera\Desktop\Estudos\Taks BBA - Comparando arquivos\Arquivos p Comparar\Fotografia\Fotografia Operacoes Funded.xlsx')
Base_Unificada = pd.read_excel(r'C:\Users\luanzera\Desktop\Estudos\Taks BBA - Comparando arquivos\Arquivos p Comparar\BaseUnificada\BaseUnificada.xlsx')

# Dicionário com as colunas correspondentes
#      BaseUnifi / Fotografia Unfd
colunas = {
        'BANCO': 'BANCO',
        'PAIS_UNIDADE': 'Unidade',
        'BANK_CITY_LENDER': 'Bank/City Lender', 
        'CCY': 'CCY',
        'AMOUNT_RECEIVED': 'Amount',
        'AMOUNT_USD': 'Amount_USD', 
        'TRANSACTION': 'Transaction Type',
        'DEAL_DATE': 'Deal Date',
        'VALUE_DATE': 'Value Date', 
        'MATURITY': 'Maturity'
        }


# Renomeia as colunas do arquivo Fotografia
fotografia_Funded.rename(columns=colunas, inplace=True)

# Renomeando as colunas do arquivo A para as colunas do arquivo B
fotografia_Funded = fotografia_Funded.rename(columns=colunas)

# Join utilizando SQL para comparar as colunas LEFT
query = """
        SELECT *
        FROM fotografia_Funded
        LEFT OUTER JOIN Base_Unificada
        ON fotografia_Funded.BANCO = Base_Unificada.BANCO
        AND fotografia_Funded.Unidade = Base_Unificada.PAIS_UNIDADE
        AND fotografia_Funded.coluna_b_3 = Base_Unificada.coluna_b_3
        AND fotografia_Funded.coluna_b_4 = Base_Unificada.coluna_b_4
        AND fotografia_Funded.coluna_b_5 = Base_Unificada.coluna_b_5
        WHERE Base_Unificada.BANCO IS NULL
        """
dados_left = sqldf(query)

# Join utilizando SQL para comparar as colunas RIGHT
query = """
        SELECT *
        FROM fotografia_Funded
        RIGHT OUTER JOIN Base_Unificada
        ON fotografia_Funded.BANCO = Base_Unificada.BANCO
        AND fotografia_Funded.Unidade = Base_Unificada.PAIS_UNIDADE
        AND fotografia_Funded.coluna_b_3 = Base_Unificada.coluna_b_3
        AND fotografia_Funded.coluna_b_4 = Base_Unificada.coluna_b_4
        AND fotografia_Funded.coluna_b_5 = Base_Unificada.coluna_b_5
        WHERE fotografia_Funded.BANCO IS NULL
        """
dados_right = sqldf(query)

# Join utilizando SQL para comparar as colunas INNER
query = """
        SELECT *
        FROM fotografia_Funded
        INNER JOIN Base_Unificada
        ON fotografia_Funded.BANCO = Base_Unificada.BANCO
        AND fotografia_Funded.Unidade = Base_Unificada.PAIS_UNIDADE
        AND fotografia_Funded.coluna_b_3 = Base_Unificada.coluna_b_3
        AND fotografia_Funded.coluna_b_4 = Base_Unificada.coluna_b_4
        AND fotografia_Funded.coluna_b_5 = Base_Unificada.coluna_b_5
        """
dados_comuns = sqldf(query)

# # Compara os dados dos arquivos
# dados_comuns = pd.merge(fotografia_Funded, Base_Unificada, on=list(colunas.values()), how='inner')
# dados_apenas_fotografia_Funded = pd.merge(fotografia_Funded, Base_Unificada, on=list(colunas.values()), how='left').query('Bancos_y.isnull()', engine='python')
# dados_apenas_Base_Unificada = pd.merge(fotografia_Funded, Base_Unificada, on=list(colunas.values()), how='right').query('Bancos_x.isnull()', engine='python')

# Selecionando dados exclusivos do arquivo A
dados_apenas_fotografia_Funded = pd.merge(fotografia_Funded, Base_Unificada, on=list(colunas.values()), how='left').query('coluna_b_1.isnull()', engine='python')

# Selecionando dados exclusivos do arquivo B
dados_apenas_Base_Unificada = pd.merge(fotografia_Funded, Base_Unificada, on=list(colunas.values()), how='right').query('coluna_a_1.isnull()', engine='python')

# Salva os dados em arquivos excel
with pd.ExcelWriter('Dados_comuns.xlsx') as writer:
  dados_comuns.to_excel(writer, sheet_name='Dados em comum', index=False)
    
with pd.ExcelWriter('Dados_apenas_fotografia_Funded.xlsx') as writer:
  dados_apenas_fotografia_Funded.to_excel(writer, sheet_name='Dados exclusivos do arquivo A', index=False)
    
with pd.ExcelWriter('Dados_apenas_Base_Unificada.xlsx') as writer:
  dados_apenas_Base_Unificada.to_excel(writer, sheet_name='Dados exclusivos do arquivo B', index=False)
