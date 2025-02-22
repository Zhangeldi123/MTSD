import sys

if len(sys.argv) > 1:
    for name in sys.argv[1:]:
        print(f"Hello, {name}!")
else:
    print("No names provided.")
