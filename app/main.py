import sys
import os


def main():
    # Uncomment this block to pass the first stage
    
    path = os.environ.get("PATH")
    paths = path.split(":")
    path_cmds = []
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
            for pathx in paths:
                if os.path.isfile(f"{pathx/cmd}"):
                    path_cmds.append(cmd)
            if(cmd == "echo" or cmd == "type" or cmd == "exit"):
                sys.stdout.write(f"{cmd} is a shell builtin\n")
                sys.stdout.flush()
            elif cmd in path_cmds:
                sys.stdout.write(f"{cmd} is {path}/{cmd}\n")
                sys.stdout.flush()
        else:
            sys.stdout.write(f"{inp}: command not found\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
