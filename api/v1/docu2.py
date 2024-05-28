import app

def check_doc(obj):
    if obj.__doc__:
        print(f"Documentation for {obj.__name__}:\n{obj.__doc__}")
    else:
        print(f"No documentation found for {obj.__name__}")

for name in dir(app):
    obj = getattr(app, name)
    if callable(obj):
        check_doc(obj)
