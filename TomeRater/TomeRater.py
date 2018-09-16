class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "Your e-mail has been updated."

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        for rating in self.books.values():
            if type(rating) == int:
                total += rating
        return total / len(self.books) # Returns average rating by dividing sum of all ratings by length of dictionary containing all books read

    def __repr__(self):
        return "User: {user}, E-mail: {email}, # of Books Read: {books}".format(user=self.name, email=self.email, books=len(self.books))

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.name:
            self = other_user

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, number):
        self.isbn = number
        return "The book's ISBN has been updated."

    def add_rating(self, rating):
        if 0 <= rating <= 4: # Range of valid ratings
            self.ratings.append(rating)
        else:
            print("Invalid Rating.")

    def get_average_rating(self):
        total = 0
        for rating in self.ratings:
            total += rating
        return total / len(self.ratings) # See same method in User class

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            self = other_book

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return "{title}".format(title=self.title)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self):
        return "List of Users: {users}\n\nList of books read: {books}".format(users=list(self.users.values()), books=list(self.books.keys()))

    def create_book(self, title, isbn):
        book = Book(title, isbn)
        return book

    def create_novel(self, title, author, isbn):
        fiction = Fiction(title, author, isbn)
        return fiction

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = Non_Fiction(title, subject, level, isbn)
        return non_fiction

    def add_book_to_user(self, book, email, rating=None):
        if email in self.users.keys():
            self.users[email].read_book(book, rating)
            if type(rating) == int:
                book.add_rating(rating)
            if book not in self.books:
                self.books[book] = 1
            else:
                self.books[book] += 1
        else:
            print("No user with e-mail {email}".format(email=email))


    def add_user(self, name, email, user_books=None):
        if ("@" in email) and (".com" == email[-4:] or ".edu" == email[-4:] or ".org" == email[-4:]): # Checks if last four letters in e-mail string are valid extensions
            user = User(name, email)
            if email not in self.users.keys():
                self.users[email] = user
                if user_books != None:
                    for book in user_books:
                        self.add_book_to_user(book, email)
            else:
                print("This user already exists.")
        else:
            print("Sorry, that is not a valid e-mail address. Please try again.")

    def print_catalog(self):
        for book in self.books:
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def get_most_read_book(self):
        most_read = ""
        times_read = 0
        for book in self.books:
            if self.books[book] > times_read:
                most_read = book
                times_read = self.books[book]
            else:
                continue
        return most_read

    def highest_rated_book(self):
        highest = ""
        rating = 0
        for book in self.books:
            if book.get_average_rating() > rating:
                highest = book
                rating = book.get_average_rating()
            else:
                continue
        return highest

    def most_positive_user(self):
        name = ""
        rating = 0
        for user in self.users:
            if self.users[user].get_average_rating() > rating:
                name = self.users[user]
                rating = self.users[user].get_average_rating()
            else:
                continue
        return name

# Book Subclass
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)

# Book Subclass
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return "{title}, a(n) {level} manual on {subject}".format(title=self.title, level=self.level, subject=self.subject)
