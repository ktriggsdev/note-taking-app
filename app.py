import streamlit as st
import os

st.title("Notion.io")

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

# Download button
if st.button("Download Notes"):
    # Download notes from the file
    with open("notes.txt", "r") as file:
        for i, note in enumerate(file.readlines()):
            st.write(f"{i + 1}. {note.strip()}")

# Upload button
if st.button("Upload Notes"):
    # Clear notes list
    notes = []

    # Upload notes from a file
    uploaded_file = st.file_uploader("Upload a file containing notes (one note per line)")
    if uploaded_file is not None:
        with open(uploaded_file, "r") as file:
            for line in file:
                notes.append(line.strip())

        st.write("Notes uploaded successfully!")
        st.write("Notes:")
        for i, note in enumerate(notes):
            st.write(f"{i + 1}. {note}")
