##streamlit

import streamlit as st
import time
import random
from st_pages import hide_pages
from recipes import Recipes

#round image croners
#add browsing menu
#add hovering infos
#add color and italic and bold to text
#add hub
#add page icon
#add page title
#scapre web to get ingredients image?
#add back to to of the page button?
#cache stuff?
#fix same-name recipes
#don't load every page at once
#add favorites selection
#add logo

#Recipes at https://frosch.cosy.sbg.ac.at/datasets/json/recipes/-/blob/main/recipes.json?ref_type=heads
#betterfood

st.set_page_config(initial_sidebar_state="collapsed")

hide_pages(["test_page","main"])

if "recipes_initialized" not in st.session_state:
    Recipes.init("files/recipes.json")
    st.session_state.recipes=Recipes.recipes
    st.session_state.recipes_initialized=True

if "base_query" not in st.session_state:
    st.session_state.base_query=random.choice(("Salmon?","Pork?","Pasta?","Potato dish?"))

def process(text):

    results=Recipes.search(text)

    st.text(f"{len(results)} result{'s' if len(results)!=1 else ''}.")
    st.session_state.links=[]

    for name,file_name in results:

        st.image(f"files/images/{file_name}",caption=None,width=500)

        st.session_state.links.append(st.page_link(f"pages/{file_name.replace('.jpg','.py')}",label=name))
        st.text("")
        st.text("")

st.sidebar.link_button("Github Repo","https://www.youtube.com/watch?v=dQw4w9WgXcQ")
st.title("Over 1 600 recipes to choose from.")

for i in range(2):
    text=st.text("")

with st.form(key="my_form"):

    textinput=st.text_input(label="Enter some text",value=st.session_state.base_query,max_chars=256)
    submit_button=st.form_submit_button("Search.")

    if submit_button:
        process(textinput)

for i in range(13):
    text=st.text("")

st.text("© YknotTYD 2024")