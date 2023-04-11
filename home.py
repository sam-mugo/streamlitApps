import streamlit as st


col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        f"""
        <a href="/page1" target="_self" style="text-decoration: none; color: inherit;">
            <div style='padding: 10px; border-style: solid; border-width: 2px; border-color: black; border-radius: 10px'>
                <h3 style='text-align: center; color: black;'>📈 Title 1</h3>
                <p style='text-align: center; color: black;'>Subtitle 1</p>
            </div>
        </a>
        <script defer src="https://use.fontawesome.com/releases/v5.15.4/js/all.js" integrity="sha384-rOA1PnstxnOBLzCLMcre8ybwbTmemjzdNlILg8O7z1lUkLXozs4DHonlDtnE7fpc" crossorigin="anonymous"></script>
        """, unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <a href="/page2" target="_self" style="text-decoration: none; color: inherit;">
            <div style='padding: 10px; border-style: solid; border-width: 2px; border-color: black; border-radius: 10px'>
                <h3 style='text-align: center; color: black;'>👤 Title 2</h3>
                <p style='text-align: center; color: black;'>Subtitle 2</p>
            </div>
        </a>
        """, unsafe_allow_html=True
    )
with col3:
    st.markdown(
        f"""
        <a href="/page3" target="_self" style="text-decoration: none; color: inherit;">
            <div style='padding: 10px; border-style: solid; border-width: 2px; border-color: black; border-radius: 10px'>
                <h3 style='text-align: center; color: black;'>⚙ Title 3</h3>
                <p style='text-align: center; color: black;'>Subtitle 3</p>
            </div>
        </a>
        """, unsafe_allow_html=True
    )



