#Build with AI: AI-Powered Dashboards with Streamlit 
#Quick Review: Streamlit Basics for Web Apps

#Import packages
import streamlit as st
from datetime import date, datetime

#Configure page
st.set_page_config(page_title="Streamlit Basics Review",layout="wide")

#Write title and text: flexible - allows us to render text, data frames, visualisations and more.
st.title("Streamlit Basics Review - Vanessa is Here")
st.write("Hello world! - Vanessa is cooking Chinese")

#Gather current date and time: use the date/time func to get the date & time at the moment, and format it with `strftime()` func.
st.write("Current date and time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

#Create button that our users can press to interact with our Streamlit apps. if statement with a `button()`` 
if st.button("Press me!"):
    st.success("Button was pressed!") # A success msg

#Create slider widget: will return whatever the chosen value is selected by the user, and save to variable `age`.
age = st.slider("Your age", 0, 100, 30) # The minium, maxiumn, default values.
st.write(f"You are {age} years old.") # Display value in `age` variable.

#Create text input widget: use when we allow users to talk to the LLM models.
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}!")

#Create checkbox widget: user can check the box and then it can do something.
toggle = st.checkbox("Check for a surprise")
if toggle:
    st.info("Surprise!")

#Create multiselect widget: user to select different options for filtering items.
options = st.multiselect("Choose pizza toppings", ["Cheese", "Pepperoni", "Onions"])
st.write("Toppings:", options) # This func will present a list that user can pick from and it will return a Python list as the result.

#Create sidebar container: a separate section on the left-side on oour app that allows users to do various things in it, i.e. write in different prompts or working with filters later on. 
st.sidebar.title("Sidebar Panel") # Put a title on the sidebar.
#Add selection widget for sidebar
sidebar_option = st.sidebar.selectbox("Select an option:", ["Home", "Settings", "About"])
st.sidebar.write("You chose", sidebar_option)

#Create three column containers: use to organise and display obj such as KPIs. 
col1, col2, col3 = st.columns(3)

#Create temperature container: will show a key num with an optional change indicator. 
with col1:
    st.metric("Temperature", "72°F", "-1.2°F")

#Create wind speed container
with col2:
    st.metric("Wind Speed", "10 mph", "+1.5 mph")

#Create humidity container
with col3:
    st.metric("Humidity", "50%", "-5%")

#Create expander container: allows users to expand or collapse info inside a container. Can place anything inside of it like text, charts or even other widgets.
with st.expander("See more details"):
    st.write("Here are more details... you can put any Streamlit commands inside expanders.")