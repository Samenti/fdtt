# coding: utf-8

"""
Finnish Declension Tables Tester
--------------------------------
This is a simple GUI-based python program that helps with
learning Finnish nominal declension tables.
"""

# Max line length w/ --- w/o flowing text blocks (PEP 8 style guide): 72 --- 79

import Tkinter as tk

root = tk.Tk()

word=tk.StringVar()
word.set("<current word>")
english=tk.StringVar()
english.set("<English translation>")

title_text0 = tk.Label(root, font=("Helvetiva", 32), textvariable=word)
title_text0.grid(row=0, column=0)
title_text1 = tk.Label(root, text=" – ", font=("Helvetiva", 32))
title_text1.grid(row=0, column=1)
title_text2 = tk.Label(root, font=("Helvetiva", 32), textvariable=english)
title_text2.grid(row=0, column=2)

table_header0 = tk.Label(root, text="", font=("Helvetiva", 14))
table_header0.grid(row=1, column=0)
table_header1 = tk.Label(root, text="singular", font=("Helvetiva", 14))
table_header1.grid(row=1, column=1)
table_header2 = tk.Label(root, text="plural", font=("Helvetiva", 14))
table_header2.grid(row=1, column=2)

entry_dic = {}
labels = [
"nominative", "genitive", "accusative", "partitive", "illative", "inessive",
"allative", "adessive", "elative", "ablative", "essive", "abessive",
"translative", "instructive", "comitative"
]

row_counter = 2
for label in labels:
	entry_dic[label] = (tk.Label(root), tk.Entry(root), tk.Entry(root))

	entry_dic[label][0].config(text=label, font=("Helvetica", 14))
	entry_dic[label][0].grid(row=row_counter, column=0)

	entry_dic[label][1].config(font=("Helvetica", 14), foreground="darkgray")
	entry_dic[label][1].grid(row=row_counter, column=1, pady=5)

	entry_dic[label][2].config(font=("Helvetica", 14), foreground="darkgray")
	entry_dic[label][2].grid(row=row_counter, column=2, pady=5)

	row_counter += 1

root.mainloop()