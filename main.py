import openpyxl as xl
import filemanip
import extension

directory = input('Type a directory where you store your Excel files: ')
file_name = extension.get_all_xl_files_in_dir(directory)
if len(file_name) == 0:
    print("No Excel files found in this directory")
    exit()

# wb = xl.load_workbook(file_name[0])
counter = 1
for count, file in enumerate(file_name):
    print(file.split("/")[-1], end=f" |{counter}| \n")
    counter += 1

# print(file_name[0])
# new_file_name = filemanip.file_name_increment(file_name)
# print(new_file_name)
# wb.save(new_file_name)
