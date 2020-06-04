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

word_var=tk.StringVar()
word_var.set("<current word>")
english_var=tk.StringVar()
english_var.set("<English translation>")

lbl_title_word = tk.Label(root, font=("Helvetiva", 32), textvariable=word_var)
lbl_title_word.grid(row=0, column=0)
lbl_title_dash = tk.Label(root, text=" – ", font=("Helvetiva", 32))
lbl_title_dash.grid(row=0, column=1)
lbl_title_english = tk.Label(root, font=("Helvetiva", 32), textvariable=english_var)
lbl_title_english.grid(row=0, column=2)

lbl_table_null = tk.Label(root, text="", font=("Helvetiva", 14))
lbl_table_null.grid(row=1, column=0)
lbl_table_sg = tk.Label(root, text="singular", font=("Helvetiva", 14))
lbl_table_sg.grid(row=1, column=1)
lbl_table_pl = tk.Label(root, text="plural", font=("Helvetiva", 14))
lbl_table_pl.grid(row=1, column=2)

table_dic = {}
labels = [
"nominative", "genitive", "accusative", "partitive", "illative", "inessive",
"allative", "adessive", "elative", "ablative", "essive", "abessive",
"translative", "instructive", "comitative"
]

row_counter = 2
for label in labels:
	table_dic[label] = (tk.Label(root), tk.Entry(root), tk.Entry(root))

	table_dic[label][0].config(text=label, font=("Helvetica", 14))
	table_dic[label][0].grid(row=row_counter, column=0, sticky=tk.W, padx=100)

	table_dic[label][1].config(
		font=("Helvetica", 14), foreground="darkgray",
		insertbackground="darkgray", insertontime=500, insertofftime=500
	)
	table_dic[label][1].grid(row=row_counter, column=1, pady=5)

	table_dic[label][2].config(
		font=("Helvetica", 14), foreground="darkgray",
		insertbackground="darkgray", insertontime=500, insertofftime=500
		)
	table_dic[label][2].grid(row=row_counter, column=2, pady=5)

	row_counter += 1

table_dic["nominative"][1].config(
	textvariable=word_var, state="readonly", fg="green4"
	)
table_dic["instructive"][1].insert(0, "–")
table_dic["comitative"][1].insert(0, "–")
table_dic["instructive"][1].config(state="readonly", justify=tk.CENTER)
table_dic["comitative"][1].config(state="readonly", justify=tk.CENTER)

root.mainloop()