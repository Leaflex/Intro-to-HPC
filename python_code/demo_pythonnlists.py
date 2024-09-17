#!/usr/bin/env python3
# append(), clear(), copy(), count(), extend(), index(), insert(), pop(), remove(), reverse(), sort()

def listAppend():
    list = [1, "abc", 2.1]
    print(f"\n\nappend():\nlist & id before append: {list} {id(list)}")
    list.append(1.0)
    print(f"list & id after append(1.0): {list} {id(list)}")

def listClear():
    list = [1, "abc", 2.1]
    print(f"\n\nclear():\nlist & id before clear: {list} {id(list)}")
    list.clear()
    print(f"list & id after clear(): {list} {id(list)}")

def listCopy():
    list = [1, "abc", 2.1]
    print(f"\n\ncopy():\nlist & id: {list} {id(list)}")
    list2 = list.copy()
    print(f"list2 & id: {list2} {id(list2)}")

def listCount():
    list = [1, "abc", 2.1, 1]
    print(f"\n\ncount():\nlist & id: {list} {id(list)}")
    print(f"Occurences of `1` in list: {list.count(1)}")

def listExtend():
    list = [1, "abc", 2.1]
    list2 = [2, "def", 2.0]
    print(f"\n\nextend():\nlist & id: {list} {id(list)}\nlist2 & id: {list2} {id(list2)}")
    print(f"list 1 and 2 extended & id: {list.extend(list2)}")

def listIndex():
    list = [1, "abc", 2.1, "abc"]
    print(f"\n\nindex():\nlist & id: {list} {id(list)}")
    print(f"Index of first 'abc' in list: {list.index("abc")}")

def listInsert():
    list = [1, "abc", 2.1]
    print(f"\n\ninsert():\nlist & id: {list} {id(list)}")
    list.insert(1, "inserted")
    print(f"list & id after adding 'inserted' at list[1]: {list} {id(list)}")

def listPop():
    list = [1, "abc", 2.1]
    print(f"\n\npop():\nlist & id: {list} {id(list)}")
    list.pop(1)
    print(f"list & id after popping list[1]: {list} {id(list)}")

def listRemove():
    list = [1, "abc", 2.1, "abc"]
    print(f"\n\nremove():\nlist & id: {list} {id(list)}")
    list.remove("abc")
    print(f"list after removing 'abc': {list} {id(list)}")

def listReverse():
    list = [1, "abc", 2.1]
    print(f"\n\nreverse():\nlist & id: {list} {id(list)}")
    list.reverse()
    print(f"list & id after popping list[1]: {list} {id(list)}")

def listSort():
    list = [2.3, 1.0, 7.6, 3.4, 100.2, 58.6]
    print(f"\n\nsort():\nlist & id: {list} {id(list)}")
    list.sort()
    print(f"list & id after sorting: {list} {id(list)}")

def main():
    listAppend()
    listClear()
    listCopy()
    listCount()
    listExtend()
    listIndex()
    listInsert()
    listPop()
    listRemove()
    listReverse()
    listSort()

if __name__ == "__main__":
    main()
