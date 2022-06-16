def Run():
    import os
    os.chdir("/var/lib/mkt/Res/Data/BaseDB/")
    print("[BaseDB] Initing ...")
    
    with open("List","r") as file:
        for line in file:
            line = line.strip()
            if (line == ""):
                continue
            downloadLink,savePath = line.split("||")
            downloadLink = downloadLink.strip()
            savePath = savePath.strip()

            print("[BaseDB] Downloading %s ... " % (os.path.basename(savePath)))
            absSavePath = "/var/lib/mkt/Res/Data/BaseDB/" + savePath

            from pathlib import Path
            path = Path(os.path.dirname(absSavePath))
            path.mkdir(parents=True, exist_ok=True)

            WgetDownloadFile(downloadLink,absSavePath,True)

def WgetDownloadFile(url,local_path,quiet = False):
    import os
    if os.path.exists(local_path):
        os.remove(local_path)
    quiet = "--quiet" if quiet else ""
    os.system('wget "%s" %s -O "%s"' % (url,quiet,local_path))
