from sys import argv

from src.doremi_executor import DoremiExecutor


def main():

    if len(argv) != 2:
        raise Exception("File path not entered")

    file_path = argv[1]
    with open(file_path, "r") as f:
        lines = f.readlines()
        command_executor = DoremiExecutor()
        command_executor.execute(command_lines=lines)


if __name__ == "__main__":
    main()
