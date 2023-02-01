def assertSame(expect, got):
    if str(expect) != str(got):
        print('Expect: ' + str(expect) + '. Got: ' + str(got))
    assert str(expect) == str(got)