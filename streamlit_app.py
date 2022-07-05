
import streamlit
import pandas

streamlit.title("My parents new healthy Diner")

streamlit.header("🥣 Breakfast Menu")
streamlit.text("🥗 Omega 3 and Blueberry Oatmeal")
streamlit.text("🐔 Kale, Spinach and Rocket Smoothie")
streamlit.text("🥑🍞 Hard-Boiled Fre-Range Eggs")
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
