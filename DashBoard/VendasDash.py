#!/usr/bin/env python
# coding: utf-8

# In[17]:


import streamlit as st
import pandas as pd
import plotly.express as px


# In[18]:


st.set_page_config(layout='wide')

dados = pd.read_excel('C:/DashBoard/Vendas_Tratado.xlsx')
#dados

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

graf1 = px.bar(dados, x='Nome do Produto', y='Quantidade Vendida', color='Sede', title='Vendas por Produto')
graf1.update_layout(title_x=0.5)
col1.plotly_chart(graf1, use_container_width=True)

sedes = dados.groupby('Sede')[['Quantidade Vendida']].sum().reset_index()
graf2 = px.bar(sedes, x='Sede', y='Quantidade Vendida', title='Vendas por sede')
graf2.update_layout(title_x=0.5)
col2.plotly_chart(graf2, use_container_width=True)

lucratividade = dados['Lucratividade'].value_counts().reset_index()
graf3 = px.pie(lucratividade, values='count', names='Lucratividade', title='Lucratividade geral')
graf3.update_layout(title_x=0.5)
col3.plotly_chart(graf3, use_container_width=True)

graf4 = px.bar(dados, x='Nome do Produto', y='Lucro Bruto', title='Lucro bruto por produto')
graf4.update_layout(title_x=0.5)
col4.plotly_chart(graf4, use_container_width=True)


# In[13]:





# In[ ]:




