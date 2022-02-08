#! /usr/bin/env python3
import argparse
import os
from src.file_service import file_service


def read_file():
    """ Asks use for filename, prints file content """
    filename = input("Enter file name : ")
    print(f"read file : {filename}")
    content = file_service.read_file(filename)
    print(content)


def create_file():
    """ Asks user for file content, creates file with that content """
    content = input("Enter file content : ")
    print(f"creating file with content: {content}")
    filename = file_service.create_file(content)
    print(f"created file with name: {filename}")


def delete_file():
    """ Asks user for filename, deletes this file """
    filename = input("Enter file name : ")
    file_service.delete_file(filename)
    print(f"deleted file : {filename}")


def list_dir():
    """ Prints content of current directory """
    print(f"list dir")
    for f in file_service.list_dir():
        print(f)


def change_dir():
    """ Asks user for directory name, changes current working directory """
    directory = input("Enter dir name : ")
    print(f"change dir : {directory}")
    file_service.change_dir(directory)


def print_current_dir():
    """ Prints path to current working directory """
    print(file_service.get_current_dir())


def main():
    """ Parses arguments and starts accepting user CLI commands for file server """
    parser = argparse.ArgumentParser(description="REST File Server")
    parser.add_argument('-d', '--directory', dest='initial_dir', help="Initial directory", default=os.getcwd())
    args = parser.parse_args()
    if not os.path.isdir(args.initial_dir):
        print(f"{args.initial_dir} - directory does not exist!")
        return
    else:
        os.chdir(args.initial_dir)

    commands = {
        "read": read_file,
        "create": create_file,
        "delete": delete_file,
        "ls": list_dir,
        "cd": change_dir,
        "pwd": print_current_dir
    }

    while True:
        command = input("Enter command: ")
        if command == "exit":
            return
        if command not in commands:
            print(f"Unknown command - {command}")
            print(f"Supported commands: {list(commands.keys())}")
            continue
        command = commands[command]
        try:
            command()
        except Exception as ex:
            print(f"Error on {command} execution : {ex}")


if __name__ == "__main__":
    main()
