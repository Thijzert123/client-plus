#!/usr/bin/python3

import os

def main():
    pack_content = eval(open("../pack_content.py").read())

    if not os.path.isfile("pack.toml"):
        print(os.getcwd())

    for content_type in pack_content:
        for project in pack_content[content_type]:
            print("Adding project: " + project)
            os.system("packwiz modrinth install --yes " + project)

    os.system("packwiz update --all --yes")

if __name__ == "__main__":
    main()
