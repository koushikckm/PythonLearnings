if __name__=="__main__":
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

    fruits.append('pineapple')
    print(fruits)

    anotherlist = ['aaa','bbb']
    fruits.extend(anotherlist)
    print(fruits)

    fruits.insert(1,'ccc')
    print(fruits)

    fruits.remove('bbb')
    print(fruits)

    fruits.pop(8)
    print(fruits)

    print(fruits.index('apple'))

    print(fruits.count('apple'))

    fruits.sort()
    print(fruits)

    fruits.sort(reverse = True)
    print(fruits)

    fruits.reverse()
    print(fruits)

    copylist = fruits.copy()
    print(copylist)