import streamlit as st
import pandas as pd
from PIL import Image

##############################################################################
##############################################################################
##############################################################################
#opacity_list=['100%','50%','50%','50%','50%']
#init_page=False
#feliperamongarcia

##############################################################################
##############################################################################
##############################################################################
st.set_page_config(page_title="Felipe Ramón García", page_icon="📊🚀", layout="wide")
#
def change_lan(lan):
    st.session_state.lan=lan
    st.rerun()

@st.cache_data
def cargar_imagen(path):
    return Image.open(path)

def get_pdf(path):
    with open(path, "rb") as file:
        pdf_data = file.read()
    return pdf_data

#@st.cache_data
def load_translations(path="translations.csv"):
    df = pd.read_csv(path,sep=';')
    df['es']=df['es'].apply(lambda x:x.replace('\r',''))
    df['en']=df['en'].apply(lambda x:x.replace('\r',''))
    translations=(
        df.groupby('type')[['es','en']]
        .apply(lambda g: g.to_dict(orient='records')[0])
        .to_dict()
    )
    return translations,df

def get_elements_type(translations,kind='project_priv'):
    img_type=[]
    resume_type=[]
    title_type=[]
    proyectos=[]
    init_type="default"
    for type_ in translations.keys():
        if kind in type_:

            if 'init' in type_:
                init_type=type_

            elif 'title' in type_:
                title_type.append(type_)

            elif 'img' in type_:   
                img_type.append(type_)

            elif 'resume' in type_: 
                resume_type.append(type_)

    if img_type==[]:
        img_type=["default"]*len(resume_type)

    for i in range(0,len(resume_type)):
        proyectos.append(        {
            "titulo": translations[title_type[i]][st.session_state.lan],
            "imagen": translations[img_type[i]]['es'],  
            "resumen": translations[resume_type[i]][st.session_state.lan]
        })

    return init_type,proyectos

def funcion_de_inicio():
    global opacity_list
    global init_page
   
    st.session_state.init = True  # Marcar como ejecutado
    opacity_list=['100%','50%','50%','50%','50%']
    init_page=True

translations,df = load_translations()
##############################################################################
#################### SESSION VARIABLES #####################
##############################################################################
if "init" not in st.session_state:
    funcion_de_inicio()

if "light_theme" not in st.session_state:
    st.session_state.light_theme=True

if "lan" not in st.session_state:
    st.session_state.lan='es'

if "category" not in st.session_state:
    st.session_state.category='Inicio'
    opacity_list=['100%','50%','50%','50%','50%']

##############################################################################
######################## STYLES     ###########################################
##############################################################################
st.markdown('<a name="top"></a>', unsafe_allow_html=True)  # en la parte superior

st.markdown("""
    <style>
        div[data-testid="stSidebarHeader"] {
            height: 0%;
            padding: 0;
        }
            
        div[data-testid="stSidebar"] {
            width:270px;
        }  
            
        .stColumn {
            align-content: center;
        }
            
        .stButton {
            display: flex;
            justify-content: center;
        }
            
        div[data-testid="stMarkdownContainer"] {
            text-align: center;
            list-style-position: inside;
        }
            
        button[data-testid="stBaseButton-secondary"]{
            width: 300px;
            height: 40px; 
            opacity:50%;     
            font-weight: bold;    
        }
            
        .stHorizontalBlock{
            justify-content: center;
            }

        .stHeading{
            display: flex;
            justify-content: center;
            padding:0.5rem;
        }
            
        div[data-testid="stVerticalBlock"] > div:nth-child(5){
            display: flex;
            justify-content: center;      
         }
            
    </style>
""", unsafe_allow_html=True)

#language and theme buttons
st.markdown(""" 
    <style>
         div[data-testid="stSidebarUserContent"] > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1){
                flex-direction: row;
                gap: 0;
                justify-content: center;
                    }
            
         div[data-testid="stSidebarUserContent"] > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1) > div:nth-child(2)> div:nth-child(1)> button:nth-child(1){
                width: 125px;
                border-radius: 0px;
                    }   
         div[data-testid="stSidebarUserContent"] > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1) > div:nth-child(1)> div:nth-child(1)> button:nth-child(1){
                width: 125px;
                border-radius: 0px;
                    }    
    </style>
""", unsafe_allow_html=True)

#st.markdown("""
#    <style>
#        div[data-testid="stSidebarUserContent"] > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1){
#                flex-direction: row;
#                gap: 0;
#                justify-content: center;
#                    }
#            
#        div[data-testid="stSidebarUserContent"] > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1) > div:nth-child(2)> div:nth-child(1)> button:nth-child(1){
#                width: 125px;
#                border-radius: 0px;
#                    }   
#        div[data-testid="stSidebarUserContent"] > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1) > div:nth-child(1)> div:nth-child(1)> button:nth-child(1){
#                width: 125px;
#                border-radius: 0px;
#                    }   
#    </style>
#""", unsafe_allow_html=True)


##############################################################################
# SIDEBAR
##############################################################################
side=st.sidebar
side.title(translations['section_nav'][st.session_state.lan])
col1=side.columns(1)

