############################## Custom Containers Part 2 ############################

# Example getting the number of the bookmarks types

from typing import Any


class BookmarkedPage:
    def __init__(self):
        self.bookmarks = {}

    def add(self, bookmark):
        self.bookmarks[bookmark.lower()] = self.bookmarks.get(
            bookmark.lower(), 0) + 1

    def __getitem__(self, bookmark):
        return self.bookmarks.get(bookmark.lower(), 0)

    def __setitem__(self, bookmark, count):
        self.bookmarks[bookmark.lower()] = count

    def __len__(self):
        return len(self.bookmarks)


target_bookmark = BookmarkedPage()

target_bookmark.add("python")
target_bookmark.add("python")
target_bookmark.add("python")
target_bookmark.add("php")
target_bookmark.add("php")
target_bookmark.add("javascript")
target_bookmark.add("react")
target_bookmark.add("java")
target_bookmark.add("angularjs")
target_bookmark.add("angularjs")
target_bookmark.add("typescript")

print("total types of keys and numbers")
print(target_bookmark)
print("total number of keys")
print(len(target_bookmark))


# iterating over the class

class BookmarkedPage:
    def __init__(self):
        self.bookmarks = {}

    def add(self, bookmark):
        self.bookmarks[bookmark.lower()] = self.bookmarks.get(
            bookmark.lower(), 0) + 1

    def __getitem__(self, bookmark):
        return self.bookmarks.get(bookmark.lower(), 0)

    def __setitem__(self, bookmark, count):
        self.bookmarks[bookmark.lower()] = count

    def __len__(self):
        return len(self.bookmarks)

    def __iter__(self):
        return iter(self.bookmarks)


target_bookmark = BookmarkedPage()
target_bookmark.add("python")
target_bookmark.add("python")
target_bookmark.add("python")
target_bookmark.add("php")
target_bookmark.add("php")
target_bookmark.add("javascript")
target_bookmark.add("react")
target_bookmark.add("java")
target_bookmark.add("angularjs")
target_bookmark.add("angularjs")
target_bookmark.add("typescript")

print("total types of keys and numbers")
print(target_bookmark)

for bookmark in target_bookmark:
    print(bookmark)
