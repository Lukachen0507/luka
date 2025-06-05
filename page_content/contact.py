import streamlit as st

def contact_page():
    st.markdown("## Contact Me")
    st.markdown("""
    - **Email**: [lukachen0507@foxmail.com](mailto:lukachen0507@foxmail.com)  
    - **Phone**: 86-13168058499 / 852-63985845  
    - **LinkedIn**: [www.linkedin.com/in/lukachen0507](https://www.linkedin.com/in/lukachen0507)  
    - **Location**: Hong Kong / Shenzhen  
    """)

    st.markdown("---")

    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")
        with col2:
            subject = st.text_input("Subject")
        message = st.text_area("Message", height=150)
        submitted = st.form_submit_button("Send Message")

        if submitted:
            st.success("Thanks for your message! I'll get back to you soon.")
            # In a real app, process form data (e.g., send email or store in database)