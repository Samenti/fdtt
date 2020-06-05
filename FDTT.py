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

# make root widget
root = tk.Tk()
root.title("Finnish Declension Tables Tester")

# globals and contants
TEMPLATE = ("nominative", "genitive", "accusative", "partitive", "illative", "inessive",
"allative", "adessive", "elative", "ablative", "essive", "abessive",
"translative", "instructive", "comitative", "nominative_pl", "genitive_pl", "accusative_pl", "partitive_pl", "illative_pl", "inessive_pl",
"allative_pl", "adessive_pl", "elative_pl", "ablative_pl", "essive_pl", "abessive_pl",
"translative_pl", "instructive_pl", "comitative_pl", "english")
title_var = tk.StringVar()
word_var = tk.StringVar()
word_counter = 10
max_words = 10
words = None
points = 0

declension_tables = [(
	'äiti', 'äidin', ('äiti', 'äidin'), 'äitiä', 'äitiin', 'äidissä',
	'äidille', 'äidillä', 'äidistä', 'äidiltä', 'äitinä', 'äidittä', 'äidiksi', '', '',
	'äidit', 'äitien', 'äidit', 'äitejä', 'äiteihin', 'äideissä',
	'äideille', 'äideillä', 'äideistä', 'äideiltä', 'äiteinä', 'äideittä', 'äideiksi', 'äidein', 'äiteineen', 'mother'
	), ('sokeri', 'sokerin', ('sokeri', 'sokerin'), 'sokeria', 'sokeriin', 'sokerissa',
	'sokerille', 'sokerilla', 'sokerista', 'sokerilta', 'sokerina', 'sokeritta', 'sokeriksi', '', '',
	'sokerit', ('sokerien', 'sokereiden', 'sokereitten'), 'sokerit', ('sokereita', 'sokereja'), 'sokereihin', 'sokereissa',
	'sokereille', 'sokereilla', 'sokereista', 'sokereilta', 'sokereina', 'sokereitta', 'sokereiksi', 'sokerein', 'sokereineen', 'sugar'
	), ('suola', 'suolan', ('suola', 'suolan'), 'suolaa', 'suolaan', 'suolassa',
	'suolalle', 'suolalla', 'suolasta', 'suolalta', 'suolana', 'suolatta', 'suolaksi', '', '',
	'suolat', ('suolojen', 'suolainrare'), 'suolat', 'suoloja', 'suoloihin', 'suoloissa',
	'suoloille', 'suoloilla', 'suoloista', 'suoloilta', 'suoloina', 'suoloitta', 'suoloiksi', 'suoloin', 'suoloineen', 'salt')]


# make frames and labels
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

labels = [
"nominative", "genitive", "accusative", "partitive", "illative", "inessive",
"allative", "adessive", "elative", "ablative", "essive", "abessive",
"translative", "instructive", "comitative"
]

# create Label widgets from labels, assign them grid positions
row_counter = 1
for label in labels:
	lab = tk.Label(frm_table)
	lab.config(text=label, font=("Helvetica", 14), background="light steel blue")
	lab.grid(row=row_counter, column=0, sticky=tk.W, pady=5, padx=50)
	row_counter += 1

mapping = []
for column_idx in range(2):
	row_counter = 1
	for label in labels:
		entry = tk.Entry(frm_table)
		entry.config(
		font=("Helvetica", 14),
		insertbackground="darkgray", insertontime=500, insertofftime=500,
		readonlybackground="light steel blue"
		)
		entry.grid(row=row_counter, column=column_idx+1, pady=5, padx=50)
		mapping.append(entry)
		row_counter += 1

frm_info = tk.Frame(root, bg="steel blue", pady=5)
frm_info.pack()
lbl_info = tk.Label(frm_info)
info_text = str(word_counter-1) + " more words in the deck. 0/" + str(word_counter) + " declensions done. Points: " + str(points)
lbl_info.config(text=info_text, font=("Helvetica", 14), background="steel blue")
lbl_info.pack()

frm_toolbar = tk.Frame(root, bg="steel blue", pady=20)
frm_toolbar.pack(anchor=tk.N)
btn_skip = tk.Button(frm_toolbar, text="Skip", width=10)
btn_skip.pack()

def end_game():
	"""
	Runs when the game has run out of words.
	"""
	global info_text, word_counter
	word_counter -= 1
	info_text = str(word_counter) + " more words in the deck. " + str(max_words - word_counter) + "/" + str(max_words) + " declensions done. Points: " + str(points) + " New game?"
	lbl_info.config(text=info_text)
	btn_skip.config(text="New Game", width=15)
	btn_skip.bind("<Button-1>", init_game)



def get_next_word(event):
	"""
	Event handler for a skip button. It jumps to the next declension table.
	It's also used upon initialization.
	"""

	global words, answers, answered, word_var, title_var
	global info_text, word_counter, start_flag

	if word_counter == 1:
		end_game()
		return
	answers = words.pop()
	answered = [False for answer in answers]
	answered[0] = True
	word_var.set(answers[0])
	title_var.set(answers[0] + "   –   " + answers[30])
	mapping[0].config(
	textvariable=word_var, state="readonly", fg="green4"
	)
	if answers[13] == '':
		mapping[13].insert(0, "–")
		mapping[13].config(state="readonly", justify=tk.CENTER)
		answered[13] = True
	if answers[14] == '':
		mapping[14].insert(0, "–")
		mapping[14].config(state="readonly", justify=tk.CENTER)
		answered[14] = True

	if not start_flag:
		word_counter -= 1
	info_text = str(word_counter-1) + " more words in the deck. " + str(max_words - word_counter) + "/" + str(max_words) + " declensions done. Points: " + str(points)
	lbl_info.config(text=info_text)
	start_flag = False
	print "frm_table.grid_bbox()[2]", frm_table.grid_bbox()[2]
	resize_frames(frm_table.grid_bbox()[2])


def init_game(event):
	"""
	Function to help initialize a game.
	"""
	global max_words, word_counter, words
	global points, start_flag
	max_words = len(declension_tables)
	if max_words < word_counter:
		words = random.sample(declension_tables, max_words)
		word_counter = max_words
	else:
		words = random.sample(declension_tables, word_counter)
		max_words = word_counter

	points = 0
	start_flag = True
	get_next_word("<Button-1>")

	


def print_stuff(event):
	"""Print some info while in root.mainloop()"""
	print "frm_table.grid_bbox()", frm_table.grid_bbox()

def return_press(event):
	"""
	Event handler for an 'Enter key' press.
	"""
	current_widget = root.focus_get()
	if isinstance(current_widget, tk.Entry):
		input_text = current_widget.get()
		print input_text
		answer_idx = mapping.index(current_widget)
		print answers[answer_idx]
		print input_text
		if answers[answer_idx] == input_text:
			print "YAY!"
		else:
			print "INCORRECT!"



def resize_frames(window_width):
	"""
	Function that resizes the title based on width of the title words
	and the desired width of the window ('window_width').
	"""
	label_width = lbl_title.winfo_reqwidth()
	print label_width
	frm_title.config(padx = (window_width - label_width) / 2) 
	frm_table.config(padx = (window_width - frm_table.grid_bbox()[2]) / 2)
	label_width = lbl_info.winfo_reqwidth()
	print label_width
	frm_info.config(padx = (window_width - label_width) / 2)
	button_width = btn_skip.winfo_reqwidth()
	print button_width
	frm_toolbar.config(padx = (window_width - button_width) / 2)


root.bind("<Return>", return_press)
btn_skip.bind("<Button-1>", get_next_word)
root.wait_visibility()
init_game("<Button-1")
root.mainloop()