if col1[0].button(translations['section_init'][st.session_state.lan]):
    st.session_state.category = "Inicio"
if col1[0].button(translations['section_about_me'][st.session_state.lan]):
    st.session_state.category = "Sobre mí"
if col1[0].button(translations['section_project_pers'][st.session_state.lan]):
    st.session_state.category = "Proyectos Personales"
if col1[0].button(translations['section_project_priv'][st.session_state.lan]):
    st.session_state.category = "Proyectos Privados"
if col1[0].button(translations['section_contact'][st.session_state.lan]):
    st.session_state.category = "Contacto"


st.sidebar.markdown(
    "<div style='height: 50px;'></div>", unsafe_allow_html=True
)

#st.sidebar.markdown("""
#<div style="display: flex; font-weight: bold;">
#    <form action="?theme=light" method="get" style="flex: 1;">
#        <button style="width: 100%; padding: 8px; background:#f0f0f0; border:1px solid #ccc;">ES</button>
#    </form>
#    <form action="?theme=dark" method="get" style="flex: 1;">
#        <button style="width: 100%; padding: 8px; background:#333; color:white; border:1px solid #666;">EN</button>
#    </form>
#</div>
#""", unsafe_allow_html=True)

col1 = st.sidebar.columns(1)
with col1[0]:
    if st.button("ES", key="lan_es"):
       change_lan('es')
        
    if st.button("EN", key="lan_en"):
        change_lan('en')



st.sidebar.markdown(
    "<div style='height: 25px;'></div>", unsafe_allow_html=True
)


#col1 = st.sidebar.columns(1)
#with col1[0]:
#    if st.button("☀️ Claro", key="light_button"):
#        st.session_state.light_theme=True
#    if st.button("🌙 Oscuro", key="dark_button2"):
#        st.session_state.light_theme=False

#st.sidebar.markdown(
#    "<div style='height: 25px;'></div>", unsafe_allow_html=True
#)

st.sidebar.markdown(f"""
<a href="#top">
    <button style="width: 100%; padding: 8px;">{translations['section_up'][st.session_state.lan]}</button>
</a>
""", unsafe_allow_html=True)
 
st.markdown(""" 
    <style>
        .stButton button:hover {
            opacity: 70%;
            background-color:#F0F2F6;
            
            
        }
    <style>
        .stButton button:active {
            background-color:black;
            
        }
""", unsafe_allow_html=True)

#########################################################################################
##########################  END SIDEBAR           #######################################
#########################################################################################

##############################################################################
# INICIO
##############################################################################

if st.session_state.category=="Inicio":
    opacity_list=['100%','50%','50%','50%','50%']    
    init_page=False


    st.title("📊🚀 Felipe Ramón García - Data Scientist")
    st.markdown("""---""",unsafe_allow_html=True) 

    col1, col2 = st.columns([1, 2]) 
    with col1:
            imagen = cargar_imagen('Img/CV_Felipe_imagen_5.png')
            st.image(imagen, use_container_width =True)
    with col2:
            st.write(translations['first_resume_1'][st.session_state.lan])

##############################################################################
# ABOUT ME
##############################################################################
elif st.session_state.category=="Sobre mí":
    opacity_list=['50%','100%','50%','50%','50%']

    init_type,experiencias=get_elements_type(translations,kind='company')
    _,academic=get_elements_type(translations,kind='academic')

    st.title(translations['section_about_me'][st.session_state.lan])
    #st.write("""
    #Soy un analista de datos con experiencia en proyectos de machine learning, análisis financiero y visualización. 
    #Aquí algunos de mis proyectos destacados:
    #""")
    st.markdown("""---""",unsafe_allow_html=True) 

    ## Mostrar cada bloque
    for i,item in enumerate(experiencias):
        st.subheader(item["titulo"])
        col1, col2 = st.columns([1, 3]) if i % 2 == 0 else st.columns([3, 1])  # col1 con ancho fijo en px, gap="large"

        with col1:
            if i % 2 == 0:
                st.markdown("""<div style="width:300px></div>""",unsafe_allow_html=True)
            else:
                st.write(item["resumen"])

        with col2:
            if i % 2 == 0:
                st.write(item["resumen"])
            else:
                st.markdown("""<div style="width:300px></div>""",unsafe_allow_html=True)

    st.markdown("""---""",unsafe_allow_html=True) 

    # Mostrar cada bloque
    for i,item in enumerate(academic):
        st.subheader(item["titulo"])
        col1, col2 = st.columns([1, 3]) if i % 2 == 0 else st.columns([3, 1])  # col1 con ancho fijo en px, gap="large"

        with col1:
            if i % 2 == 0:
                st.markdown("""<div style="width:300px></div>""",unsafe_allow_html=True)
            else:
                st.write(item["resumen"])

        with col2:
            if i % 2 == 0:
                st.write(item["resumen"])
            else:
                st.markdown("""<div style="width:300px></div>""",unsafe_allow_html=True)

