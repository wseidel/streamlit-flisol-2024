from urllib.error import URLError
import streamlit as st

import pandas as pd
import numpy as np
import pydeck as pdk


#
# Configurações da Página.
#
st.set_page_config(
    page_title="Copia do Mapping Demo", 
    page_icon="🌍"
    )

# st.title("Plágio do Mapping Demo")
st.markdown("# Simplificação dos exemplos")
st.sidebar.header("Simplificando os exemplos")
st.write(
    """Esta é uma cópia da demonstração de uso de Mapas do Stremlit.
Faça você a sua cópia também para conseguir não copiar depois! :)
    """
)

#
#
# Primeiro Exemplo: Produção Agrícola
#
#

# https://docs.streamlit.io/develop/api-reference
st.header("Usando os Produção Agrícola")
st.subheader("Produção Agrícola Bruta")




#
#
# Carregando os dados.
#
#
df_agri = pd.read_csv("./data/agri.csv")


# df_stop_stats = pd.read_json("./data/bart_stop_stats.json")
# df_bart_path_stats = pd.read_json("./data/bart_path_stats.json")
# df_bikes = pd.read_json("./data/bike_rental_stats.json")




with st.expander("Exemplo usando o dataframe Agri"):
    df_agri
    df_agri = df_agri.set_index("Region")
    df_agri
    df_agri.index

countries = st.sidebar.multiselect(
    "Choose countries", list(df_agri.index), ["China", "United States of America"]
)

# countries


df_agri = df_agri.loc[countries]

# df_agri

st.line_chart(df_agri.T)

# df_stop_stats
# df_bart_path_stats
# df_bikes

# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

# st.line_chart(chart_data)






#
#
# Segundo Exemplo: Usando mapas...
#
#

# st.header("Usando os Produção Agrícola")
# st.subheader("Produção Agrícola Bruta")
























#
#  PyDeck
#

# camada_vazia = pdk.Layer(
#         "HexagonLayer",
#         data=[],
#         get_position=["lon", "lat"],
#         radius=200,
#         elevation_scale=4,
#         elevation_range=[0, 1000],
#         extruded=True,
#     )

# camada_onde_tem_bike = pdk.Layer(
#         "HexagonLayer",
#         data=df_bikes,
#         get_position=["lon", "lat"],
#         radius=200,
#         elevation_scale=4,
#         elevation_range=[0, 1000],
#         extruded=True,
#     )



# camada_ponto_de_onibus_nomes = pdk.Layer(
#         "TextLayer",
#         data=df_stop_stats,
#         get_position=["lon", "lat"],
#         get_text="name",
#         get_color=[0, 0, 0, 200],
#         get_size=10,
#         get_alignment_baseline="'bottom'",
#     )



# camada_ponto_de_onibus_localizacao = pdk.Layer(
#         "ScatterplotLayer",
#         data=df_stop_stats,
#         get_position=["lon", "lat"],
#         get_color=[200, 30, 0, 160],
#         get_radius="[exits]",
#         radius_scale=0.05,
#     )


# camada_fluxo_dos_onibus = pdk.Layer(
#         "ArcLayer",
#         data=df_bart_path_stats,
#         get_source_position=["lon", "lat"],
#         get_target_position=["lon2", "lat2"],
#         get_source_color=[200, 30, 0, 160],
#         get_target_color=[200, 30, 0, 160],
#         auto_highlight=True,
#         width_scale=0.0001,
#         get_width="outbound",
#         width_min_pixels=3,
#         width_max_pixels=30,
#     )


# camadas_para_o_mapa = [camada_vazia]

# camadas_para_o_mapa.append( camada_onde_tem_bike )
# camadas_para_o_mapa.append( camada_ponto_de_onibus_nomes )
# camadas_para_o_mapa.append( camada_ponto_de_onibus_localizacao )
# camadas_para_o_mapa.append( camada_fluxo_dos_onibus )




# st.markdown("### O Mapa:")  
# st.pydeck_chart(
#     pdk.Deck(
#         map_style=None,
#         initial_view_state={
#             "latitude": 37.76,
#             "longitude": -122.4,
#             "zoom": 11,
#             "pitch": 50,
#         },
#         layers=camadas_para_o_mapa,
#     )
# )























# TODAS_AS_CAMADAS = {
#     "Vazia": camada_vazia,
#     "Onde tem bike de aluguel ?": camada_onde_tem_bike,
#     "Ponto de ônibus": camada_ponto_de_onibus_localizacao,
#     "Nomes dos pontos": camada_ponto_de_onibus_nomes,
#     "Fluxo": camada_fluxo_dos_onibus,
# }






# st.markdown("### Escolha as camadas:")
# st.sidebar.markdown("### Escolha as camadas")
# selected_layers = [
#     layer
#     for layer_name, layer in TODAS_AS_CAMADAS.items()
#     if True # st.checkbox(layer_name, True)
# ]






# ALL_LAYERS = {
#     "Bike Rentals": pdk.Layer(
#         "HexagonLayer",
#         data=from_data_file("bike_rental_stats.json"),
#         get_position=["lon", "lat"],
#         radius=200,
#         elevation_scale=4,
#         elevation_range=[0, 1000],
#         extruded=True,
#     ),
#     "Bart Stop Exits": pdk.Layer(
#         "ScatterplotLayer",
#         data=from_data_file("bart_stop_stats.json"),
#         get_position=["lon", "lat"],
#         get_color=[200, 30, 0, 160],
#         get_radius="[exits]",
#         radius_scale=0.05,
#     ),
#     "Bart Stop Names": pdk.Layer(
#         "TextLayer",
#         data=from_data_file("bart_stop_stats.json"),
#         get_position=["lon", "lat"],
#         get_text="name",
#         get_color=[0, 0, 0, 200],
#         get_size=10,
#         get_alignment_baseline="'bottom'",
#     ),
#     "Fluxo de Saída": pdk.Layer(
#         "ArcLayer",
#         data=from_data_file("bart_path_stats.json"),
#         get_source_position=["lon", "lat"],
#         get_target_position=["lon2", "lat2"],
#         get_source_color=[200, 30, 0, 160],
#         get_target_color=[200, 30, 0, 160],
#         auto_highlight=True,
#         width_scale=0.0001,
#         get_width="outbound",
#         width_min_pixels=3,
#         width_max_pixels=30,
#     ),
# }


