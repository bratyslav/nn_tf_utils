import os


class DataGen:
    def read_all_fnames_from(self, path):
        # create a list of file names in given directory and sub directories
        listdir = os.listdir(path)
        fnames = []
        # Iterate over all the entries
        for entry in listdir:
            full_path = os.path.join(path, entry)
            # If entry is a directory then get the list of files in this directory
            if os.path.isdir(full_path):
                fnames = fnames + self.read_all_fnames_from(full_path)
            else:
                fnames.append(full_path)
        return fnames
