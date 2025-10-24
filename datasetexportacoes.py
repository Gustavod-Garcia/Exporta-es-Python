
Vitor Hugo Araújo Santos - 2422120008
Gustavo dos Santos Garcia - 2422120038
Bibliotecas utilizadas

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import requests
     
Dataframes utilizados dos anos:
- 2018
- 2020
- 2022
- 2024

from google.colab import drive
drive.mount('/content/drive')
     
Mounted at /content/drive

df_exp2018 = pd.read_csv('/content/drive/MyDrive/P2_Estatística_grupo/intro ciencia de dados/Dataset/EXP_2018_MUN.csv', sep=';')
df_exp2020 = pd.read_csv('/content/drive/MyDrive/P2_Estatística_grupo/intro ciencia de dados/Dataset/EXP_2020_MUN.csv', sep=';')
df_exp2022 = pd.read_csv('/content/drive/MyDrive/P2_Estatística_grupo/intro ciencia de dados/Dataset/EXP_2022_MUN.csv', sep=';')
df_exp2024 = pd.read_csv('/content/drive/MyDrive/P2_Estatística_grupo/intro ciencia de dados/Dataset/EXP_2024_MUN.csv', sep=';')
     
Dataframe de código SH de produto


produtos_sh4 = pd.read_csv('/content/drive/MyDrive/P2_Estatística_grupo/intro ciencia de dados/Dataset/NCM_SH.csv', encoding='latin1', sep=';')

     
Dataframe de código de países


paises = pd.read_csv('/content/drive/MyDrive/P2_Estatística_grupo/intro ciencia de dados/Dataset/PAIS.csv', encoding='latin1', sep=';')
     
Limpeza de dados

# Padronizar os nomes das colunas para minúsculas e tirar aspas/ espaços
df_exp2018.columns = df_exp2018.columns.str.lower().str.strip().str.replace('"', '')
df_exp2020.columns = df_exp2018.columns.str.lower().str.strip().str.replace('"', '')
df_exp2022.columns = df_exp2018.columns.str.lower().str.strip().str.replace('"', '')
df_exp2024.columns = df_exp2018.columns.str.lower().str.strip().str.replace('"', '')

produtos_sh4.columns = produtos_sh4.columns.str.lower().str.strip().str.replace('"', '')

paises.columns = paises.columns.str.lower().str.strip().str.replace('"', '')
     

print(paises.columns.tolist())
     
['co_pais', 'co_pais_ison3', 'co_pais_isoa3', 'no_pais', 'no_pais_ing', 'no_pais_esp']

print(df_exp2018.columns.tolist())
     
['co_ano', 'co_mes', 'sh4', 'co_pais', 'sg_uf_mun', 'co_mun', 'kg_liquido', 'vl_fob']

print(produtos_sh4.columns.tolist())
     
['co_sh6', 'no_sh6_por', 'no_sh6_esp', 'no_sh6_ing', 'co_sh4', 'no_sh4_por', 'no_sh4_esp', 'no_sh4_ing', 'co_sh2', 'no_sh2_por', 'no_sh2_esp', 'no_sh2_ing', 'co_ncm_secrom', 'no_sec_por', 'no_sec_esp', 'no_sec_ing']
Adicionar coluna de nome de produto correspondente ao código de produto

# Fazer o merge com base em df_exp2018['sh4'] e produtos_sh4['co_sh4']
df_2018 = pd.merge(
    df_exp2018,
    produtos_sh4[['co_sh4', 'no_sh4_por']],
    left_on='sh4',
    right_on='co_sh4',
    how='left'
)

# Remover a coluna 'co_sh4' duplicada (que veio do produtos_sh4)
df_2018 = df_2018.drop(columns=['co_sh4'])
     

# Fazer o merge com base em df_exp2018['sh4'] e produtos_sh4['co_sh4']
df_2020 = pd.merge(
    df_exp2020,
    produtos_sh4[['co_sh4', 'no_sh4_por']],
    left_on='sh4',
    right_on='co_sh4',
    how='left'
)

# Remover a coluna 'co_sh4' duplicada (que veio do produtos_sh4)
df_2020 = df_2020.drop(columns=['co_sh4'])
     

# Fazer o merge com base em df_exp2018['sh4'] e produtos_sh4['co_sh4']
df_2022 = pd.merge(
    df_exp2022,
    produtos_sh4[['co_sh4', 'no_sh4_por']],
    left_on='sh4',
    right_on='co_sh4',
    how='left'
)

# Remover a coluna 'co_sh4' duplicada (que veio do produtos_sh4)
df_2022 = df_2022.drop(columns=['co_sh4'])
     

