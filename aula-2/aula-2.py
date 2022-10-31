# Análise de Dados com Python

# Passo 1: Importar a base de dados

# Passo 2: Visualizar a base de dados
#          Entender as informações que você tem disponível
#          Descobrir as cagadas da base de dados

# Passo 3: Tratamento dos dados

# Passo 4: Análise inicial dos dados

# Passo 5: Descobrir os motivos do cancelamento

import pandas as pd
import plotly.express as px

tabela = pd.read_csv(r"C:\Users\Arthur\Desktop\Códigos\Teste\aula-2\telecom_users.csv")

# excluir coluna inútil
# axis = 0 -> eixo x
# axis = 1 -> eixo y
tabela = tabela.drop("Unnamed: 0", axis=1)

tabela["TotalGasto"] = pd.to_numeric(tabela["TotalGasto"], errors="coerce") # força a alteração de tipo de dado
tabela = tabela.dropna(how="all", axis=1) # excluir qualquer coluna completamente vazia
tabela = tabela.dropna(how="any", axis=0) # excluir qualquer linha com inforamação vazia

# print(tabela["Churn"].value_counts())
# print(tabela["Churn"].value_counts(normalize=True))

# criar um gráfico
grafico = px.histogram(tabela, x="MesesComoCliente", color="Churn", barmode="group")
grafico.show()
