
def foo(n):
    def recurve(n, original):
        if n == 0:
            return
        print(original)

        recurve(n-1, original)
    recurve(n, n)

foo(4)