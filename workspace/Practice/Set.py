if __name__=="__main__":
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)  # Duplicates removed

    if 'xxx' in basket:
        print("present")
    else:
        print("Not present")

    a = set("aabbccdd")
    print(a)
    b = set("ccddeeff")
    print(b)
    print(a - b)
    print(a | b)
    print(a & b)
    print(a ^ b)
