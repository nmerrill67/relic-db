import tarfile
import os

#extract the files from MBZ backup, and store in folder VPL
def extract_tar_file(source_file, output_directory):
    tar = tarfile.open(source_file)
    tar.extractall(path = output_directory)
    tar.close()


#recreate VPL backup file from directory using modified files
def make_tarfile(output_filename, source_dir):
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.sep)

#extract_tar_file("backup-moodle.mbz","vpl") #your filename here
#make_tarfile("new-backup.mbz", "vpl")