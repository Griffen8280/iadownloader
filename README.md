# Internet Archive Downloader
Simple downloader that accepts a few arguments on the command line and does it's thing.

## Output of Help
```
usage: iadownloader.py [-h] -u URL [-o OUTPUT] [-g GLOB_PATTERN] [-v VERBOSE]

optional arguments:
  -h, --help            show this help message and exit
  -u, --url             Input URL (the bit after archive.org/download/THISSTUFFHERE)
  -o, --output          Output directory, if not specified it will download here
  -g, --glob_pattern    Glob Pattern if you only want certian files (ie. *7z, *mkv, *png)
  -v, --verbose         Verbose, whether you want to see the output
```
