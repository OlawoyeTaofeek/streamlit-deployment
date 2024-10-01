# Advanced for Forms in streamlit

import streamlit as st       
from streamlit_option_menu import option_menu
def form_code():
    
    st.header("Contact: Get In Touch with Me!")
    # For the contact form, I will be using formsubmit

    contact_form = """
    <form action="https://formsubmit.co/habephe21@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Get in Touch with me: Your message"></textarea>
        <button type="submit">Send</button>
    </form>
    """


    st.markdown(contact_form, unsafe_allow_html=True)

    # Line separator before footer
    st.markdown('<div class="main-footer-separator"></div>', unsafe_allow_html=True)

    # Footer HTML
    footer = """
    <div class="footer">
        <p>© 2024 Your Name | Connect with me: 
            <a href="https://www.linkedin.com/in/yourprofile" target="_blank">LinkedIn</a> |
            <a href="https://github.com/yourprofile" target="_blank">GitHub</a> |
            <a href="https://twitter.com/yourprofile" target="_blank">Twitter</a>
        </p>
    </div>
    """

    # Display the footer
    st.markdown(footer, unsafe_allow_html=True)

    # Function to load local CSS
    def local_css(filename):
        with open(filename) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Load custom CSS
    local_css("project/style/style.css")












