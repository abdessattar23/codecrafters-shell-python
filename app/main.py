import sys


def main():
    # Uncomment this block to pass the first stage
    

    # Wait for user input
    while(True):
        sys.stdout.write("$ ")
        sys.stdout.flush()
        inp = input("")
        if inp == "exit 0":
            return 0
        elif inp.startswith("echo"):
            sys.stdout.write(inp.replace("echo ", "") + "\n")
            sys.stdout.flush()
        elif inp.startswith("type"):
            cmd = inp.replace("type ", "");
            if(cmd == "echo" or cmd == "type" or cmd == "exit"):
                sys.stdout.write(f"{cmd} is a shell builtin\n")
                sys.stdout.flush()
            else:
                sys.stdout.write(f"{cmd}: not found\n")
                sys.stdout.flush()
        else:
            sys.stdout.write(f"{inp}: command not found\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
