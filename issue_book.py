from utils import books, issued_books
from datetime import datetime

def issue():
    book_name = input("Enter book name: ").strip().upper()
    
    # check karo book available hai ya nhi
    if book_name in books and books[book_name] > 0:
        student = input("Enter student name: ").strip()
        
        # kitne din ke liye issue karvani hai
        days = int(input("For how many days: "))
        
        issue_date = datetime.now() # current date store
        
        # issued book ka record store karo
        issued_books[book_name] = {
            "student": student,
            "days": days,
            "issue_date": issue_date
        }
        
        # available books me se ek kam karo
        books[book_name] -= 1
        
        print(f"Book issued to {student} for {days} days")
        print("Late return par fine lagega")
        
    else:
        print("Book not available")
