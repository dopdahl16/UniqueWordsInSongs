def CleanLyrics(file_to_open_name):
    f = open(file_to_open_name, "r")
    # TODO: Remove things like "[Chorus]" from files
    f.close()