# Fazer o merge com base em df_exp2018['sh4'] e produtos_sh4['co_sh4']
df_2024 = pd.merge(
    df_exp2024,
    produtos_sh4[['co_sh4', 'no_sh4_por']],
    left_on='sh4',
    right_on='co_sh4',
    how='left'
)

# Remover a coluna 'co_sh4' duplicada (que veio do produtos_sh4)
df_2024 = df_2024.drop(columns=['co_sh4'])
     
left_on se refere a coluna da primeira tabela que tera uma correlação com a coluna right_on da segunda tabela

how='left' colocará NaN onde o código do produto não bater com o cóigo da segunda tabela


print(df_2018.columns.tolist())

     
['co_ano', 'co_mes', 'sh4', 'co_pais', 'sg_uf_mun', 'co_mun', 'kg_liquido', 'vl_fob', 'no_sh4_por']

df_2018 = df_2018[['co_ano', 'co_mes', 'sh4', 'no_sh4_por', 'co_pais', 'sg_uf_mun', 'co_mun', 'kg_liquido', 'vl_fob']]
df_2020 = df_2020[['co_ano', 'co_mes', 'sh4', 'no_sh4_por', 'co_pais', 'sg_uf_mun', 'co_mun', 'kg_liquido', 'vl_fob']]
df_2022 = df_2022[['co_ano', 'co_mes', 'sh4', 'no_sh4_por', 'co_pais', 'sg_uf_mun', 'co_mun', 'kg_liquido', 'vl_fob']]
df_2024 = df_2024[['co_ano', 'co_mes', 'sh4', 'no_sh4_por', 'co_pais', 'sg_uf_mun', 'co_mun', 'kg_liquido', 'vl_fob']]
     
Adicionar coluna de países

# alterar nome da coluna para poder utilizar o drop futuramente
paises.rename(columns={'co_pais': 'co_paisp'}, inplace=True)
     

print(paises.columns.tolist())
     
['co_paisp', 'co_pais_ison3', 'co_pais_isoa3', 'no_pais', 'no_pais_ing', 'no_pais_esp']

df_2018 = pd.merge(
    df_2018,
    paises[['co_paisp', 'no_pais']],
    left_on='co_pais',
    right_on='co_paisp',
    how='left'
)

df_2018 = df_2018.drop(columns=['co_paisp'])
     

df_2020 = pd.merge(
    df_2020,
    paises[['co_paisp', 'no_pais']],
    left_on='co_pais',
    right_on='co_paisp',
    how='left'
)

df_2020 = df_2020.drop(columns=['co_paisp'])
     

df_2022 = pd.merge(
    df_2022,
    paises[['co_paisp', 'no_pais']],
    left_on='co_pais',
    right_on='co_paisp',
    how='left'
)

df_2022 = df_2022.drop(columns=['co_paisp'])
     

df_2024 = pd.merge(
    df_2024,
    paises[['co_paisp', 'no_pais']],
    left_on='co_pais',
    right_on='co_paisp',
    how='left'
)

df_2024 = df_2024.drop(columns=['co_paisp'])
     

print(df_2018.columns.tolist())
     
['co_ano', 'co_mes', 'sh4', 'no_sh4_por', 'co_pais', 'sg_uf_mun', 'co_mun', 'kg_liquido', 'vl_fob', 'no_pais']

df_2018 = df_2018[['co_ano', 'co_mes', 'sh4', 'no_sh4_por', 'co_pais', 'no_pais', 'sg_uf_mun', 'co_mun', 'kg_liquido', 'vl_fob']]
df_2020 = df_2020[['co_ano', 'co_mes', 'sh4', 'no_sh4_por', 'co_pais', 'no_pais', 'sg_uf_mun', 'co_mun', 'kg_liquido', 'vl_fob']]
df_2022 = df_2022[['co_ano', 'co_mes', 'sh4', 'no_sh4_por', 'co_pais', 'no_pais', 'sg_uf_mun', 'co_mun', 'kg_liquido', 'vl_fob']]
df_2024 = df_2024[['co_ano', 'co_mes', 'sh4', 'no_sh4_por', 'co_pais', 'no_pais', 'sg_uf_mun', 'co_mun', 'kg_liquido', 'vl_fob']]
     

print(df_2018.columns.tolist())
     
['co_ano', 'co_mes', 'sh4', 'no_sh4_por', 'co_pais', 'no_pais', 'sg_uf_mun', 'co_mun', 'kg_liquido', 'vl_fob']

df_2018.head()
     
