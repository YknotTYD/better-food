##test_page

import streamlit as st
import time
import unidecode
from st_pages import hide_pages
from recipes import Recipes

#reduce distance between ingredients
#put name on top
#put name in brightest average color of image

if "recipes" not in st.session_state:
    Recipes.init("files/recipes.json")
    st.session_state.recipes=Recipes.recipes

name="Carrot & star anise purée"
recipe=[i for i in st.session_state.recipes if i["Name"]==name][0] #else notFoundError

file_name=unidecode.unidecode("".join([char if char.isalpha() else " " for char in name]).lower()).split()
file_name="_".join(file_name)+".jpg"

st.set_page_config(initial_sidebar_state="collapsed")

hide_pages(["test_page","main"])

st.sidebar.link_button("Github Repo","https://www.youtube.com")
st.title(f"{name}")

for i in range(4):
    st.text("")

c1,c2=st.columns(2)

with c1:
    st.image(f"files/images/{file_name}",width=350)

for i in range(3):
    st.text("")

def slim(text,limit):

    aquadesc=""
    loops=0

    while text:

        n=0
        loops+=1

        if loops>=1e+5:
            break

        if len(text)>=limit:

            while len(" ".join(text.split(" ")[:n]))<=limit:

                n+=1
                loops+=1

                if loops>=1e+5:
                    break

            n=n-1

            aquadesc+=" ".join(text.split(" ")[:n])+"\n"
            text=" ".join(text.split(" ")[n:])

        else:
            aquadesc+=text
            break

    return(aquadesc)

description=recipe["Description"]

if description:
    if description[-1] not in ".!?;,":
        description+="."

    with c2:
        st.markdown(f"<h4>{slim(description,36)}</h4>",unsafe_allow_html=True)

with st.expander(":red[Ingredients]",expanded=True):

    st.markdown("<h2>Ingredients:</h2>",unsafe_allow_html=True)
    st.text("")

    for i,ing in enumerate(recipe["Ingredients"]):

        ing=list(ing)
        ing[0]=ing[0].upper()
        ing="".join(ing)

        endl=(';' if i<len(recipe['Ingredients'])-1 else ".")

        st.markdown(f"<p style='padding-left: 36px'>-{ing}{endl}</p>",unsafe_allow_html=True)

    st.text("")

with st.expander(":red[Recipe]",expanded=True):

    st.subheader("Recipe:")

    for i,step in enumerate(recipe["Method"]):
        st.markdown(f"<h4 style='padding-left: 36px'>{i+1}):</h4>",unsafe_allow_html=True)
        st.markdown(f"<p style='padding-left: 72px'>{step}</p>",unsafe_allow_html=True)

    st.text("")

for i in range(10):
    st.text("")

st.page_link("main.py",label="Back.")

for i in range(3):
    st.text("")

st.text("© YknotTYD 2024")