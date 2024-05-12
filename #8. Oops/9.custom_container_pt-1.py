######################### custom contaier part - 1 ###########################

# creating a custom container

from typing import Any


class BookmarkedPage:
    def __init__(self):
        self.bookmarks = {}

    def add(self, bookmark):
        self.bookmarks[bookmark] = self.bookmarks.get(bookmark, 0)+1


target_book_mark = BookmarkedPage()

target_book_mark.add("python")
target_book_mark.add("python")
target_book_mark.add("python")
target_book_mark.add("python")
target_book_mark.add("python")

print("output")
print(target_book_mark.bookmarks)

# handling corner cases


class BookmarkedPages:
    def __init__(self):
        self.bookmarks = {}

    def add(self, bookmark):
        self.bookmarks[bookmark.lower()] = self.bookmarks.get(bookmark, 0) + 1


target_book_mark = BookmarkedPage()

target_book_mark.add("python")
target_book_mark.add("python")
target_book_mark.add("Python")
target_book_mark.add("python")
target_book_mark.add("python")

print("output handling corner cases")
print(target_book_mark.bookmarks)

# getting the count of a key


class BookmarkedPages:
    def __init__(self):
        self.bookmarks = {}

    def add(self, bookmark):
        self.bookmarks[bookmark.lower()] = self.bookmarks.get(
            bookmark.lower(), 0) + 1

    def __getattribute__(self, bookmark):
        return self.bookmarks.get(bookmark.lower(), 0)


target_book_mark = BookmarkedPage()

target_book_mark.add("python")
target_book_mark.add("python")
target_book_mark.add("Python")
target_book_mark.add("python")
target_book_mark.add("python")

print("get the count of a key")
print(target_book_mark.bookmarks["python"])
