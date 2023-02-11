def assertSame(expect, got):
    def listToString(l):
        l.sort()
        return str(list(map(str, l)))
    if isinstance(expect, list):
        expect = listToString(expect)
        # print('sorted ' + str(expect))
    if isinstance(got, list):
        got = listToString(got)
        # print('sorted ' + str(got))
    if str(expect) != str(got):
        print('Expect: ' + str(expect) + '. Got: ' + str(got))
    assert str(expect) == str(got)