def Run():
    max_thread = 3

    import os
    os.chdir("/var/lib/mkt/Res/Data/BaseDB/")
    print("[BaseDB] Initing ...")

    from concurrent.futures import ThreadPoolExecutor, as_completed

    def sub_run(path):
        import subprocess,os
        base_name = os.path.basename(path)
        print("[%s] Fetching ..." % (base_name))
        subprocess.getoutput("python3 '%s'" % (path))
        os.remove(path)
        return base_name

    executor = ThreadPoolExecutor(max_workers=max_thread)
    task_pool = []
    for path,sub_path,files in os.walk("/var/lib/mkt/Res/Data/BaseDB/"):
        for file in files :
            if (file[-(len(".mktdb")):] == ".mktdb") :
                task_pool.append(executor.submit(sub_run,(path + "/" + file)))

    for status in as_completed(task_pool):
        #print("[%s] Done!" % (status.result()))
        pass

    print("[BaseDB] All finished!")