##############################################################################
# PERSONAL PROJECTS
##############################################################################
elif st.session_state.category=="Proyectos Personales":
    opacity_list=['50%','50%','100%','50%','50%']   

    init_type,proyectos=get_elements_type(translations,kind='project_personal')

    st.header(translations['section_project_pers'][st.session_state.lan])
    st.markdown("""---""",unsafe_allow_html=True) 
    st.write(translations[init_type][st.session_state.lan])

    # Mostrar los proyectos con layout alternado
    for i, proyecto in enumerate(proyectos):
        st.subheader(proyecto["titulo"])
        #st.markdown("---")

        col1, col2 = st.columns([2, 3]) if i % 2 == 0 else st.columns([3, 2])

        with col1:
            if i % 2 == 0:
                imagen = cargar_imagen(proyecto["imagen"])
                st.image(imagen, use_container_width =True)
            else:
                st.write(proyecto["resumen"])

        with col2:
            if i % 2 == 0:
                st.write(proyecto["resumen"])
            else:
                imagen = cargar_imagen(proyecto["imagen"])
                st.image(imagen, use_container_width =True)
        


##############################################################################
# PRIVATE PROJECTS
##############################################################################
elif st.session_state.category=="Proyectos Privados":
    opacity_list=['50%','50%','50%','100%','50%']

    init_type,proyectos=get_elements_type(translations,kind='project_priv')

    st.header(translations['section_project_priv'][st.session_state.lan])
    st.markdown("""---""",unsafe_allow_html=True) 
    st.write(translations[init_type][st.session_state.lan])

    # Mostrar los proyectos con layout alternado
    for i, proyecto in enumerate(proyectos):
        st.subheader(proyecto["titulo"])
        #st.markdown("---")

        col1, col2 = st.columns([1, 2]) if i % 2 == 0 else st.columns([2, 1])

        with col1:
            if i % 2 == 0:
                imagen_priv_1 = Image.open(proyecto["imagen"])
                st.image(imagen_priv_1, use_container_width =True)
            else:
                st.write(proyecto["resumen"])

        with col2:
            if i % 2 == 0:
                st.write(proyecto["resumen"])
            else:
                imagen_priv_1 = Image.open(proyecto["imagen"])
                st.image(imagen_priv_1, use_container_width =True)

##############################################################################
# CONTACTS
##############################################################################
elif st.session_state.category=="Contacto":
    opacity_list=['50%','50%','50%','50%','100%']    
    if st.session_state.lan=='es':
        path_cv='Data/CV_Felipe_Ramon_ES.pdf'
        pdf_data=get_pdf(path_cv)
    else:
        path_cv='Data/CV_Felipe_Ramon_EN.pdf'
        pdf_data=get_pdf(path_cv)


    st.header(translations['section_contact'][st.session_state.lan])
    st.markdown("""---""",unsafe_allow_html=True) 
    st.markdown(translations['contact_resume_1'][st.session_state.lan])

    _,col2,_=st.columns(3)

    with col2:
        # Crea el botón de descarga
        st.download_button(
            label=translations['contact_button_1'][st.session_state.lan],
            data=pdf_data,
            file_name="Felipe_Ramon_Garcia_CV.pdf",
            mime="Img"
        )

#####################################################################################
########################        DYNAMIC STYLES     ##################################
#####################################################################################
#change sidebar main buttons
for i in range(1,6):
    style_sidebar_button=f'div[data-testid="stSidebarUserContent"] > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1)> div:nth-child({i})> div:nth-child(1)> button:nth-child(1)'
    opacity=opacity_list[i-1]
    color='black' if opacity=='100%' else 'grey'
    st.markdown(
        f"""
        <style>
        {style_sidebar_button}{{
            opacity: {opacity};
            transition: opacity 0.3s ease;
            border-color:{color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

#change theme
#for i in range(1,3):
#    style_sidebar_button=f'[data-testid="stSidebarUserContent"] > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(6)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1) > div:nth-child({i})> div:nth-child(1)> button:nth-child(1)'
#    opacity= '100%' if ((st.session_state.light_theme and i==1) or (not st.session_state.light_theme and i==2)) else '50%'
#    color='black' if opacity=='100%' else 'grey'
#    st.markdown(
#        f"""
#        <style>
#        {style_sidebar_button}{{
#            opacity: {opacity};
#            transition: opacity 0.5s ease;
#            border-color:{color};
#        }}
#        </style>
#        """,
#        unsafe_allow_html=True
#    )
#feliperamongarcia
#change language
for i in range(1,3):
    style_sidebar_button=f'[data-testid="stSidebarUserContent"] > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1)> div:nth-child(1) > div:nth-child({i})> div:nth-child(1)> button:nth-child(1)'
    opacity= '100%' if ((st.session_state.lan=='es' and i==1) or (not st.session_state.lan=='es' and i==2)) else '50%'
    color='black' if opacity=='100%' else 'grey'
    st.markdown(
        f"""
        <style>
        {style_sidebar_button}{{
            opacity: {opacity};
            transition: opacity 0.5s ease;
            border-color:{color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )