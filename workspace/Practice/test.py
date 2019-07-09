def testlooping():
    a = ['Mary', 'had', 'a', 'little', 'lamb']
    for i in range(len(a)):
        print(i, a[i])


def testbreak():
    for n in range(2, 10):
        if n % 5 == 0:
            break
        else:
            print(n)


def testcontinue():
    for n in range(2, 10):
        if n % 5 == 0:
            continue
        else:
            print(n)


def defaultargvalues(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

def keywordarguments(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print(action)
    print(voltage)
    print(type)
    print(state)


def arbitraryargs(*args, sep="/"):
    return sep.join(args)


def testlambdaexp(n):
    return lambda x: x + n


if __name__=="__main__":

    # testlooping()
    # testbreak()
    # testcontinue()

    # defaultargvalues('Do you really want to quit?')
    # defaultargvalues('OK to overwrite the file?', 2)
    # defaultargvalues('OK to overwrite the file?', 2, 'Come on, only yes or no!')

    #keywordarguments(1000)
    #keywordarguments(voltage=1000)
    #keywordarguments(voltage=1000000, action='VOOOOOM')
    #keywordarguments(action='VOOOOOM', voltage=1000000)
    #keywordarguments('a million', 'bereft of life', 'jump')
    #keywordarguments('a thousand', state='pushing up the daisies')

    #print(arbitraryargs("earth", "mars", "venus"))
    #print(arbitraryargs("earth", "mars", "venus", sep="."))

    f = testlambdaexp(4)
    print(f(5))