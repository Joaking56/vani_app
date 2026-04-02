from supabase import create_client
import streamlit as st

url = st.secrets["SUPABASE_URL"]
key = st.secrets["SUPABASE_KEY"]

client = create_client(url, key)