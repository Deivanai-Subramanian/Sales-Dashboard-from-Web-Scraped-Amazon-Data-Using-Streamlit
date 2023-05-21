import streamlit as st
from streamlit_login_auth_ui.widgets import __login__

__login__obj = __login__(auth_token = "pk_prod_27GNYP246PME2HPJZEV7FX35XRX5", 
                    company_name = "Team Tech Aspirants",
                    width = 200, height = 250, 
                    logout_button_name = 'Logout', hide_menu_bool = False, 
                    hide_footer_bool = False, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:

    st.markdown("Your Streamlit Application Begins here!")


if st.session_state['LOGGED_IN'] == True:
	st.write("WELCOME!")