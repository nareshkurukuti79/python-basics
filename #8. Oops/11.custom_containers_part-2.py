############################ Custom Containers Part 3 ################
# Private Members (__ you can use as private member)
# Accessing  a dict from outside
# Blocking a dict access form outside

class BookmarkedPage:
    def __init__(self):
        self.__bookmarks = {}

    def add(self, bookmark):
        self.__bookmarks[bookmark.lower()] = self.__bookmarks.get(
            bookmark.lower(), 0) + 1

    def __getitem__(self, bookmark):
        return self.__bookmarks.get(bookmark.lower(), 0)

    def __setitem__(self, bookmark, count):
        self.__bookmarks[bookmark.lower()] = count

    def __len__(self):
        return len(self.__bookmarks)

    def __iter__(self):
        return iter(self.__bookmarks)


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

print(target_bookmark.__dict__)

print(target_bookmark._BookmarkedPage__bookmarks)
