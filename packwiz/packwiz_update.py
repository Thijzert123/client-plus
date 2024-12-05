#!/usr/bin/python3

import sys
import os
import subprocess

PACKWIZ_SUFFIX = ".pw.toml" # files that are managed by packwiz

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'

# remove and clean all mod/shaders/resources managed by packwiz
def remove_packwiz_files(mc_dirs, debug = False):
    for root, dirnames, filenames in os.walk("."):
        for filename in filenames:
            if filename.endswith(PACKWIZ_SUFFIX):
                filepath = os.path.join(root, filename)
                mc_version = root.split("/")[1]
                if mc_version in mc_dirs:
                    if debug:
                        print("Removing " + filepath)
                    os.remove(filepath)

def main(debug = False):
    if len(sys.argv) < 2:
        print("Please specify Minecraft version (e.g. 1.21.1) or update all instances with 'all'.")
        exit(1)

    packwiz_output_stream = subprocess.DEVNULL
    if debug:
        packwiz_output_stream = None

    mc_dirs = [] # such as mc1.20.4 or mc1.21.1
    if sys.argv[1] == "all":
        for root, dirnames, filenames in os.walk("."):
            for dirname in dirnames:
                if dirname.startswith("mc"):
                    mc_dirs.append(dirname)
    else:
        for arg in sys.argv[1:]: # skip first entry
            mc_dirs.append("mc" + arg)

    pack_content = eval(open("pack_content.py").read())

    print("Removing packwiz files...", end="")
    sys.stdout.flush()
    remove_packwiz_files(mc_dirs, debug)
    print(" done")
    
    projects = []
    for content_type in pack_content:
        for project in pack_content[content_type]:
            projects.append(project)

    for project in sorted(projects):
        print(f"Adding {project}: ", end="")
        sys.stdout.flush()
        
        for mc_dir in sorted(mc_dirs):
            command = ["packwiz", "modrinth", "install", "--yes", project]
            if project == "hyper-realistic-sky":
                command = ["packwiz", "modrinth", "install", "--yes", "--project-id", "hyper-realistic-sky", "--version-id", "Ag95J3hS"]
                    
            returncode = subprocess.run(command, cwd=mc_dir, stdout=packwiz_output_stream, stderr=packwiz_output_stream).returncode
            mc_version = mc_dir.replace("mc", "")
            
            if returncode == 0:
                print(f"{Colors.GREEN}{mc_version}{Colors.END} ", end="")
            else:
                print(f"{Colors.RED}{mc_version}{Colors.END} ", end="")
            sys.stdout.flush()
                    
        print("done")

if __name__ == "__main__":
    main()
