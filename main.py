import langchain_helper as langchain_helper
import streamlit as st

st.title("Pet Name Generator")
animal_type = st.sidebar.selectbox("What is your pet's type?", ["dog", "cat", "fish", "cow", "bird", "hen", "hamster"])
pet_color = ""
if animal_type == "cat":
    pet_color = st.sidebar.text_area(label="What is your cat's color?", max_chars=15)

if pet_color:
    # Generate and print the pet name
    response = langchain_helper.generate_pet_name(animal_type, pet_color)
    st.write(response['pet_name'])