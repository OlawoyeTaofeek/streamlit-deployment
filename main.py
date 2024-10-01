import streamlit as st
from form import form_code
from home import home_page
from blog import blog_page
import time

        
# Add a sidebar for navigation
with st.sidebar:
    # st.title("Navigation")
    page = st.selectbox("Go to", ["Home", "Blogs", "Contact"])

# Content for each page based on navigation
if page == "Home":
    home_page()
    st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
elif page == "Blogs":
    blog_page()
    st.color_picker('Choose your favorite color')
elif page == "Contact":
    form_code()
    st.balloons()  # Celebration balloons
    st.progress(10)  # Progress bar
    with st.spinner('Wait for it...'):
        time.sleep(10)  # Simulating a process delay
        
st.success("You did it!")
st.error("Error occurred")
st.warning("This is a warning")
st.info("It's easy to build a Streamlit app")
st.exception(RuntimeError("RuntimeError exception"))


# Expander widget acting like a dropdown
with st.expander("What is this dropdown for?"):
    st.write("""
        This dropdown explains the purpose of this section. 
        You can use it to provide detailed information or context to users, 
        while keeping the interface clean by hiding the explanation under a collapsible section.
    """)