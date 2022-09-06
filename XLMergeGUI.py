import tkinter as tk
from extension import get_all_xl_files_in_dir


def check_dir():
    dir_select = directory_entry.get()
    directory_entry.delete(0, 'end')
    xl_list = get_all_xl_files_in_dir(dir_select)
    for count, file in enumerate(xl_list):
        current_filename = file.split("/")[-1] + '\n'
        print(file.split("/")[-1])
        output_xlfiles.insert(f"{count + 1}.0", current_filename)


main_window = tk.Tk()
main_window.geometry('320x200')

greeting = tk.Label(text='Welcome to XL Merge')
greeting.pack()

directory_entry = tk.Entry()
directory_entry.pack()

directory_submit = tk.Button(text='Submit Directory', command=check_dir)
directory_submit.pack()

output_xlfiles = tk.Text()
output_xlfiles.pack()

main_window.mainloop()
# /home/scrant/PycharmProjects/
