import sys

source_code = """

def Setup():
    import os
    Base_Path = os.path.split(os.path.realpath(__file__))[0]
    os.chdir(Base_Path)

    Download_array = [
        [\"""" + sys.argv[1] + """\",\""""+ sys.argv[2] +""".md\"]
    ]
    
    for a,b in Download_array:
        WgetDownloadFile(a,b,True)

def WgetDownloadFile(url,local_path,quiet = False):
    import os
    if os.path.exists(local_path):
        os.remove(local_path)
    quiet = "--quiet" if quiet else ""
    os.system('wget "%s" %s -O "%s"' % (url,quiet,local_path))

Setup()

"""

file = open(sys.argv[2] + ".mktdb", "w")
file.writelines(source_code)
file.close()
