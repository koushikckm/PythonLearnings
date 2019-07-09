if __name__=="__main__":
    t = 12345, 54321, 'hello!'
    print(t[0])

    # Tuples may be nested
    u = t, (1, 2, 3, 4, 5)
    print(u)
    print(u[0])

    # Tuples are immutable
    t[0] = 2222