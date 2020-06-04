# coding: utf-8

"""
Finnish Declension Tables Tester
--------------------------------
This is a simple GUI-based python program that helps with
learning Finnish nominal declension tables.
"""

# Max line length w/ --- w/o flowing text blocks (PEP 8 style guide): 72 --- 79

import Tkinter as tk
import random

declension_tables = [(
	'äiti', 'äidin', 'äiti', 'äidin', 'äitiä', 'äitiin', 'äidissä',
	'äidille', 'äidillä', 'äidistä', 'äidiltä', 'äitinä', 'äidittä', 'äidiksi', '', '',
	'äidit', 'äitien', 'äidit', '', 'äitejä', 'äiteihin', 'äideissä',
	'äideille', 'äideillä', 'äideistä', 'äideiltä', 'äiteinä', 'äideittä', 'äideiksi', 'äidein', 'äiteineen', 'mother'
	), ('sokeri', 'sokerin', 'sokeri', 'sokerin', 'sokeria', 'sokeriin', 'sokerissa',
	'sokerille', 'sokerilla', 'sokerista', 'sokerilta', 'sokerina', 'sokeritta', 'sokeriksi', '', '',
	'sokerit', ('sokerien', 'sokereiden', 'sokereitten'), 'sokerit', '', ('sokereita', 'sokereja'), 'sokereihin', 'sokereissa',
	'sokereille', 'sokereilla', 'sokereista', 'sokereilta', 'sokereina', 'sokereitta', 'sokereiksi', 'sokerein', 'sokereineen', 'sugar'
	), ('suola', 'suolan', 'suola', 'suolan', 'suolaa', 'suolaan', 'suolassa',
	'suolalle', 'suolalla', 'suolasta', 'suolalta', 'suolana', 'suolatta', 'suolaksi', '', '',
	'suolat', ('suolojen', 'suolainrare'), 'suolat', '', 'suoloja', 'suoloihin', 'suoloissa',
	'suoloille', 'suoloilla', 'suoloista', 'suoloilta', 'suoloina', 'suoloitta', 'suoloiksi', 'suoloin', 'suoloineen', 'salt')]

root = tk.Tk()
root.title("Finnish Declension Tables Tester")
title_var = tk.StringVar()
word_var = tk.StringVar()

frm_title = tk.Frame(root, bg="steel blue")
frm_title.pack()
lbl_title = tk.Label(frm_title, font=("Helvetica", 32), textvariable=title_var, bg="steel blue")
lbl_title.pack()

frm_table = tk.Frame(root, pady=50, bg="light steel blue")
frm_table.pack()

lbl_table_null = tk.Label(frm_table, text="", font=("Helvetica", 14), background="light steel blue")
lbl_table_null.grid(row=0, column=0)
lbl_table_sg = tk.Label(frm_table, text="singular", font=("Helvetica", 14), background="light steel blue")
lbl_table_sg.grid(row=0, column=1)
lbl_table_pl = tk.Label(frm_table, text="plural", font=("Helvetica", 14), background="light steel blue")
lbl_table_pl.grid(row=0, column=2)

table_dic = {}
labels = [
"nominative", "genitive", "accusative", "partitive", "illative", "inessive",
"allative", "adessive", "elative", "ablative", "essive", "abessive",
"translative", "instructive", "comitative"
]


# to maintain correct tab-order (going from top to bottom then left to right)
# I made 3 separate loops to create the labels and the entries;
# previous solution commented out further down
row_counter = 1
for label in labels:
	table_dic[label] = []
	table_dic[label].append(tk.Label(frm_table))
	table_dic[label][0].config(text=label, font=("Helvetica", 14), background="light steel blue")
	table_dic[label][0].grid(row=row_counter, column=0, sticky=tk.W, pady=5, padx=50)
	row_counter += 1

row_counter = 1
for label in labels:
	table_dic[label].append(tk.Entry(frm_table))
	table_dic[label][1].config(
		font=("Helvetica", 14),
		insertbackground="darkgray", insertontime=500, insertofftime=500,
		readonlybackground="light steel blue"
	)
	table_dic[label][1].grid(row=row_counter, column=1, pady=5)
	row_counter += 1

row_counter = 1
for label in labels:
	table_dic[label].append(tk.Entry(frm_table))
	table_dic[label][2].config(
		font=("Helvetica", 14),
		insertbackground="darkgray", insertontime=500, insertofftime=500,
		readonlybackground="light steel blue"
		)
	table_dic[label][2].grid(row=row_counter, column=2, pady=5, padx=50)
	row_counter += 1

# for label in labels:
# 	table_dic[label] = (tk.Label(frm_table), tk.Entry(frm_table), tk.Entry(frm_table))

# 	table_dic[label][0].config(text=label, font=("Helvetica", 14), background="light steel blue")
# 	table_dic[label][0].grid(row=row_counter, column=0, sticky=tk.W, pady=5, padx=50)

# 	table_dic[label][1].config(
# 		font=("Helvetica", 14),
# 		insertbackground="darkgray", insertontime=500, insertofftime=500,
# 		readonlybackground="light steel blue"
# 	)
# 	table_dic[label][1].grid(row=row_counter, column=1, pady=5)

# 	table_dic[label][2].config(
# 		font=("Helvetica", 14),
# 		insertbackground="darkgray", insertontime=500, insertofftime=500,
# 		readonlybackground="light steel blue"
# 		)
# 	table_dic[label][2].grid(row=row_counter, column=2, pady=5, padx=50)

# 	row_counter += 1

def init_game():
	"""
	Function to help initialize a game.
	"""
	global words, answers, answered, word_var, title_var
	max_words = len(declension_tables)
	if max_words < 10:
		words = random.sample(declension_tables, max_words)
	else:
		words = random.sample(declension_tables, 10)

	# print words
	answers = words.pop()
	# print answers
	answered = [False for answer in answers]
	answered[0] = True
	word_var.set(answers[0])
	title_var.set(answers[0] + "   –   " + answers[32])
	table_dic["nominative"][1].config(
	textvariable=word_var, state="readonly", fg="green4"
	)
	if answers[13] == '':
		table_dic["instructive"][1].insert(0, "–")
		table_dic["instructive"][1].config(state="readonly", justify=tk.CENTER)
		answered[13] = True
	if answers[14] == '':
		table_dic["comitative"][1].insert(0, "–")
		table_dic["comitative"][1].config(state="readonly", justify=tk.CENTER)
		answered[14] = True

def print_stuff(event):
	"""Print some info while in root.mainloop()"""
	print "frm_table.grid_bbox()", frm_table.grid_bbox()

def return_press(event):
	"""
	Event handler for an 'Enter key' press.
	"""

	

def tab_press(event):
	"""
	Event handler for a 'tab key' press.
	"""
	pass

def resize_title(window_width):
	"""
	Function that resizes the title based on width of the title words
	and the desired width of the window ('window_width').
	"""
	label_width = lbl_title.winfo_reqwidth()
	frm_title.config(padx = (window_width - label_width) / 2) 
	frm_table.config(padx = (window_width - frm_table.grid_bbox()[2]) / 2)


init_game()
root.bind("<Return>", print_stuff)
root.wait_visibility()
print frm_table.grid_bbox()[2]
resize_title(frm_table.grid_bbox()[2])
root.mainloop()