import streamlit as st

# Configuração da página com ícone e título
st.set_page_config(
    page_title="Gas Calculator",
    page_icon="🚗",
    layout="centered"
)


# Título da aplicação com cor customizada
st.markdown("<h1 style='text-align: center; color: #FF5733; padding-bottom: 50px;'>🚗 Calculadora de Custo 🚗</h1>", unsafe_allow_html=True)

# Dividir a tela em duas colunas para melhor visualização
col1, col2 = st.columns(2)

# Estilo dos inputs e botões
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
    }
    div.stButton > button:hover {
        background-color: #45a049;
        color: white;
    }
    div[data-baseweb="select"] > div {
        color: black;  /* Cor do texto na selectbox */
    }
    div[data-baseweb="select"] > div > div {
        color: black;  /* Cor do texto das opções da selectbox */
    }

    </style>
    """, unsafe_allow_html=True)

# Inicializa a sessão para armazenar o custo total e divisão por pessoa
if 'custo_total' not in st.session_state:
    st.session_state.custo_total = None
if 'custo_por_pessoa' not in st.session_state:
    st.session_state.custo_por_pessoa = None

# Dividir a tela em duas colunas para melhor visualização
col1, col2 = st.columns(2)

# Espaçamento extra entre as linhas
with col1:
    km_por_litro = st.number_input("Quantos KM/L seu carro faz?", min_value=0.1, step=0.1)
    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)  # Espaçamento entre os inputs
    qtd_viagens = st.number_input("Quantas vezes você percorreu essa distância?", min_value=1, step=1)
    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)  # Espaçamento entre os inputs

with col2:
    distancia_percorrida = st.number_input("Qual foi a distância percorrida pelo carro (KM)?", min_value=0.1, step=0.1)
    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)  # Espaçamento inferior
    preco_gasolina = st.number_input("Qual é o preço do litro da gasolina (R$)?", min_value=0.1, step=0.1)
    st.markdown("<div style='margin-bottom: 20px;'></div>", unsafe_allow_html=True)  # Espaçamento inferior

# Botão para calcular o custo
calcular = st.button("Calcular Custo")

# Verifica se o botão foi clicado
if calcular or st.session_state.custo_total is not None:
    # Cálculo do custo total
    st.session_state.custo_total = (distancia_percorrida * qtd_viagens / km_por_litro) * preco_gasolina
    st.markdown(f"<h2 style='text-align: center; color: #4CAF50;'>O custo total da locomoção foi: R${st.session_state.custo_total:.2f}</h2>", unsafe_allow_html=True)

# Pergunta se o usuário deseja dividir o custo
if st.session_state.custo_total is not None:
    dividir_custo = st.radio("Você gostaria de dividir o custo entre outras pessoas?", options=['Não', 'Sim'])

    if dividir_custo == 'Sim':
        numero_pessoas = st.selectbox("Dividir entre quantas pessoas?", [2, 3, 4])
        
        # Botão para calcular o custo por pessoa
        calcular_divisao = st.button("Calcular Custo por Pessoa")

        if calcular_divisao:
            st.session_state.custo_por_pessoa = st.session_state.custo_total / numero_pessoas
            st.markdown(f"<h3 style='text-align: center; color: #FF5733;'>O custo por pessoa é: R${st.session_state.custo_por_pessoa:.2f}</h3>", unsafe_allow_html=True)

# Botão para reiniciar a aplicação com classe para estilização
reiniciar = st.button("Reiniciar", key="reiniciar_button", help="Clique aqui para reiniciar a calculadora")

if reiniciar:
    # Redefine os valores no session state
    st.session_state.custo_total = None
    st.session_state.custo_por_pessoa = None
    st.rerun()


