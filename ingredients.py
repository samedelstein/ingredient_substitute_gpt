import streamlit as st
import pandas as pd
import datetime
import openai

st.header(':knife_fork_plate:  :orange[Substituted Ingredients]')


openai.api_key = 'OPEN-AI-KEY'
st.sidebar.header(':fork_and_knife: :blue[Add Your Ingredients Here]')

options = st.sidebar.multiselect(
    'What dietary restrictions do you have?',
    ['lactose intolerance', 'vegan', 'vegetarian', 'kosher', 'keto', 'low carb', 'pescatarian', 'gluten free'])
options_string = ', '.join(options) 
data = st.sidebar.text_area("Paste Your Ingredients")
button=st.sidebar.button('Generate Substitutions')

if (button==True):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant that converts recipes"},
            {"role": "user", "content": 'based on the following ingredient list,  please substitute the ingredients below with ' + options_string + ' friendly ingredients. Create an html table with one column as the original ingredient another column with the substitute ingredient, and a final column with the reason this subsitution is best. Please include the amounts and recommend appropriate amounts: '+ data}

        ]
    )
    recipe_name = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant that converts recipes"},
            {"role": "user", "content": 'based on the following ingredient list,  name this dish: '+ data}

        ]
    )
    st.write(recipe_name["choices"][0]["message"]["content"])

    st.write(response["choices"][0]["message"]["content"])
