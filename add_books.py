from utils import books

def add():
    # user se book ka naam lo
    book_name = input("Enter book name: ").strip().upper()
    
    # agar book already hai to quantity badhao
    if book_name in books:
        books[book_name] += 1
    else:
        # warna nayi entry banao
        books[book_name] = 1
        
    print(f"Book '{book_name}' added successfully")
