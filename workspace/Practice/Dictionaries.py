if __name__=="__main__":
    tel = {'jack': 4098, 'sape': 4139}
    print(tel)
    tel['guido'] = 4127
    print(tel)
    print(tel['jack'])
    del tel['sape']
    print(tel)

    print(list(tel))

    print(sorted(tel))