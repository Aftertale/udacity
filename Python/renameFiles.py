import os

def rename_files():
    # get names from a folder
    os.chdir(r"C:\Users\dmcdowell\Downloads\prank\prank")
    file_list = os.listdir(r"C:\Users\dmcdowell\Downloads\prank\prank")
    print(file_list)
    # for each file rename file
    for file_name in file_list:
        new_name = file_name.translate(None, "0123456789")
        print("Changing file "+file_name+" to "+new_name)
        os.rename(file_name, new_name)
        print("done!")


rename_files()
