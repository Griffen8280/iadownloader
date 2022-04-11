# iadownloader
Simple downloader that accepts a few arguments on the command line and does it's thing.

## Output of Help
```
usage: iadownloader.py [-h] -u URL [-o OUTPUT] [-g GLOB_PATTERN] [-v VERBOSE]

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     Input URL (the bit after archive.org/download/THISSTUFFHERE)
  -o OUTPUT, --output OUTPUT
                        Output directory, if not specified it will download here
  -g GLOB_PATTERN, --glob_pattern GLOB_PATTERN
                        Glob Pattern if you only want certian files (ie. *7z, *mkv, *png)
  -v VERBOSE, --verbose VERBOSE
                        Verbose, whether you want to see the output
```
