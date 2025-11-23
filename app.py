# app.py
import streamlit as st
import openai
from datetime import datetime

st.set_page_config(page_title="Content API Turbo com OpenAI", layout="wide")
st.title("Content API Turbo")
st.markdown("### Gerador de textos para atendimento, promoções e parceiros")
st.caption("Feito por Erick Costa – Nov/2025")

# API Key
api_key = st.text_input("Cole sua API key abaixo",type="password", value=st.session_state.get("api_key", ""))
if api_key:
    st.session_state.api_key = api_key
    openai.api_key = api_key

# Abas
tab1, tab2, tab3, tab4 = st.tabs(["Resposta de Atendimento", "Resumo de Cardápio", "Promoção do Dia", "E-mail para Parceiro"])

with tab1:
    st.subheader("Resposta de atendimento (cliente reclamou)")
    reclamacao = st.text_area("O que o cliente escreveu?", height=120, placeholder="Ex: meu pedido veio frio e atrasado 40 minutos")
    if st.button("Gerar resposta empática + solução", type="primary"):
        with st.spinner("Gerando resposta perfeita..."):
            r = openai.chat.completions.create(
                model="gpt-4o-mini",
                temperature=0.7,
                messages=[{"role": "user", "content": f"Responda com empatia, peça desculpas, ofereça solução (vale-refeição ou desconto) e finalize com tom positivo. Máximo 4 linhas.\n\nCliente disse: {reclamacao}"}]
            )
            st.success("Resposta pronta!")
            st.info(r.choices[0].message.content)

with tab2:
    st.subheader("Resumo de cardápio para WhatsApp")
    cardapio = st.text_area("Cole parte do cardápio", height=150, placeholder="Pizza Margherita R$ 49,90\nHambúrguer Artesanal R$ 34,90\n...")
    if st.button("Gerar resumo atraente com emojis", type="primary"):
        with st.spinner("Criando texto matador..."):
            r = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": f"Transforme isso em um texto curto, atraente com emojis para mandar no WhatsApp do cliente:\n\n{cardapio}"}]
            )
            st.success("Pronto para enviar!")
            st.info(r.choices[0].message.content)

with tab3:
    st.subheader("Promoção do dia")
    prato = st.text_input("Prato principal", "Pizza Grande")
    preco = st.text_input("Preço promocional", "R$ 39,90")
    if st.button("Gerar texto com urgência", type="primary"):
        with st.spinner("Criando promoção irresistível..."):
            r = openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": f"Crie 3 variações de texto promocional com urgência e emojis para {prato} por apenas {preco} HOJE!"}]
            )
            texto = r.choices[0].message.content
            st.success("3 opções prontas!")
            st.markdown(texto)

with tab4:
    st.subheader("E-mail profissional para parceiro")
    parceiro = st.text_input("Nome do restaurante", "Pizzaria do João")
    assunto = st.text_input("Assunto", "Aumento de 30% nas vendas com nova campanha")
    if st.button("Gerar e-mail completo", type="primary"):
        with st.spinner("Escrevendo e-mail perfeito..."):
            r = openai.chat.completions.create(
                model="gpt-4o-mini",
                temperature=0.6,
                messages=[{"role": "user", "content": f"Escreva um e-mail profissional, amigável e com dados para o parceiro {parceiro}. Assunto: {assunto}. Inclua saudação, corpo com 3 parágrafos e despedida."}]
            )
            email = r.choices[0].message.content
            st.success("E-mail pronto!")
            st.text_area("Copie e envie", email, height=300)
