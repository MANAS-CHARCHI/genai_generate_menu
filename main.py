import streamlit as st
import langchain_helper
st.title("Restaurant Menu Generation.")

cuisine=st.sidebar.selectbox("Pick a cuisine", ["Italian", "Chinese", "Indian", "Japanese", "Mexican", "Russian", "Pakistani"])

if cuisine:
    response=langchain_helper.generate_restaurant_menu_with_name_and_item(cuisine)
    st.header(response['restaurant_name'])
    menu_item=response['menu_items']
    st.write("Menu Items:")
    for item in menu_item:
        st.write("-",item)