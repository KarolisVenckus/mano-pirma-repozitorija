import PySimpleGUI as sg
from backend import *

# Fetch all books from the database
books = session.query(Book).all()

# Fetch all categories from the database
categories = session.query(Category).all()

# Define the layout
layout = [
    [sg.Text('Manage Books and Authors', font=('Helvetica', 20), justification='center')],
    [sg.Text('Book Title'), sg.Input(key='-TITLE-')],
    [sg.Text('Author Name'), sg.Input(key='-AUTHOR-')],
    [sg.Text('Category'), sg.Combo(values=[category.name for category in categories], key='-CATEGORY-', enable_events=True)],
    [sg.Button('Add Book'), sg.Button('Clear Fields')],
    [sg.Text('_' * 50)],
    [sg.Text('Search: '), sg.Input(key='-SEARCH_INPUT-'), sg.Button('Search')],
    [sg.Table(values=[[book.title, book.author.name, ", ".join([category.name for category in book.categories])] for book in books], headings=['Title', 'Author', 'Categories'], key='-BOOK_TABLE-', justification='left', enable_events=True, auto_size_columns=False, col_widths=[30, 20, 40])],
    [sg.Text('_' * 50)],
    [sg.Button('Delete Book'), sg.Button('Exit')]
]

# Create the window
window = sg.Window('Book Manager', layout, size=(600, 475))

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    elif event == 'Add Book':
        title = values['-TITLE-'].strip()
        author = values['-AUTHOR-'].strip()
        category_name = values['-CATEGORY-']

        if title and author and category_name:
            # Add the book to the database
            author_obj = Author(name=author)
            book_obj = Book(title=title, author=author_obj)
            
            # Fetch or create the category
            category = session.query(Category).filter_by(name=category_name).first()
            if not category:
                category = Category(name=category_name)
            
            book_obj.categories.append(category)
            
            session.add(author_obj)
            session.add(book_obj)
            session.commit()

            # Fetch all books from the database
            books = session.query(Book).all()

            # Update the table values
            window['-BOOK_TABLE-'].update(values=[[book.title, book.author.name, ", ".join([category.name for category in book.categories])] for book in books])

            # Clear the input fields
            window['-TITLE-'].update('')
            window['-AUTHOR-'].update('')
            window['-CATEGORY-'].update('')

    elif event == 'Clear Fields':
        window['-TITLE-'].update('')
        window['-AUTHOR-'].update('')
        window['-CATEGORY-'].update('')

    elif event == 'Delete Book':
        selected_rows = values['-BOOK_TABLE-']

        if selected_rows:
            for row in selected_rows:
                book = session.query(Book).get(row + 1)
                session.delete(book)
            session.commit()

            # Fetch all books from the database
            books = session.query(Book).all()

            # Update the table values
            window['-BOOK_TABLE-'].update(values=[[book.title, book.author.name, ", ".join([category.name for category in book.categories])] for book in books])

    elif event == 'Search':
        search_term = values['-SEARCH_INPUT-'].strip()

        if search_term:
            # Search for books or authors matching the search term
            matching_books = session.query(Book).filter(Book.title.ilike(f'%{search_term}%')).all()
            matching_authors = session.query(Author).filter(Author.name.ilike(f'%{search_term}%')).all()
            matching_categories = session.query(Category).filter(Category.name.ilike(f'%{search_term}%')).all()

            # Combine the matching books, authors, and categories into a single list
            search_results = [[book.title, book.author.name, ", ".join([category.name for category in book.categories])] for book in matching_books]
            search_results += [[book.title, book.author.name, ", ".join([category.name for category in book.categories])] for author in matching_authors for book in author.books]
            search_results += [[book.title, book.author.name, ", ".join([category.name for category in book.categories])] for category in matching_categories for book in category.books]

            # Update the table values with the search results
            window['-BOOK_TABLE-'].update(values=search_results)

        else:
            # Fetch all books from the database
            books = session.query(Book).all()

            # Update the table values
            window['-BOOK_TABLE-'].update(values=[[book.title, book.author.name, ", ".join([category.name for category in book.categories])] for book in books])

window.close()