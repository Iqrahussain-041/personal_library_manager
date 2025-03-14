import streamlit as st
import pandas as pd
import json
from datetime import datetime
import os

# Initialize session state variables
if 'library' not in st.session_state:
    st.session_state.library = []

def save_library():
    """Save the library to a JSON file"""
    with open('library.json', 'w') as f:
        json.dump(st.session_state.library, f)

def load_library():
    """Load the library from a JSON file"""
    try:
        with open('library.json', 'r') as f:
            st.session_state.library = json.load(f)
    except FileNotFoundError:
        st.session_state.library = []

# Load library when the app starts
if os.path.exists('library.json'):
    load_library()

# Set page config
st.set_page_config(page_title="Personal Library Manager", layout="wide")

# Title and description
st.title("📚 Personal Library Manager")
st.markdown("Manage your personal book collection with ease!")

# Sidebar with options
with st.sidebar:
    st.header("Menu")
    option = st.radio(
        "Choose an action:",
        ["Add a Book", "Remove a Book", "Search Books", "Display All Books", "Statistics"]
    )

# Add a Book
if option == "Add a Book":
    st.header("Add a New Book")
    with st.form("add_book_form"):
        title = st.text_input("Book Title")
        author = st.text_input("Author")
        year = st.number_input("Publication Year", min_value=0, max_value=datetime.now().year, value=2024)
        genre = st.selectbox("Genre", ["Fiction", "Non-Fiction", "Science Fiction", "Mystery", "Romance", "Biography", "Other"])
        read_status = st.checkbox("Have you read this book?")
        
        submitted = st.form_submit_button("Add Book")
        if submitted and title and author:
            new_book = {
                "title": title,
                "author": author,
                "year": int(year),
                "genre": genre,
                "read": read_status
            }
            st.session_state.library.append(new_book)
            save_library()
            st.success("Book added successfully!")
        elif submitted:
            st.error("Please fill in at least the title and author fields.")

# Remove a Book
elif option == "Remove a Book":
    st.header("Remove a Book")
    if not st.session_state.library:
        st.warning("Your library is empty!")
    else:
        book_titles = [book["title"] for book in st.session_state.library]
        book_to_remove = st.selectbox("Select a book to remove:", book_titles)
        if st.button("Remove Book"):
            st.session_state.library = [book for book in st.session_state.library if book["title"] != book_to_remove]
            save_library()
            st.success(f"'{book_to_remove}' has been removed from your library.")

# Search Books
elif option == "Search Books":
    st.header("Search Books")
    search_type = st.radio("Search by:", ["Title", "Author"])
    search_term = st.text_input("Enter search term:")
    
    if search_term:
        if search_type == "Title":
            results = [book for book in st.session_state.library if search_term.lower() in book["title"].lower()]
        else:
            results = [book for book in st.session_state.library if search_term.lower() in book["author"].lower()]
        
        if results:
            st.subheader("Search Results:")
            df = pd.DataFrame(results)
            st.dataframe(df, use_container_width=True)
        else:
            st.info("No books found matching your search.")

# Display All Books
elif option == "Display All Books":
    st.header("Your Library")
    if not st.session_state.library:
        st.warning("Your library is empty!")
    else:
        df = pd.DataFrame(st.session_state.library)
        st.dataframe(df, use_container_width=True)

# Statistics
elif option == "Statistics":
    st.header("Library Statistics")
    if not st.session_state.library:
        st.warning("Your library is empty!")
    else:
        total_books = len(st.session_state.library)
        read_books = len([book for book in st.session_state.library if book["read"]])
        read_percentage = (read_books / total_books) * 100 if total_books > 0 else 0
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Books", total_books)
        with col2:
            st.metric("Books Read", read_books)
        with col3:
            st.metric("Percentage Read", f"{read_percentage:.1f}%")
        
        # Genre distribution
        st.subheader("Genre Distribution")
        genre_counts = pd.DataFrame(st.session_state.library)["genre"].value_counts()
        st.bar_chart(genre_counts)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
