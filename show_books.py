from utils import books

def show():
    # agar koi book nahi hai
    if not books:
        print("No books available in library")
    else:
        print("Available Books:")
        
        # saari books aur unki quantity dikhao
        for book, quantity in books.items():
            print(f"{book} (Quantity: {quantity})")
