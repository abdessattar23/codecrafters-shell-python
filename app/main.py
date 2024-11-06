import sys


def main():
    # Uncomment this block to pass the first stage
    

    # Wait for user input
    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()
        inp = input("")
        sys.stdout.write(f"{inp}: command not found\n")
        sys.stdout.flush()


if __name__ == "__main__":
    main()
