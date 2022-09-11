import glob


def get_all_files_in_dir(directory_name):
    file_list = []
    for file in glob.glob(f"{directory_name}/*.*"):
        file_list.append(file)
    return file_list


def get_all_xl_files_in_dir(directory_name):
    file_list = []
    for file in glob.glob(f'{directory_name}/*.xlsx'):
        file_list.append(file)
    return file_list


# desired_directory = input("Type the name of the directory : ")
#
# test_files = get_all_files_in_dir(desired_directory)
# xl_files = get_all_xl_files_in_dir(desired_directory)
# print(f"These are all the files in the directory : {test_files}")
# print(f'Of those files, these are the Excel files: {xl_files}')
