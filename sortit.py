import sys
import time
import logging

import yaml
import os

# A config file which maps files to its Type
# You may edit the config file so as to add a flie type
# A dictionary where keys are Type and values are extensions
CONFIG = yaml.load(open('config.yaml','r').read(),Loader=yaml.SafeLoader)
# reverse the dictionary 
FILE_TYPES = {value: key for key in CONFIG.keys() for value in CONFIG[key]}


def createSymLink(directory='~/Downloads',destination='~/Desktop/Downloads'):
    """
    This function receives the directory in which the files are to be sorted and the Destination directory where
    the sorted files with folders are to be created.
    This does not copy or move the files, but creates a symbolic link to the original file and keeps them in the 
    destination folder so that original data is not tampered.
    Parameters
        -----------------------------
        directory : str
            The path of the directory to sort. eg. ~/Downloads
        destination : str
            The path of destination where the sym-links are to be created.
    """
    # expands the tilde to home dir
    directory = os.path.expanduser(directory)
    destination = os.path.expanduser(destination)
    # get all the files in the directory
    try:
        os.chdir(os.path.join(os.getcwd(),directory))
        dir = os.listdir()
        cwd = os.getcwd()
        files = [i for i in dir if not os.path.isdir(i) and not i.startswith('.')]
    except Exception as e:
        print(e)
    
    for file in files:
        # Extract the extension. Misc if no key is found.
        try:
            ext = 'misc' if len(file.split('.'))<2 else file.split('.')[-1]
            ext_folder = FILE_TYPES[ext].capitalize()
        except KeyError:
            ext_folder = 'Misc'
        file_directory = os.path.join(destination,ext_folder)
        
        # Make the directory or sub-directories if not exists
        os.makedirs(file_directory,exist_ok = True)
        src_path = os.path.join(cwd,file)
        dest_path = os.path.join(file_directory,file)
        # logging.info(src_path,'-->',dest_path)
        try:
            if not os.path.exists(dest_path):
                # Create a symlink
                os.symlink(src_path,dest_path)
        except OSError:
            logging.info('File already Exists.',dest_path)
            pass 
        except Exception as e:
            logging.info(e)
    logging.info('Successfully sorted and symlink-ed files.')

       
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    createSymLink(sys.argv[1],sys.argv[2])
    
    
