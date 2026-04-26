from utils import books, issued_books
from datetime import datetime

# fine calculate karne ka function
def calculate_fine(extra_days):
    fine = 0
    
    # har extra din ke liye increasing fine
    for i in range(1, extra_days + 1):
        fine += 10 * i
    
    return fine

def return_book():
    book_name = input("Enter book name: ").strip().upper()
    
    if book_name in issued_books:
        record = issued_books[book_name]
        
        issue_date = record["issue_date"]
        allowed_days = record["days"]
        
        return_date = datetime.now()
        
        # total days calculate karo
        total_days = (return_date - issue_date).days
        
        extra_days = total_days - allowed_days
        
        # agar late hai to fine lagao
        if extra_days > 0:
            fine = calculate_fine(extra_days)
            print(f"Late by {extra_days} days")
            print(f"Fine to pay: Rs {fine}")
        else:
            print("Book returned on time. No fine")
        
        # book wapas add karo
        books[book_name] = books.get(book_name, 0) + 1
        
        # issued list se hatao
        issued_books.pop(book_name)
        
    else:
        print("This book was not issued")
