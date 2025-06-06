import streamlit as st
import os
from PIL import Image

def home_page():
    st.markdown("## Chen Xi")
    st.markdown("""
    ### Recent Master's Graduate in Marketing  
    - **University**: The Chinese University of Hong Kong  
    - **Focus**: Big Data Marketing with Python and R  
    - **Location**: Hong Kong / Shenzhen  
    - **Email**: [lukachen0507@foxmail.com](mailto:lukachen0507@foxmail.com)  
    - **LinkedIn**: [www.linkedin.com/in/lukachen0507](https://www.linkedin.com/in/lukachen0507)  
    """)
        # Profile Image (optional)
    if os.path.exists("static/images/profile.jpg"):
        image = Image.open("static/images/profile.jpg")
        st.image(image, width=200)
    else:
        st.warning("Profile image not found")
    st.markdown("---")

    st.markdown("### About Me")
    st.write("""
    I am a recent Master's graduate in Marketing from The Chinese University of Hong Kong, specializing in Big Data Marketing using Python and R. With a Bachelor's in Management from Shenzhen University (GPA: 3.28/4.5), I have developed strong analytical and marketing skills through internships and academic projects. I am passionate about leveraging data to drive marketing strategies and am eager to contribute to innovative marketing solutions.
    """)

    st.markdown("---")

    st.markdown("### Skills")
    st.write("""
    - **Quantitative Marketing Research & Analysis**: IBM SPSS, R, Python  
    - **MS Office**: Excel, Word, PowerPoint, Outlook  
    - **Languages**: Native Chinese, Fluent English and Cantonese  
    - **Soft Skills**: Communication, Presentation, Multi-Project Management, Client Coordination  
    """)
