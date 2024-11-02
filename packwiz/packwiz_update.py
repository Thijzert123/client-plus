#!/usr/bin/python3

#
# min. python version: 3.11
#

import os
import tomllib # python >= 3.11
import requests

PACKWIZ_SUFFIX = ".pw.toml"

# human readable id: fabric-api
# abstract id: P7dR8mSH
def convert_to_abstract_modrinth_id(human_readable_id):
    project_url = "https://api.modrinth.com/v2/project/" + human_readable_id
    r = requests.get(project_url)
    if r.status_code != 200:
        print("Error while retrieving project " + human_readable_id)
        exit(1)
    project_details = r.json()
    return project_details["id"]

def retrieve_pinned_projects():
    pinned_projects = []
    for root, dirs, files in os.walk("."):
        for file_name in files:
            if file_name.endswith(PACKWIZ_SUFFIX):
                file_path = os.path.join(root, file_name)
                remove = True
                abstract_modrinth_id = ""
                with open(file_path, "rb") as file_content:
                    toml_data = tomllib.load(file_content)
                    abstract_modrinth_id = toml_data["update"]["modrinth"]["mod-id"]
                    if "pin" in toml_data:
                        if toml_data["pin"] == True:
                            remove = False
                if remove:
                    print("Removing " + file_path)
                    os.remove(file_path)
                else:
                    print(abstract_modrinth_id + " is pinned")
                    pinned_projects.append(abstract_modrinth_id)
    os.system("packwiz refresh")
    return pinned_projects

def main():
    if not os.path.isfile("pack.toml"):
        print("No pack.toml found, exiting")
        exit(0)

    pack_content = eval(open("../pack_content.py").read())
    pinned_projects = retrieve_pinned_projects()

    for content_type in pack_content:
        for project in pack_content[content_type]:
            abstract_modrinth_id = convert_to_abstract_modrinth_id(project)
            if abstract_modrinth_id not in pinned_projects:
                print("Adding project: " + project)
                os.system("packwiz modrinth install --yes " + project)
            else:
                print("Project already in packwiz: " + project)

    os.system("packwiz update --all --yes")

if __name__ == "__main__":
    main()
