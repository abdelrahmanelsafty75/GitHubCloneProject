def say_my_name(n):
    if n == 0:
        return
    print("My name is Elsafty")
    say_my_name(n - 1)

say_my_name(5)