co_ano	co_mes	sh4	no_sh4_por	co_pais	no_pais	sg_uf_mun	co_mun	kg_liquido	vl_fob
0	2018	1	9999	Consumo de bordo (exceto combustíveis e lubrif...	169	Colômbia	SP	3450308	2	1090
1	2018	1	9999	Consumo de bordo (exceto combustíveis e lubrif...	169	Colômbia	SP	3450308	2	1090
2	2018	1	8483	Veios (árvores) de transmissão [incluídas as á...	63	Argentina	RS	4302105	5	4624
3	2018	1	8483	Veios (árvores) de transmissão [incluídas as á...	63	Argentina	RS	4302105	5	4624
4	2018	1	8483	Veios (árvores) de transmissão [incluídas as á...	63	Argentina	RS	4302105	5	4624
Gráfico passagem de tempo

# Dicionário com os nomes dos DataFrames
dfs = {
    2018: df_2018,
    2020: df_2020,
    2022: df_2022,
    2024: df_2024
}

# Dicionário para armazenar os top 5 por ano
top_paises_por_ano = {}

for ano, df in dfs.items():
    top10 = (
        df.groupby('no_pais')['vl_fob']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    top_paises_por_ano[ano] = top10
    print(f"\nTop 10 países em {ano}:\n{top10}")
     
Top 10 países em 2018:
no_pais
China                      208314539846
Estados Unidos             203808651739
Argentina                  154291891459
Países Baixos (Holanda)     59551781013
México                      43158760503
Chile                       39268351947
Japão                       39005398976
Bélgica                     31023201938
Alemanha                    30916395533
Arábia Saudita              26985487444
Name: vl_fob, dtype: int64

Top 10 países em 2020:
no_pais
China                      240558592564
Estados Unidos             161545855100
Argentina                   83087401979
Países Baixos (Holanda)     43214170875
México                      33215596110
Japão                       32711872493
Singapura                   26845340599
Chile                       25764382446
Arábia Saudita              23696842469
Bélgica                     23106124631
Name: vl_fob, dtype: int64

Top 10 países em 2022:
no_pais
China                      305366594762
Estados Unidos             259870865696
Argentina                  143615698639
Países Baixos (Holanda)     66408091328
México                      65291851614
Chile                       58193589492
Singapura                   57942622507
Japão                       48151043563
Colômbia                    43599348961
Bélgica                     37813232826
Name: vl_fob, dtype: int64

Top 10 países em 2024:
no_pais
China                      305945090953
Estados Unidos             277753945465
Argentina                  135212001431
México                      76652096607
Países Baixos (Holanda)     68940300564
Singapura                   51323661237
Japão                       46376448271
Emirados Árabes Unidos      42526210487
Chile                       40957900450
Bélgica                     38688714436
Name: vl_fob, dtype: int64

# Criar subplots 2x2
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

# Plotar os gráficos com base no dicionário top_paises_por_ano
for i, (ano, series) in enumerate(top_paises_por_ano.items()):
    axes[i].barh(series.index[::-1], series.values[::-1])  # maior valor no topo
    axes[i].set_title(f'Top 10 países - {ano}')
    axes[i].set_xlabel('Valor FOB (USD)')
    axes[i].set_ylabel('País')

plt.tight_layout()
plt.show()
     


for ano, df in dfs.items():
    print(f"{ano} - Linhas: {len(df)} | Anos únicos: {df['co_ano'].unique()}")
     
2018 - Linhas: 6598153 | Anos únicos: [2018]
2020 - Linhas: 7743336 | Anos únicos: [2020]
2022 - Linhas: 8620084 | Anos únicos: [2022]
2024 - Linhas: 9034773 | Anos únicos: [2024]
Compreender produtos mais exportados

def top_produtos_sh4(df, top_n=10):
    """
    Retorna os top N códigos SH4 mais frequentes com seus nomes.

    Parâmetros:
    - df: DataFrame contendo colunas 'sh4' e 'no_sh4_por'
    - top_n: número de produtos a retornar (default = 10)

    Retorno:
    - DataFrame com colunas: sh4, no_sh4_por, quantidade
    """
    # Conta quantas vezes cada código aparece
    contagem = df['sh4'].value_counts().reset_index()
    contagem.columns = ['sh4', 'quantidade']

    # Junta com os nomes dos produtos
    resultado = pd.merge(contagem, df[['sh4', 'no_sh4_por']].drop_duplicates(), on='sh4', how='left')

    # Retorna apenas os top N
    return resultado.head(top_n)

     

df_2018.head()
     
co_ano	co_mes	sh4	no_sh4_por	co_pais	no_pais	sg_uf_mun	co_mun	kg_liquido	vl_fob
0	2018	1	9999	Consumo de bordo (exceto combustíveis e lubrif...	169	Colômbia	SP	3450308	2	1090
1	2018	1	9999	Consumo de bordo (exceto combustíveis e lubrif...	169	Colômbia	SP	3450308	2	1090
2	2018	1	8483	Veios (árvores) de transmissão [incluídas as á...	63	Argentina	RS	4302105	5	4624
3	2018	1	8483	Veios (árvores) de transmissão [incluídas as á...	63	Argentina	RS	4302105	5	4624
4	2018	1	8483	Veios (árvores) de transmissão [incluídas as á...	63	Argentina	RS	4302105	5	4624
Quais foram os principais países latino-americanos de destino das exportações brasileiras?

paises_latam = [
    'Argentina', 'Bolívia', 'Chile', 'Colômbia', 'Equador', 'Guiana',
    'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela', 'México'
]

# Variáveis para armazenar as somas
soma_latam = 0
soma_total_mundial = 0

for ano, df in dfs.items():
    # Soma para os países da LATAM no ano
    soma_latam += df[df['no_pais'].isin(paises_latam)]['vl_fob'].sum()
    # Soma o total do ano
    soma_total_mundial += df['vl_fob'].sum()

# Calcula o percentual
percentual_latam = (soma_latam / soma_total_mundial) * 100

print("\n--- Resultado Final ---")
print(f"Valor total exportado para a América Latina: ${soma_latam:,.2f}")
print(f"Valor total exportado para o Mundo: ${soma_total_mundial:,.2f}")
print(f"A América Latina representou {percentual_latam:.2f}% do total de exportações no período.")
     
--- Resultado Final ---
Valor total exportado para a América Latina: $1,384,840,870,067.00
Valor total exportado para o Mundo: $6,237,566,366,656.00
A América Latina representou 22.20% do total de exportações no período.
Quais países mais exportaram do Brasil entre 2018 e 2024?

def preparar_df(df, ano):
    df_ano = df.groupby('no_pais')['vl_fob'].sum().reset_index()
    df_ano['ano'] = ano
    df_ano.rename(columns={'no_pais': 'País', 'vl_fob': 'Valor_FOB'}, inplace=True)
    return df_ano

# Exemplo: se seus dfs reais forem df_2018, df_2020, df_2022 e df_2024:
top_2018 = preparar_df(df_2018, 2018).sort_values(by='Valor_FOB', ascending=False).head(10)
top_2020 = preparar_df(df_2020, 2020).sort_values(by='Valor_FOB', ascending=False).head(10)
top_2022 = preparar_df(df_2022, 2022).sort_values(by='Valor_FOB', ascending=False).head(10)
top_2024 = preparar_df(df_2024, 2024).sort_values(by='Valor_FOB', ascending=False).head(10)

# Concatenar todos os anos em um único df
df_destinos = pd.concat([top_2018, top_2020, top_2022, top_2024], ignore_index=True)

# Função para abreviar nome de país longo
def abreviar_pais(nome):
    partes = nome.split()
    return ' '.join([p[:6] + '.' if len(p) > 7 else p for p in partes])

df_destinos['País_Abrev'] = df_destinos['País'].apply(abreviar_pais)

# Função para formatar valores em bilhões (com 1 casa decimal)
def formatar_bilhoes(x):
    return f"${x/1e9:.1f}B"

anos = sorted(df_destinos['ano'].unique())
fig_barras = make_subplots(rows=1, cols=len(anos), subplot_titles=[f"Top 10 Destinos - {ano}" for ano in anos])

for i, ano in enumerate(anos):
    dados = df_destinos[df_destinos['ano'] == ano].sort_values(by='Valor_FOB', ascending=True)
    fig_barras.add_trace(
        go.Bar(
            x=dados['Valor_FOB'],
            y=dados['País_Abrev'],
            orientation='h',
            name=str(ano),
            text=dados['Valor_FOB'].apply(formatar_bilhoes),
            hovertext=dados['País'],
            hovertemplate='%{hovertext}Valor FOB: US$ %{x:,.0f}',
            hoverinfo='text+x',
            textposition='auto'
        ),
        row=1, col=i+1
    )

fig_barras.update_layout(
    title_text='Países que Mais Exportaram do Brasil (2018–2024)',
    margin=dict(l=50, r=50, t=80, b=50),
    plot_bgcolor='white',
    paper_bgcolor='whitesmoke',
    font=dict(family="Arial, sans-serif", size=12, color="black")
)

# Gráfico de rosca com participação total (soma dos 4 anos)
df_soma = df_destinos.groupby('País')['Valor_FOB'].sum().reset_index()
df_soma['percent'] = 100 * df_soma['Valor_FOB'] / df_soma['Valor_FOB'].sum()

fig_rosca = go.Figure(
    go.Pie(
        labels=df_soma['País'],
        values=df_soma['Valor_FOB'],
        hole=0.5,
        textinfo='label+percent',
        hovertemplate='%{label}US$ %{value:,.0f}'
    )
)

fig_rosca.update_layout(
    title_text='Participação Total dos Destinos',
    font=dict(family="Arial, sans-serif", size=12, color="black")
)
fig_barras.show()
fig_rosca.show()

fig_barras.write_html("grafico_top10_por_ano.html")
fig_rosca.write_html("grafico_rosca_destinos.html")

     
Qual foi o total de exportação brasileira para a América Latina em comparação com o resto do mundo?

paises_latam = [
    'Argentina', 'Bolívia', 'Chile', 'Colômbia', 'Equador', 'Guiana',
    'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela', 'México'
]

# Inicializa os somatórios
soma_latam = 0
soma_total_mundial = 0

# Lista de DataFrames (ajuste os nomes se forem diferentes)
lista_dfs = [df_2018, df_2020, df_2022, df_2024]

# Loop para calcular os totais
for df in lista_dfs:
    soma_latam += df[df['no_pais'].isin(paises_latam)]['vl_fob'].sum()
    soma_total_mundial += df['vl_fob'].sum()

# Conversão para trilhões
soma_latam_trilhoes = soma_latam / 1e12
soma_total_trilhoes = soma_total_mundial / 1e12
percentual_latam = (soma_latam / soma_total_mundial) * 100

# Criação do gráfico
fig = go.Figure()

fig.add_trace(go.Bar(
    x=["América Latina", "Resto do Mundo"],
    y=[soma_latam_trilhoes, soma_total_trilhoes - soma_latam_trilhoes],
    marker_color=['#1f77b4', '#ff7f0e'],
    text=[f"{soma_latam_trilhoes:.2f} tri", f"{(soma_total_trilhoes - soma_latam_trilhoes):.2f} tri"],
    textposition='auto',
    name="Exportação em trilhões USD"
))

fig.add_trace(go.Scatter(
    x=["América Latina", "Resto do Mundo"],
    y=[soma_latam_trilhoes, soma_total_trilhoes - soma_latam_trilhoes],
    mode='text',
    text=[f"{percentual_latam:.1f}%", f"{100 - percentual_latam:.1f}%"],
    textposition="top center",
    showlegend=False
))

fig.update_layout(
    title="Exportações Brasileiras: América Latina vs Resto do Mundo (Total do Período)",
    yaxis_title="Valor Exportado (em trilhões de USD)",
    xaxis_title="Região",
    template="plotly_white",
    height=500,
    width=700,
    yaxis=dict(
        showticklabels=False  # remove os números no eixo Y
    )
)

fig.show()
fig.write_html("latam_vsmundo.html")
     
Quais estados brasileiros lideraram as exportações totais??

def top_ufs(df, ano):
    df_ano = df.groupby('sg_uf_mun')['vl_fob'].sum().reset_index()
    df_ano = df_ano.sort_values(by='vl_fob', ascending=False).head(10)
    df_ano['ano'] = ano
    df_ano.rename(columns={'sg_uf_mun': 'UF', 'vl_fob': 'Valor_FOB'}, inplace=True)
    return df_ano

# Substitua pelos seus dataframes reais:
top_uf_2018 = top_ufs(df_2018, 2018)
top_uf_2020 = top_ufs(df_2020, 2020)
top_uf_2022 = top_ufs(df_2022, 2022)
top_uf_2024 = top_ufs(df_2024, 2024)

# Concatenar os dados
df_ufs = pd.concat([top_uf_2018, top_uf_2020, top_uf_2022, top_uf_2024], ignore_index=True)

# === Agrupar o total por UF ===
df_uf_total = df_ufs.groupby('UF')['Valor_FOB'].sum().reset_index()

# === Obter GeoJSON dos estados brasileiros ===
geojson_url = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'
geojson_br = requests.get(geojson_url).json()

# === Função para formatar os valores de forma compacta ===
def formatar_valor_compacto(x):
    if x >= 1e12:
        return f"${x/1e12:.1f}T"
    elif x >= 1e9:
        return f"${x/1e9:.1f}B"
    elif x >= 1e6:
        return f"${x/1e6:.1f}M"
    else:
        return f"${x:,.0f}"

# === Ordenar para o gráfico de barras ===
df_uf_sorted = df_uf_total.sort_values(by='Valor_FOB', ascending=True)

# === Criar a figura com subplots ===
fig = make_subplots(
    rows=1, cols=2,
    column_widths=[0.6, 0.4],
    subplot_titles=["Mapa do Brasil por Estado", "Top Estados Exportadores"],
    specs=[[{"type": "choropleth"}, {"type": "bar"}]]
)

# === Gráfico 1: Mapa do Brasil ===
choromap = go.Choropleth(
    geojson=geojson_br,
    locations=df_uf_total['UF'],
    z=df_uf_total['Valor_FOB'],
    featureidkey="properties.sigla",
    locationmode="geojson-id",
    colorscale="Viridis",
    colorbar_title="FOB (US$)",
    hovertemplate='%{location}US$ %{z:,.0f}',
    showscale=False
)
fig.add_trace(choromap, row=1, col=1)

# === Gráfico 2: Barras por UF com texto em B/T ===
barplot = go.Bar(
    y=df_uf_sorted['UF'],
    x=df_uf_sorted['Valor_FOB'],
    orientation='h',
    text=df_uf_sorted['Valor_FOB'].apply(formatar_valor_compacto),
    hovertemplate='%{y}Valor FOB: US$ %{x:,.0f}',
    marker=dict(color='royalblue'),
    textposition='auto'
)
fig.add_trace(barplot, row=1, col=2)

# === Layout e ajustes finais ===
fig.update_geos(
    fitbounds="locations",
    visible=False,
    scope="south america",
    resolution=50,
    showland=True,
    landcolor="white",
    showcountries=True,
    countrycolor="gray"
)

fig.update_layout(
    title_text="Exportações por Estado (UF) – Brasil (2018–2024)",
    height=600,
    width=1000,
    paper_bgcolor='white',
    plot_bgcolor='white',
    font=dict(family="Arial", size=13),
    margin=dict(t=50, l=20, r=20, b=20),
    showlegend=False
)

fig.show()
fig.write_html("estados_exportacoes.html")
     
Quais estados brasileiros mais exportaram entre 2018 e 2024 (variação)?

# Converter para bilhões
df_ufs['Valor_FOB_bilhoes'] = df_ufs['Valor_FOB'] / 1e9

# Criar label resumida para exibir na barra (ex: US$12,0 bi)
df_ufs['label_resumido'] = df_ufs['Valor_FOB_bilhoes'].apply(lambda x: f"US${x:.1f} bi")

# Definir posição e cor do texto conforme valor, limite exemplo 180 bi
def definir_pos_texto(valor):
    if valor < 180:
        return 'outside', 'black'  # texto fora da barra e cor preta
    else:
        return 'inside', 'white'   # texto dentro da barra e cor branca

posicoes = df_ufs['Valor_FOB_bilhoes'].apply(lambda x: definir_pos_texto(x))
df_ufs['textposition'] = posicoes.apply(lambda x: x[0])
df_ufs['textcolor'] = posicoes.apply(lambda x: x[1])

anos = sorted(df_ufs['ano'].unique())
fig_ufs = make_subplots(
    rows=1, cols=len(anos),
    subplot_titles=[f"{ano}" for ano in anos]
)

for i, ano in enumerate(anos):
    dados = df_ufs[df_ufs['ano'] == ano].sort_values(by='Valor_FOB_bilhoes', ascending=True)
    fig_ufs.add_trace(
        go.Bar(
            x=dados['Valor_FOB_bilhoes'],
            y=dados['UF'],
            orientation='h',
            text=dados['label_resumido'],
            textposition=dados['textposition'],
            textfont=dict(color=dados['textcolor']),
            hovertemplate='UF: %{y}Valor FOB: US$%{x:.2f} bi',
            marker=dict(color='rgba(26, 118, 255, 0.7)', line=dict(color='black', width=1))
        ),
        row=1, col=i+1
    )

fig_ufs.update_layout(
    height=600,
    width=1400,
    showlegend=False,
    font=dict(family="Arial, sans-serif", size=14, color="darkblue"),
    margin=dict(l=70, r=40, t=80, b=70),
    plot_bgcolor='white',
    paper_bgcolor='whitesmoke',
    title_text="Top 10 Estados Exportadores por Ano (2018-2024)"
)

fig_ufs.update_xaxes(title_text='Valor FOB (bi USD)', ticksuffix=' B', showgrid=True)
fig_ufs.update_yaxes(title_text='UF', showgrid=False)

fig_ufs.show()
fig_ufs.write_html("estados_exportacoes_ano.html")
     
Quais estados brasileiros lideraram as exportações para o nosso maior parceiro comercial?

top_china = []
for ano, df in zip([2018, 2020, 2022, 2024], [df_2018, df_2020, df_2022, df_2024]):
    df_china = df[df['no_pais'].str.lower() == 'china']
    grouped = df_china.groupby('sg_uf_mun')['vl_fob'].sum().sort_values(ascending=False).head(5).reset_index()
    grouped['ano'] = ano
    top_china.append(grouped)

top_china_df = pd.concat(top_china)

# Converter valores para bilhões de dólares
top_china_df['vl_fob_bilhoes'] = top_china_df['vl_fob'] / 1e9

# Gráfico de barras agrupadas com Plotly Express
fig = px.bar(
    top_china_df,
    x='sg_uf_mun',
    y='vl_fob_bilhoes',
    color='ano',
    barmode='group',
    labels={
        'sg_uf_mun': 'Estado (UF)',
        'vl_fob_bilhoes': 'Valor FOB (US$ bilhões)',
        'ano': 'Ano'
    },
    title='Top 5 Estados Exportadores para a China (Total do Período)',
    color_continuous_scale=px.colors.sequential.Viridis
)

# Ajustes visuais
fig.update_layout(
    template='plotly_white',
    font=dict(size=14),
    legend_title_text='Ano',
    yaxis=dict(tickprefix='$', ticksuffix=' B'),
    xaxis_title='Estado (UF)',
    yaxis_title='Valor FOB (US$ bilhões)',
    height=550,
    width=900,
    margin=dict(l=50, r=50, t=80, b=50)
)

fig.update_traces(
    hovertemplate='UF: %{x}Valor FOB: %{y:.2f} B USDAno: %{marker.color}'
)

fig.show()
fig.write_html("estados_exportacoes_china.html")
     
Quais produtos ou setores lideraram as exportações do Brasil entre 2018 e 2024?

def preparar_top10(df, ano):
    top = df.groupby('no_sh4_por')['vl_fob'].sum().sort_values(ascending=False).head(10).reset_index()
    top['ano'] = ano
    return top

top_2018 = preparar_top10(df_2018, 2018)
top_2020 = preparar_top10(df_2020, 2020)
top_2022 = preparar_top10(df_2022, 2022)
top_2024 = preparar_top10(df_2024, 2024)

# ---- Unir e renomear ----
df_top = pd.concat([top_2018, top_2020, top_2022, top_2024])
df_top.rename(columns={'no_sh4_por': 'Produto', 'vl_fob': 'Valor_FOB'}, inplace=True)

# ---- Preencher nomes curtos (resumidos) manualmente ----
resumos = {
    'Carnes e miudezas comestíveis': 'Carne',
    'Soja': 'Soja',
    'Automóveis de passageiros': 'Carros',
    'Minérios de ferro': 'Minério de Ferro',
    'Sumos de frutas': 'Suco de Frutas',
    'Ferro-ligas': 'Ferro-ligas',
    'Partes e acessórios dos veículos': 'Peças de Carros',
    'Açúcares de cana': 'Açúcar',
    'Pastas químicas de madeira': 'Celulose',
    'Óleos de petróleo': 'Óleo Refinado',
    'Café, mesmo torrado': 'Café',
    'Óleos brutos de petróleo': 'Petróleo Bruto'
}

# Aplicar os nomes resumidos por busca parcial (flexível)
def resumir(produto):
    for chave, resumo in resumos.items():
        if chave.lower() in produto.lower():
            return resumo
    return "Outro"

df_top['Produto_resumido'] = df_top['Produto'].apply(resumir)

# ---- Criar MultiGO ----
anos = sorted(df_top['ano'].unique())
fig = make_subplots(rows=1, cols=len(anos), subplot_titles=[f"{ano}" for ano in anos])

for i, ano in enumerate(anos):
    dados = df_top[df_top['ano'] == ano].sort_values(by='Valor_FOB', ascending=True)

    fig.add_trace(
    go.Bar(
        x=dados['Valor_FOB'],
        y=dados['Produto_resumido'],
        orientation='h',
        name=str(ano),
        text=dados['Valor_FOB'].apply(lambda x: f"US${x/1e9:.1f} bi"),  # Valor formatado na barra
        textposition='auto',
        hovertext=dados['Produto'],  # Nome completo no hover
        hoverinfo='text'
    ),
    row=1, col=i+1
)

fig.update_layout(
    height=600,
    width=1400,
    title_text="MultiGO: Top 10 Produtos Exportados por Ano",
    showlegend=False
)

fig.show()
fig.write_html("produts_exportados.html")
     
Quais produtos ou setores lideraram as exportações do Brasil para a América Latina entre 2018 e 2024?

latam_paises = [
    'Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Costa Rica', 'Cuba', 'Equador',
    'El Salvador', 'Guatemala', 'Honduras', 'México', 'Nicarágua', 'Panamá', 'Paraguai',
    'Peru', 'República Dominicana', 'Uruguai', 'Venezuela'
]

# Função para filtrar, agrupar e extrair os top 10 por ano
def top10_latam(df, ano):
    df_latam = df[df['no_pais'].isin(latam_paises)]
    top = df_latam.groupby('no_sh4_por')['vl_fob'].sum().reset_index()
    top = top.sort_values(by='vl_fob', ascending=False).head(10)
    top['ano'] = ano
    return top

# Aplicar para cada ano
top_2018 = top10_latam(df_2018, 2018)
top_2020 = top10_latam(df_2020, 2020)
top_2022 = top10_latam(df_2022, 2022)
top_2024 = top10_latam(df_2024, 2024)

# Unir os dados
df_top_latam = pd.concat([top_2018, top_2020, top_2022, top_2024], ignore_index=True)

# Dicionário de nomes resumidos
resumos = {
    'Carnes e miudezas comestíveis': 'Carne',
    'Soja': 'Soja',
    'Automóveis de passageiros': 'Carros',
    'Minérios de ferro': 'Minério de Ferro',
    'Sumos de frutas': 'Suco de Frutas',
    'Ferro-ligas': 'Ferro-ligas',
    'Partes e acessórios dos veículos': 'Peças de Carros',
    'Açúcares de cana': 'Açúcar',
    'Pastas químicas de madeira': 'Celulose',
    'Óleos de petróleo': 'Óleo Refinado',
    'Café': 'Café',
    'Óleos brutos de petróleo': 'Petróleo Bruto'
}

# Função para resumir nomes
def resumir(produto):
    for chave, resumo in resumos.items():
        if chave.lower() in produto.lower():
            return resumo
    return produto[:15] + '...'  # fallback

df_top_latam['Produto_resumido'] = df_top_latam['no_sh4_por'].apply(resumir)

# Criar gráfico com subplots
anos = sorted(df_top_latam['ano'].unique())
fig = make_subplots(rows=1, cols=len(anos), subplot_titles=[f"LATAM - {ano}" for ano in anos])

for i, ano in enumerate(anos):
    dados = df_top_latam[df_top_latam['ano'] == ano].sort_values(by='vl_fob', ascending=True)

    fig.add_trace(
        go.Bar(
            x=dados['vl_fob'],
            y=dados['Produto_resumido'],
            orientation='h',
            text=dados['vl_fob'].apply(lambda x: f"US${x/1e9:.1f} bi"),
            textposition='auto',
            hovertext=dados['no_sh4_por'],
            hoverinfo='text'
        ),
        row=1, col=i+1
    )

# Layout
fig.update_layout(
    height=600,
    width=1400,
    title_text="Top 10 Produtos Exportados para América Latina por Ano",
    showlegend=False,
    font=dict(family="Arial", size=13),
    paper_bgcolor="whitesmoke",
    plot_bgcolor="white",
    margin=dict(t=60, l=60, r=40, b=60)
)

# Exibir
fig.show()

# (Opcional) Salvar como HTML
# fig.write_html("top_latam_produtos.html")

     
Como evoluiu o total de exportações do Brasil entre 2018 e 2024?

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=df_evolucao['data'],
    y=df_evolucao['vl_fob_bilhoes'],
    mode='lines+markers',
    name="Exportações",
    line=dict(width=2, color='darkblue'),
    marker=dict(size=5),
    fill='tozeroy',
    hovertemplate="Data: %{x|%b/%Y}FOB: $%{y:.2f} bi"
))

fig.update_layout(
    autosize=True,
    height=550,
    title=dict(
        text="📈 Evolução Mensal das Exportações Brasileiras (2018–2024)",
        font=dict(size=18),
        x=0.5
    ),
    xaxis_title="Mês/Ano",
    yaxis_title="Valor FOB (em bilhões de USD)",
    template="plotly_white",
    font=dict(family="Arial", size=13),
    legend=dict(title="Ano", orientation="h", x=0.5, xanchor="center", y=-0.15),
    margin=dict(t=60, l=60, r=40, b=80)
)

# Eixo Y personalizado
fig.update_yaxes(
    tickprefix="$",
    showgrid=True,
    zeroline=True,
    title_font=dict(size=14),
    range=[df_evolucao['vl_fob_bilhoes'].min() * 0.95, df_evolucao['vl_fob_bilhoes'].max() * 1.05]
)

# Eixo X: mostrar apenas 1 tick por ano
fig.update_xaxes(
    showgrid=True,
    tickformat="%Y",
    tickangle=0,
    dtick="M12",
    title_font=dict(size=14)
)

fig.show()
fig.write_html("venda_anual.html")
     
