#!/usr/bin/python3
if __name__ == "__main__":
    module_name = "hidden_4"
    hidden_4 = __import__(module_name)

    names = dir(hidden_4)

    for name in sorted(names):
        if not name.startswith("__"):
            print(name)
