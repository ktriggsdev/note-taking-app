import streamlit as st

st.title("Note.io")

# Input text for the note
note_text = st.text_input("Enter your note text:")

# Button to save the note
if st.button("Save Note"):
    # Save the note to a list
    notes.append(note_text)
    st.success("Note saved successfully!")
    st.write("Notes:")
    
    for i, note in enumerate(notes):
        st.write(f"{i + 1}. {note}")
