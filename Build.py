def Run():
    import os
    os.chdir("/var/lib/mkt/Res/Data/BaseDB/")
    print("[BaseDB] Initing ...")
    
    files = [
        ["https://raw.githubusercontent.com/AidenPearce369/OSCP-Notes/main/README.md","Notes/OSCP_Note.md"]
    ]

    for downloadLink,savePath in files:
        print("[BaseDB] Downloading %s ... " % (os.path.basename(savePath)))
        WgetDownloadFile(downloadLink,"/var/lib/mkt/Res/Data/BaseDB/" + savePath)

def WgetDownloadFile(url,local_path,quiet = False):
    import os
    if os.path.exists(local_path):
        os.remove(local_path)
    quiet = "--quiet" if quiet else ""
    os.system('wget "%s" %s -O "%s"' % (url,quiet,local_path))
