# Internet Archive Downloader
Simple downloader that accepts a few arguments on the command line and does it's thing.

## Output of Help
```
usage: iadownloader.py [-h] [-u URL] [-o OUTPUT] [-g GLOB_PATTERN] [-v VERBOSE]

optional arguments:
  -h, --help            show this help message and exit
  -u, --url             Input URL (the bit after archive.org/download/THISSTUFFHERE)
  -o, --output          Output directory, if not specified it will download here
  -g, --glob_pattern    Glob Pattern if you only want certian files (ie. *7z, *mkv, *png)
  -v, --verbose         Verbose, whether you want to see the output
```

## Example
```
$ python3 iadownloader.py -u YOURURLHERE -o ~/Downloads -g *mkv -v
```
In this example the python interpreter will execute the iadownloader.py script with the following options:
- URL where you want it to download to (Keep in mind that it will create a folder named the same as your URL to download into)
- Output folder to download to ie. ~/Downloads or /home/$USERNAME/Downloads
- Glob Pattern, which in this case would be just the mkv files in the archive your downloading
- Verbose option meaning I want to watch it work and see the progress of each download
