#!/usr/bin/python3

#
# min. python version: 3.11
#

import os
import tomllib
from py_markdown_table.markdown_table import markdown_table

ROOT_DIR = "."
MC_PREFIX = "mc"
PACKWIZ_SUFFIX = ".pw.toml"

data = []
projectsindexindata = {}
projectsloaded = []

def loadtomldata(root, category, mcversion):
    for root, dirs, files in os.walk(root):
        for filename in files:
            if filename.endswith(PACKWIZ_SUFFIX):
                filepath = os.path.join(root, filename)
                with open(filepath, "rb") as filecontent:
                    filedata = tomllib.load(filecontent)
                    projectname = filedata["name"]

                    if projectname in projectsloaded:
                        if mcversion == "1.21.1":
                            data[projectsindexindata[projectname]]["1.21.1"] = ":white_check_mark:" if mcversion == "1.21.1" else ":x:"
                        elif mcversion == "1.21.3":
                            data[projectsindexindata[projectname]]["1.21.3"] = ":white_check_mark:" if mcversion == "1.21.3" else ":x:"
                    else:
                        projectid = filedata["update"]["modrinth"]["mod-id"]
                        projecturl = "https://modrinth.com/project/" + projectid
                        projectnameformatted = "[" + projectname + "](" + projecturl + ")"
                        
                        projectdata = {
                            "Name" : projectnameformatted,
                            "1.21.1" : ":white_check_mark:" if mcversion == "1.21.1" else ":x:",
                            "1.21.3" : ":white_check_mark:" if mcversion == "1.21.3" else ":x:"
                        }

                        data.append(projectdata)
                        projectsindexindata[projectname] = len(projectsloaded)
                        projectsloaded.append(projectname)


for packwizroot, packwizdirs, packwizfiles in os.walk("."):
    for minecraftdirname in packwizdirs:
        if minecraftdirname.startswith(MC_PREFIX):
            mcversion = minecraftdirname.removeprefix(MC_PREFIX).strip()
            
            for root, dirs, files in os.walk(os.path.join(packwizroot, minecraftdirname)):
                for dirname in dirs:
                    tomlroot = os.path.join(root, dirname)
                    if dirname == "mods":
                        loadtomldata(tomlroot, "mods", mcversion)
                    elif dirname == "resourcepacks":
                        loadtomldata(tomlroot, "resourcepacks", mcversion)
                    elif dirname == "shaderpacks":
                        loadtomldata(tomlroot, "shaderpacks", mcversion)

sorteddata = sorted(data, key=lambda d: d["Name"])
print(markdown_table(sorteddata).set_params(row_sep = 'markdown', quote = False).get_markdown())
