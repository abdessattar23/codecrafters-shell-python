import sys


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    inp = input("")
    sys.stdout.write(f"{inp}: command not found\n")
    sys.stdout.flush()


if __name__ == "__main__":
    main()
