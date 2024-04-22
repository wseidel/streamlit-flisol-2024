import streamlit as st

st.set_page_config(
    page_title="Minimalista",
    page_icon="👋",
)

st.title("Apresentação Minimalista.")

st.write("Minimanlista...")

import streamlit.components.v1 as components




# embed streamlit docs in a streamlit app
components.iframe("https://intelidados.com.br", width=600, height=900, scrolling=True)
st.markdown("[![Click me](app/static/assets/img/balanco01.jpg)](https://intelidados.com.br)")

# >>> import plotly.express as px
# >>> fig = px.box(range(10))
# >>> fig.write_html('test.html')

# st.header("test html import")

# HtmlFile = open("apresentacao/00-anotacoes.md", 'r', encoding='utf-8')
# source_code = HtmlFile.read() 
# print(source_code)
# # components.html(source_code, height = 600)
# st.markdown(source_code)

