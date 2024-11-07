import sys
import os
def find_in_path(param):
    path = os.environ['PATH']
    for directory in path.split(":"):
        for (dirpath, dirnames, filenames) in os.walk(directory):
            if param in filenames:
                return f"{dirpath}/{param}"
    return None
def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()
        match command.split(" "):
            case ["exit", "0"]:
                exit(0)
            case ["echo", *cmd]:
                print(" ".join(cmd))
            case ["type", *cmd]:
                match cmd:
                    case ["pwd" |"echo" | "exit" | "type"]:
                        print(f"{cmd[0]} is a shell builtin")
                    case _:
                        location = find_in_path(cmd[0])
                        if location:
                            print(f"{cmd[0]} is {location}")
                        else:
                            print(f"{" ".join(cmd)}: not found")

            case _:
                if command == "pwd":
                    print(f"{os.getcwd()}")
                else:
                    paths = os.environ.get("PATH")
                    paths = paths.split(":")
                    for path in paths:
                        if os.path.isfile(f"{path}\\{command.split(' ')[0]}"):
                            os.system(command)
                            break
                    else:
                        print(f"{command}: command not found")



if __name__ == "__main__":
    main()
