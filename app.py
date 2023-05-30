import streamlit as st

st.title("Note.io")

notes = []

# Input text for the note
note_text = st.text_input("Enter your note text:")

# Button to save the note
if st.button("Save Note"):
    # Save the note to a list
    notes.append(note_text)
    # Save notes to a file
    with open("notes.txt", "w") as file:
        for note in notes:
            file.write(f"{note}\n")
    st.success("Note saved successfully!")
    st.write("Notes:")
    
    for i, note in enumerate(notes):
        st.write(f"{i + 1}. {note}")
        
    # Read notes from the file
    with open("notes.txt", "r") as file:
        for i, note in enumerate(file.readlines()):
            st.write(f"{i + 1}. {note.strip()}")
