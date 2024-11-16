import streamlit as st

############################ Page setup #######################

# Set up the page
st.set_page_config(
    page_title="EV Adoption Tracker",
    layout="centered", # or wide
    page_icon="🚗", # choose your favorite icon
    initial_sidebar_state="collapsed" # or expanded
)

####################### Application #########################

#USER INPUT
st.title ("What is your superhero name?")


favorite_color = st.text_input('Enter favorite color')
st.text(f'my favorite color is{favorite_color}')

number= st.number_input('add number')
st.number_input(f'the number is {number}')

superpower= st.selectbox('choose your superpower:', ['Flying', 'Invisibility', 'Time Travel'])

if st.button('My superhero name'):
    superhero_name= f"{favorite_color} of {number}"
    st.header(f'your superhero name: {superhero_name}')
    st.write(f'🦹‍♀️superpower: {superpower}')

    # Display motto
    st.subheader('your super hero motto: ')
    st.write(f'with great superhero comes {superpower.lower()}')
    