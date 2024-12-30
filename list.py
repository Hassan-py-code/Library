

# Creat the library

# Step 1: creat setup
list_book=[]
list_book_future=[]

# Step 2:Adding individual books
name_book=input('Enter the name a book you own:')
another_book=input("Enter the name of another book you own(or press 'Enter' o skip):")

list_book.append(name_book)


if another_book:
    list_book.append(another_book)
    
print(f"you library is {list_book}")


# Step 3: Managing the Wishlist
future_book=input('Enter the name of a book you wish to have in the futuer:')

list_book_future.append(future_book)

another_book_future=input('Enter the name of another book you wish to have(or "enter to skip"):')

if another_book_future:
    list_book_future.append(another_book_future)


print(f"Your Wishlist: {list_book_future}")


# Step 4: Merging Wishlist into library
Wishlist=input("Enter the name of a book from your wishlist that you've acquired (or press 'Enter to skip') : ")

if Wishlist in list_book_future:

    list_book_future.remove(Wishlist)
    list_book.append(Wishlist)
   
print(f"Update library:{list_book}")
print(f"update wishlist {list_book_future}")


# Step 5: Donating books 
book_wishlist=input('Enter  the name of a book from your library you wish:')

if book_wishlist in list_book:
    list_book.remove(book_wishlist)


print(f"Final library is {list_book}")


