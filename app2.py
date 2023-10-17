import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["About me","Projects"],
        icons= ["book","boxes"],
        menu_icon = "aspect-ratio",
        default_index=0
    )
if selected == "About me":
    st.title(f"{selected}")
    st.subheader("Background")
    st.write(
    """
    My name is David Garcia. I'm an undergraduate Computer Science B.S. Major
    and am apart of the University of California Santa Cruz's class of 2026.
    I've grown up in a single parent household for most of my life as a first
    generation Latino. 
    """
    )
    st.subheader("Classes I've taken related to Computer Science")
    st.write("""
    - grade: A+ , Beginning Python: CSE 20
    - grade: A- , Computer Systems/ Assembly Language: CSE 12
    - grade: B , Programming Abstractions Python: CSE 30
    """)
    st.subheader("Current Club enrollment")
    st.write("""
    - SlugCP (Slug Competitive Programming Club)
    - UCSC Muay Thai
    - Slug Security (CyberSecurity CLub at UCSC)
    """)
if selected == "Projects":
    st.title(f"{selected}")
    st.subheader(" - (solo project) This website :)")
    st.write("""
    I made this website as a personal project to help keep track of any clubs classes or things I've done
    related to programming or the study of computers in general. It's like a journal of sorts.
    """)
    st.subheader(" - (solo project) Calculator I made with interactive GUI using Binary Tree via GitHub Link")
    st.write("""github link: [here](https://github.com/david04g/python-calculator)""")
