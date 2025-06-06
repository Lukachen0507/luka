import streamlit as st
import os
def resume_page():
    # PDF DownloadAdd commentMore actions
    if os.path.exists("static/docs/CV.pdf"):
        with open("static/docs/CV.pdf", "rb") as pdf_file:
        with open("static/docs/resume.pdf", "rb") as pdf_file:
            btn = st.download_button(
                label="Download Resume",
                data=pdf_file,
                file_name="Chen_Xi_CV.pdf",
                file_name="resume.pdf",
                mime="application/octet-stream"
            )
    else:
        st.warning("Resume PDF not found")
        
    st.markdown("## Chen Xi - Resume")
    st.markdown("""
    ### Contact Information  
    - **Email**: lukachen0507@foxmail.com  
    - **Phone**: 86-13168058499 / 852-63985845  
    - **LinkedIn**: [www.linkedin.com/in/lukachen0507](https://www.linkedin.com/in/lukachen0507)  
    - **Location**: Hong Kong / Shenzhen  

    ### Professional Summary  
    Recent Master's graduate in Marketing from The Chinese University of Hong Kong, specializing in Big Data Marketing. Skilled in Python, R, and SPSS for quantitative marketing research, with experience in internships at Deloitte and Shenzhen Finance Institute. Passionate about data-driven marketing strategies.

    ### Education  
    - **Master of Science in Marketing**: The Chinese University of Hong Kong (2024.08 - 2025.10)  
    - **Bachelor of Management in Marketing**: Shenzhen University (2020.09 - 2024.07, GPA: 3.28/4.5)  
    - **Academic Exchange**: University of Toronto (2022.09 - 2022.12)  

    ### Skills  
    - **Quantitative Marketing**: IBM SPSS, R, Python  
    - **MS Office**: Excel, Word, PowerPoint, Outlook  
    - **Languages**: Native Chinese, Fluent English and Cantonese  
    - **Soft Skills**: Communication, Presentation, Multi-Project Management, Client Coordination  

    ### Internships  
    - **Deloitte Enterprise Consulting Shanghai Ltd., Shenzhen Branch**: Intern, Chief Growth Office (2024.03 - 2024.06)  
    - **Shenzhen Finance Institute, CUHK Shenzhen**: Marketing Intern (2023.06 - 2023.08)  

    ### Academic Projects  
    - **IMC Campaign Design for Patagonia**: Developed an integrated marketing campaign (2024.12 - 2025.02)  
    - **Sentiment Analysis for Mandarin Oriental Hotel**: Analyzed OTA comments using Python (2024.09 - 2024.11)  
    - **Undergraduate Thesis**: Studied co-branding impact on Gen Z consumers using SPSS (2024.01 - 2024.05)  
    """)
