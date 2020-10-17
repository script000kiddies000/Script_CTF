import zipfile, re, os
def extract_nested_zip(zippedFile, toFolder):
        """ Unzip a zip file and its contents, including nested zip files
            Delete the zip file(s) after extraction
        """
        with zipfile.ZipFile(zippedFile, 'r') as zfile:
            zfile.extractall(path=toFolder)
        os.remove(zippedFile)
        for root, dirs, files in os.walk(toFolder):
            for filename in files:
                if re.search(r'\.zip$', filename):
                    fileSpec = os.path.join(root, filename)
                    extract_nested_zip(fileSpec, root)

    

extract_nested_zip("U.zip","/root/Unduhan/hacker class compfest/")
