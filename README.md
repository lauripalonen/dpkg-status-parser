# dpkg-status-parser
A simple dpkg status data parser.  

As an input it accepts a Debian / Linux status file found in /var/lib/dpkg/status. Output is a JSON string.

## Installation  
Requirement: Python3

Clone project with `git clone git@github.com:lauripalonen/dpkg-status-parser.git` or extract the project [.zip](https://github.com/lauripalonen/dpkg-status-parser/archive/master.zip) file to a directory of your choice.  

Copy a desired status file to the root directory, or use the provided sample file (sample_status.real). 

## Usage
Run program with `python3 main.py`. This will initiate a small command line ui:
```
Dpkg status data parser
-----------------------
File name (input): 
File name (output): 
```
As for input file name, use the name of the status file.  

For output file name, choose a name to your liking with .json extension.

As an succesfull output there will be a JSON file with items having following structure:  
```
{
  "id": (int) a unique id,
  "name": (string) name of the package,
  "description": (string) short description,
  "dependencies": (int array) id's of packages that this package depends on,
  "alternatives": (string array) names of alternative dependencies for this package,
  "dependants": (int array) id's of packages that depend on this package
 }
  
```
## For further development
- Add a feature for file overwriting
- Create tests



