import sys
import streamlit as st 
from scrap import *
import base64
import json

download_button =  False 
###########################################

def intro():
        page_icon = "https://user-images.githubusercontent.com/46791116/131223695-94935528-312a-4448-8b3c-a4678b4239d5.png"
        description = f"""
        <div align='center'>
        <img src={page_icon}
        width="100" height="100">

        # ⏬ Data Scrapper ⏬
        </div>

        [![GitHub](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://www.linkedin.com/in/adnane-driouche-275763177/)

        ---
        """
        st.write(description, unsafe_allow_html=True)

def print_center(text):
    description = f"""
        <div align='center'>

        # {text}
        </div>

        

        ---
        """
    st.write(description, unsafe_allow_html=True)
#############################################


def download_as_json(dic,output_name):
    print('Done')
    with open(output_name, 'w') as outfile:
        json.dump(dic, outfile)

#===========================================#
#              Streamlit Code               #
#===========================================#
# desc = "Uses an LSTM neural network trained on *The Lord of the Rings*. Check out the code [here](https://github.com/christian-doucette/tolkein_text)!"

intro()
site = st.selectbox('🏗️ Choose The web site', ['Avito','Mubawab','Sarouty'])
user_input = st.text_input('🏗️ Paste the url:')
scrap_button = st.button('Scrap')
st.write('---')

if user_input :

    if site == 'Avito':
        output_file = 'avito.json'
        out = avito(user_input)
    elif site == 'Mubawab' :
        output_file = 'mubawab.json'
        out = mubawab(user_input)
    else:
        output_file = 'sarouty.json'
        out = sarouty(user_input)

if scrap_button:
    
    
    print_center("✅ Data was scrapped successfully ✅")
    # st.title('✅ Data was scrapped successfully ✅') 
    st.write(out)
    out = json.dump(out, sys.stdout)
    b64 = base64.b64encode(out)
    desc = f'<a href="data:file/json;base64,{b64}" download="myfilename.json">Download json file</a>'
    st.write(desc, unsafe_allow_html=True)
    # with open(output_file, 'w') as outfile:
    #         json.dump(out, outfile)
    st.write('---')