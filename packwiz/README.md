# Packwiz
`packwiz` is used to assemble the modpack. You can find the installation instructions [here](https://packwiz.infra.link/installation).

## Export modpack
In the folder of a Minecraft version, run:
```
packwiz modrinth export
```

## Updating or adding contents of this modpack to another packwiz instance
You can use `packwiz_update.py` to import all the mods, resource packs and shaders to another packwiz instance. Be sure to specify the game version, like `1.21.1` or `1.21.3`, or `all` to update all versions. After that, you need to copy the contents of the directory `packwiz/overrides/<your Minecraft version>` to your folder containing the packwiz data. Don't forget to run `packwiz refresh` to update the hashes and the `index.toml` file. These actions would look something like this:
```
$ pwd # current working directory
/home/john/git/client-plus/packwiz
$ python3 packwiz_update.py 1.21.1
...
$ cp -r overrides/YOUR-MC-VERSION/* mc1.21.1
$ packwiz refresh
```

## Generation of a project list
With `packwiz_generate_project_list.py`, you can generate a list of all the mods used in this modpack and in which versions they come in. To download the dependencies, run `pip install py-markdown-table`. Then, while inside the packwiz directory, run:
```bash
python3 pip install py-markdown-table
```
A file `project_list.md` will be generated in the same directory.
