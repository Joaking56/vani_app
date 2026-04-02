import streamlit as st
from functions import open_wanted_file, write_wanted_file, open_completed_file, write_completed_file
from bg_func import set_background

set_background("img.png")
wanted_items = open_wanted_file()
completed_items = open_completed_file()


def add_wanted():
    wanted = st.session_state["new_wanted"] + "\n"
    if wanted not in wanted_items:
        wanted_items.append(wanted)
        write_wanted_file(wanted_items)
    st.session_state["new_wanted"] = ""


st.title("Közös programok gyüjtőhelye Szerelmemmel ♥♥♥")
st.text_input(label="empty",
              placeholder="Ide írhatod mi jutott eszedbe!",
              label_visibility="hidden",
              on_change=add_wanted,
              key="new_wanted")

for wanted_item in wanted_items:
    clean_item = wanted_item.strip()
    if st.checkbox(clean_item, key=f"wanted_cbox_{clean_item}"):
        wanted_items.remove(wanted_item)
        write_wanted_file(wanted_items)
        completed_items.append(wanted_item)
        write_completed_file(completed_items)
        st.rerun()


st.divider()
st.subheader("Már megcsináltuk:")
for completed_item in completed_items:
    st.markdown(f'<span style="color: hotpink;">♥</span> {completed_item.strip()}', unsafe_allow_html=True)