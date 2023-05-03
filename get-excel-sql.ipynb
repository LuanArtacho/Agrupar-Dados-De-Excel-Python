import pandas as pd
import sqlite3
from pandasql import sqldf

# Leitura dos arquivos excel
fotografia_Funded = pd.read_excel(r'C:\Users\luanzera\Desktop\Estudos\Taks BBA - Comparando arquivos\Arquivos p Comparar\Fotografia\Fotografia Operacoes Funded.xlsx')
Base_Unificada = pd.read_excel(r'C:\Users\luanzera\Desktop\Estudos\Taks BBA - Comparando arquivos\Arquivos p Comparar\BaseUnificada\BaseUnificada.xlsx')

# Dicionário com as colunas correspondentes
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

# Criar conexão com o banco de dados em memória
conn = sqlite3.connect(':memory:')

# Definir a consulta SQL
with conn:
    # Criar a tabela fotografia_Funded
    fotografia_Funded.to_sql('fotografia_Funded', conn, if_exists='replace', index=False)
    # Adicionar a coluna Amount_USD
    conn.execute("ALTER TABLE fotografia_Funded ADD COLUMN Amount_USD FLOAT;")
    # Criar a tabela Base_Unificada
    Base_Unificada.to_sql('Base_Unificada', conn, if_exists='replace', index=False)
    # Executar a consulta SQL
    query = """
        SELECT *
        FROM fotografia_Funded
        LEFT OUTER JOIN Base_Unificada
        ON fotografia_Funded.BANCO = Base_Unificada.BANCO
        AND fotografia_Funded.Unidade = Base_Unificada.PAIS_UNIDADE
        AND fotografia_Funded.`Bank/City Lender` = Base_Unificada.BANK_CITY_LENDER
        AND fotografia_Funded.CCY = Base_Unificada.CCY
        AND fotografia_Funded.Amount = Base_Unificada.AMOUNT_RECEIVED
        AND fotografia_Funded.Amount_USD = Base_Unificada.AMOUNT_USD
        AND fotografia_Funded.`Transaction Type` = Base_Unificada.`TRANSACTION`
        AND fotografia_Funded.`Deal Date` = Base_Unificada.DEAL_DATE
        AND fotografia_Funded.`Value Date` = Base_Unificada.VALUE_DATE
        AND fotografia_Funded.Maturity = Base_Unificada.MATURITY
        WHERE Base_Unificada.BANCO IS NULL
        """

    resultado = pd.read_sql_query(query, conn)
