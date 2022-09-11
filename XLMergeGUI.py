from tkinter import *
import tkinter as tk
from tkinter.filedialog import askdirectory
from extension import get_all_xl_files_in_dir
from xlmerger import merge_click


xl_list = []


def check_dir():
    dir_select = directory_entry.get()
    # directory_entry.delete(0, 'end')
    global xl_list
    xl_list = get_all_xl_files_in_dir(dir_select)
    output_xlfiles.delete('1.0', 'end')
    for count, file in enumerate(xl_list):
        current_filename = file.split("/")[-1] + '\n'
        # print(file.split("/")[-1])
        output_xlfiles.insert(f"{count + 1}.0", current_filename)


def dir_assign():
    manual_select = askdirectory(title='Select Directory')
    directory_entry.delete(0, "end")
    directory_entry.insert(0, manual_select)


def pop_up():
    pop_up_window = tk.Tk()
    pop_up_window.geometry('400x300')

    pop_up_greeting = tk.Label(pop_up_window, text="Merge these files?")
    pop_up_greeting.pack()

    pop_up_outfile = tk.Text(pop_up_window)
    pop_up_outfile.pack()
    for count, file in enumerate(xl_list):
        current_filename = file.split("/")[-1] + '\n'
        # print(file.split("/")[-1])
        pop_up_outfile.insert(f"{count + 1}.0", current_filename)

    pop_up_button1 = tk.Button(pop_up_window, text="Close", command=pop_up_window.destroy)
    pop_up_button1.pack()

    pop_up_window.mainloop()


main_window = tk.Tk()
main_window.geometry('750x400')

greeting = tk.Label(text='Welcome to XL Merge')
greeting.pack()

directory_entry = tk.Entry(main_window, width=50)
directory_entry.pack()

select_dir = tk.Button(main_window, text="Select Directory", command=dir_assign)
select_dir.pack()

directory_submit = tk.Button(main_window, text='List XL Files in specified directory', relief=RAISED, command=check_dir)
directory_submit.pack()

output_xlfiles = tk.Text(height=8)
output_xlfiles.pack()

merge_button = tk.Button(text="Merge selected files", command=lambda: merge_click(xl_list))
merge_button.pack()

exit_button = tk.Button(main_window, text="Exit and create files", command=main_window.destroy)
exit_button.pack()

main_window.mainloop()
# /home/scrant/PycharmProjects/Scrap
# refining merge feature
