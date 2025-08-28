books = [
    {
        "name": "Pán prstenů: Společenstvo prstenu",
        "price": 500,
        "author": "J.R.R. Tolkien",
        "publication_year": 1954,
    }
]

# 1: Přidej do proměnné 'books' 2 libovolné knihy, údaje mohou být libovolné. Vypiš list.

books.append({"name":"Farma zvířat", "price": 300, "author": "George Orwell", "publication_year": 1945})
books.append({"name":"Vesmírná odysea", "price": 400, "author": "Arthur C. Clarke", "publication_year": 1984})
print(books)

# 2. Změň cenu jedné libovolné knihy. Vypiš list.

books[2]["price"] = 600
print(books)

# 3. Odstraň nějakou knihu. Vypiš list.

books.remove(books[0])
print(books)

# 4. Vypiš celkový počet knih v listu.

books_amount = len(books)
print(books_amount)

# Bonusový úkol (dobrovolné): Přidej 1 knihu pomocí uživatelského vstupu (https://www.w3schools.com/python/ref_func_input.asp)

book_name = input("Enter book name: ")
book_price = input("Enter book price: ")
book_author = input("Enter book author: ")
book_publication_year = input("Enter book publication year: ")
books.append({"name":book_name, "price":book_price, "author":book_author, "publication_year":book_publication_year})
print(books)