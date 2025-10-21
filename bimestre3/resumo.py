#  _ __ ___  ___ _   _ _ __ ___   ___   _ __  _   _
# | '__/ _ \/ __| | | | '_ ` _ \ / _ \ | '_ \| | | |
# | | |  __/\__ \ |_| | | | | | | (_) || |_) | |_| |
# |_|  \___||___/\__,_|_| |_| |_|\___(_) .__/ \__, |
#                                      |_|    |___/

# encodings ISO-8859-1 e latin-1 são o mesmo
with open("file", "mode", encoding="ISO-8859-1") as file:
    # ou file = open("file", "mode")
    file.read(1)  # size
    file.readline()
    file.readlines()
    file.close()
    file.seek(0)  # reseta o ponteiro
    file.write("text")
