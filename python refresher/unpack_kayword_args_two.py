def both(*args, **kwargs):
    print(args)
    print(kwargs)

both(1, 3, 4, name="Bob", age=25)