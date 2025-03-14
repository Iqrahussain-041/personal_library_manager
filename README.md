# Personal Library Manager

A Streamlit-based web application for managing your personal book collection. This application allows you to add, remove, search for books, and view statistics about your library.

## Features

- Add new books with title, author, publication year, genre, and read status
- Remove books from your library
- Search books by title or author
- Display all books in a tabular format
- View library statistics including:
  - Total number of books
  - Number of books read
  - Percentage of books read
  - Genre distribution visualization

## Installation

1. Clone this repository or download the files
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, use the following command in your terminal:
```bash
streamlit run main.py
```

The application will open in your default web browser.

## Data Persistence

The library data is automatically saved to a `library.json` file and loaded when you restart the application.

## Requirements

- Python 3.7 or higher
- Streamlit
- Pandas

## License

This project is open source and available under the MIT License. 