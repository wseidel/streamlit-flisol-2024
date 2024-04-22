---
theme: gaia
_class: lead
paginate: true
backgroundColor: #fff
backgroundImage: url('https://marp.app/assets/hero-background.svg')
marp: true
---




# Protótipo
- O que significa **protótipo** ?
  - do grego  prótos (primeiro); 
  - typos (tipo)

- **Prototipação** é o processo de criação de um protótipo

- **Objetivos**:
  - POC (Prova de Conceito)
  - MVP (Mínimo Produto Viável)


---

### Ainda sobre protótipo:
- A ideia é que com a utilização do protótipo, possamos obter mais feedback e insights para alcançar o objetivo do produto final.
- Podemos pensar nele como sendo um esboço, um rascunho da ideia, e que nos permite testar e validar conceitos antes de investir mais tempo e recursos no desenvolvimento completo.

---
# Streamlit


---
### Preparando ambiente 

```bash
# Criando o ambiente virtual
$ pyenv virtualenv streamlit_hello

# Ativando o ambiente virtual
$ pyenv activate streamlit_hello
```

---
<!-- slide -->
## Instalando o Streamlit

```shell
$ pip install streamlit   #  OU pip install -r requirements.txt
```


#### Curiosidade: Quais pacotes foram instalados como dependencias do Streamlit? 
```shell
$ pip freeze > requirements-freeze.txt
```

--- 
<!-- slide -->
### Testando a  instalação
```shel 
$ streamlit           
Usage: streamlit [OPTIONS] COMMAND [ARGS]...

  Try out a demo with:

      $ streamlit hello

  Or use the line below to run your own script:

      $ streamlit run your_script.py

Options:
  --log_level [error|warning|info|debug]
  --version                       Show the version and exit.
  --help                          Show this message and exit.

Commands:
  activate  Activate Streamlit by entering your email.
  cache     Manage the Streamlit cache.
  config    Manage Streamlit's config settings.
  docs      Show help in browser.
  hello     Runs the Hello World script.
  help      Print this help message.
  run       Run a Python script, piping stderr to Streamlit.
  version   Print Streamlit's version number.
```

--- 
<!-- slide -->
### Executando o *hello* do Streamlit
```shel 
$ streamlit hello
  Welcome to Streamlit. Check out our demo in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.0.41:8501

  Ready to create your own Python apps super quickly?
  Head over to https://docs.streamlit.io

  May you create awesome apps!

```

--- 
<!-- slide -->
![bg 80%](assets/img/hello.png)



--- 
<!-- slide -->
```shel 
$ git clone https://github.com/streamlit/streamlit-hello
```






---
# Referências:
- [Modelo de Dados: Entendendo e “re-”construindo - Wesley Seidel](https://pt.slideshare.net/wesleyseidel/open-data-imastersv02)
- [Open Source Data Science - Márcio Júnior](https://pt.slideshare.net/ambientelivre/open-source-data-science-elaborando-uma-plataforma-de-big-data-analytics-100-open-source-com-apoio-do-pentaho)