import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 argv_demo.py [jelly_beans]")
        print("Expected an integer, which is the number of jelly beans in the jar.")
    else:
        try:
            jelly_beans = int(sys.argv[1])
        except ValueError:
            print("Expected the argument to be an integer.")

if __name__ == "__main__":
    main()
