import tkinter as tk

root = tk.Tk()
S = tk.Scrollbar(root)
vget = root.winfo_screenheight()
print(vget)
T = tk.Text(root, height=vget, width=80)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack()
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
T.insert(tk.END, "")
tk.mainloop()