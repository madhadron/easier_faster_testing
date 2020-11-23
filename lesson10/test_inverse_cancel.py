def test_inverses_cancel():
    for nmax in range(10000):
        n = random.randint(1, nmax)
        with self.subTest(n=n):
            self.assertEquals(0, n+(-n))