#!usr/bin/env python3

#
#   Boiler.
#       By L3pu5, L3pu5_Hare
#

import sys

extensions = {
    "py": lambda name: f"#\n#   {name}.\n#       By L3pu5, L3pu5_Hare\n#",
    "cs": lambda name: f"//\n//   {name}.\n//       By L3pu5, L3pu5_Hare\n//",
    "cpp": lambda name: f"//\n//   {name}.\n//       By L3pu5, L3pu5_Hare\n//",
    "c": lambda name: f"//\n//   {name}.\n//       By L3pu5, L3pu5_Hare\n//",
    "js": lambda name: f"//\n//   {name}.\n//       By L3pu5, L3pu5_Hare\n//",
    "rs": lambda name: f"//\n//   {name}.\n//       By L3pu5, L3pu5_Hare\n//",
}

def usage():
    print("Usage:       boiler.py newfile")
    print("Boiler will attempt to dump the predetermined boilerplater header to the top of the file.")

def write_file(name, ext):
    file = open("./" + name + "." + ext, "w")
    if ext in extensions:
        file.write(extensions[ext](name))
    file.flush()
    file.close()


def main():
    if len(sys.argv) != 2:
        usage()
    else:
        name_and_extension = sys.argv[1].split(".", 2)
        write_file(name_and_extension[0], name_and_extension[1])

if __name__ == "__main__":
    main()