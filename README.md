# Sort-It
A python script to sort the files in Downloads into respesctive types.


This srcipt searches the files in the target directory and sorts them according to the mapping
present in the Config File. Its identifies the file type and create a symbolic link to the original
file in destination Directory corresponding to the file type.

You may edit or add new file types and extentions in [config.yaml](./config.yaml)
## Features
- [x] Sorts files in a directory and create symbolic links to original file in a sorted folder.
- [ ] Create a Handler which runs in background and behave as target directory is modified.


## Installation
```
# clone the repo
$ git clone https://github.com/BhargavSatya/Sort-It.git

# Change the working directory to Sort-It
$ cd Sort-It

# Install the requirements
$ pip3 install -r requirements.txt
```
## Usage

```
python sortit.py ~/Downloads ~/Desktop/Downloads
```

```
usage: sortit.py [source_directory] [destination directory]

```

## License
MIT © [BhargavSatya] (https://github.com/BhargavSatya)

## Contributions
- ⭐️ this repository if this script helped you.
- Contributions of any kind are welcome!
