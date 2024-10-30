# Packwiz
`packwiz` is used to assemble the modpack. You can find the installation instructions [here](https://packwiz.infra.link/installation).

## Export modpack
In the folder of a Minecraft version, run:
```
packwiz modrinth export
```

## Adding mods to another packwiz instance
You can use `packwiz-import-mods.sh` to import all the mods, resource packs and shaders to another packwiz instance.

## Generation of a project list
With `packwiz-generate-project-list.py`, you can generate a list of all the mods used in this modpack and in which versions they come in. To download the dependencies, run `pip install py-markdown-table`. Then, while inside the packwiz directory, run:
```bash
python3 pip install py-markdown-table
```
A file `project_list.md` will be generated in the same directory.
