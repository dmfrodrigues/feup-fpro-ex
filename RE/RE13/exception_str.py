def exception_str(f):
    try:
        f()
    except Exception as e:
        return str(e)
    else:
        return "No exception was raised"

print(exception_str(lambda: 1/0))
print(exception_str(lambda: 0))
