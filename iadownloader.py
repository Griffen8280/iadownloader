# Import needed modules for script to work
import argparse
import os

# The following will see if internetarchive is installed and prompt if not.
try:
    from internetarchive import download
except ImportError:
    print("The internet archive module is not installed")
    print("run pip install internetarchive to install it.")
    exit()   

# Construct an argument parser
all_args = argparse.ArgumentParser()

# Add arguments to the parser
all_args.add_argument('-u', '--url', type=str, required=True, help="Input URL (the bit after archive.org/download/THISSTUFFHERE)")
all_args.add_argument('-o', '--output', type=str, required=False, help="Output directory, if not specified it will download here")
all_args.add_argument('-g', '--glob_pattern', type=str, required=False, help="Glob Pattern if you only want certian files (ie. *7z, *mkv, *png)")
all_args.add_argument('-v', '--verbose', type=str, required=False, help="Verbose, whether you want to see the output")
args = all_args.parse_args()

# Do the stuff
if args.output:
    path = args.output
    f_path = os.chdir(path)
    f = os.getcwd()
else:
    path = './'
    f_path = os.chdir(path)
    f = os.getcwd()

if args.glob_pattern and args.verbose:
    download (args.url, verbose=True, glob_pattern=args.glob_pattern)
elif args.glob_pattern:
    download (args.url, glob_pattern=args.glob_pattern)
elif args.verbose:
    download (args.url, verbose=True)
else:
    download (args.url)

# We're done here
exit()