from os import walk


def getStepFiles(dir):
    """ Return the list of step files in directory 'dir'
    :param dir: a directory where we look for step files
    :return: the list of step files in dir
    """
    file_list = []
    for sdp, Lsd, Lnf in walk(dir):
        for f in Lnf:
            if f.endswith(".step"):
                file_list.append(dir+'/'+f)
    file_list.sort()
    return file_list

def read(mambo_dir, option = "All"):
    """ read mambo files from a specified directory
    :param mambo_dir: the mambo directory
    :param option: what whe want to read in mambo. It can be only the basic models ("Basic"), the simple ones
                   ("Simple"), the medium ones ("Medium") or all of them ("All"). Default behavior is to read all of
                   them ("All")
    :return: the list of step files
    """
    step_files = []
    if (option == "Basic") or (option == "Simple") or (option == "Medium"):
        step_files = getStepFiles(mambo_dir + "/" + option)
    elif option == "All":
        step_files = getStepFiles(mambo_dir + "/Basic")
        step_files.append(getStepFiles(mambo_dir + "/Simple"))
        step_files.append(getStepFiles(mambo_dir + "/Medium"))
    return step_files