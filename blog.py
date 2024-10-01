import streamlit as st

def blog_page():
    st.title("My Blog")
    st.header("Latest Articles")

    st.write("""
    Welcome to my blog! Here, you'll find articles on Data Science, Machine Learning, and Software Development.
    Below are some of my latest posts:
    
    - **Understanding Machine Learning Algorithms**
    - **How to Build a Flask Web Application**
    - **Top 10 Data Science Projects for Beginners**
    
    Here's a quick code snippet from one of the articles:
    """)

    # Adding code snippet
    st.code("""
    import numpy as np

    def calculate_mean(arr):
        return np.mean(arr)

    data = [1, 2, 3, 4, 5]
    print(f"Mean of data: {calculate_mean(data)}")
    """, language="python")

if __name__ == "__main__":
    blog_page()
