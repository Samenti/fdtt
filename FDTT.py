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
title_str = ""
word_str = ""
word_counter = 10
max_words = 10
words = None
points = 0

declension_tables = [(
	u'äiti', u'äidin', (u'äiti', u'äidin'), u'äitiä', u'äitiin', u'äidissä',
	u'äidille', u'äidillä', u'äidistä', u'äidiltä', u'äitinä', u'äidittä', u'äidiksi', u'', u'',
	u'äidit', u'äitien', u'äidit', u'äitejä', u'äiteihin', u'äideissä',
	u'äideille', u'äideillä', u'äideistä', u'äideiltä', u'äiteinä', u'äideittä', u'äideiksi', u'äidein', u'äiteineen', u'mother'
	), (u'sokeri', u'sokerin', (u'sokeri', u'sokerin'), u'sokeria', u'sokeriin', u'sokerissa',
	u'sokerille', u'sokerilla', u'sokerista', u'sokerilta', u'sokerina', u'sokeritta', u'sokeriksi', u'', u'',
	u'sokerit', (u'sokerien', u'sokereiden', u'sokereitten'), u'sokerit', (u'sokereita', u'sokereja'), u'sokereihin', u'sokereissa',
	u'sokereille', u'sokereilla', u'sokereista', u'sokereilta', u'sokereina', u'sokereitta', u'sokereiksi', u'sokerein', u'sokereineen', u'sugar'
	), (u'suola', u'suolan', (u'suola', u'suolan'), u'suolaa', u'suolaan', u'suolassa',
	u'suolalle', u'suolalla', u'suolasta', u'suolalta', u'suolana', u'suolatta', u'suolaksi', u'', u'',
	u'suolat', (u'suolojen', u'suolainrare'), u'suolat', u'suoloja', u'suoloihin', u'suoloissa',
	u'suoloille', u'suoloilla', u'suoloista', u'suoloilta', u'suoloina', u'suoloitta', u'suoloiksi', u'suoloin', u'suoloineen', u'salt')]


# make frames and labels
frm_title = tk.Frame(root, bg="steel blue")
frm_title.pack()
lbl_title = tk.Label(frm_title, font=("Helvetica", 32), bg="steel blue")
lbl_title.config(text=title_str)
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
label_mapping = []
row_counter = 1
for label in labels:
	label_mapping.append(tk.Label(frm_table))
	label_mapping[row_counter-1].config(text=label, font=("Helvetica", 14), background="light steel blue")
	label_mapping[row_counter-1].grid(row=row_counter, column=0, sticky=tk.W, pady=5, padx=50)
	row_counter += 1

entry_mapping = []
for column_idx in range(2):
	row_counter = 1
	for label in labels:
		entry = tk.Entry(frm_table)
		entry.config(
		font=("Helvetica", 14),
		insertbackground="black", insertontime=500, insertofftime=500,
		readonlybackground="light steel blue"
		)
		entry.grid(row=row_counter, column=column_idx+1, pady=5, padx=50)
		entry_mapping.append(entry)
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

def change_color_scheme(dark, light):
	"""
	Changes the window's color scheme.
	"""
	frm_title.config(bg=dark)
	lbl_title.config(bg=dark)
	frm_table.config(bg=light)
	lbl_table_null.config(bg=light)
	lbl_table_sg.config(bg=light)
	lbl_table_pl.config(bg=light)
	for idx in range(len(entry_mapping)):
		entry_mapping[idx].config(readonlybackground=light)
	for idx in range(len(label_mapping)):
		label_mapping[idx].config(bg=light)
	frm_info.config(bg=dark)
	lbl_info.config(bg=dark)
	frm_toolbar.config(bg=dark)

def end_game():
	"""
	Runs when the game has run out of words.
	"""
	global info_text, word_counter
	word_counter -= 1
	info_text = str(word_counter) + " more words in the deck. " + str(max_words - word_counter) + "/" + str(max_words) + " declensions done. Points: " + str(points) + " New game?"
	lbl_info.config(text=info_text)
	for idx in range(len(entry_mapping)):
		entry_mapping[idx].config(state="readonly")
	btn_skip.config(text="New Game", width=15)
	btn_skip.bind("<Button-1>", init_game)

	change_color_scheme("forest green", "lime green")
	resize_frames(frm_table.grid_bbox()[2])



def get_next_word(event):
	"""
	Event handler for a skip button. It jumps to the next declension table.
	It's also used upon initialization.
	"""

	global words, answers, answered, word_str, title_str
	global info_text, word_counter, start_flag

	# commence the end of the game if there's no words left
	if word_counter == 1:
		end_game()
		return
	
	# initialize next declension table
	answers = words.pop()
	answered = [False for dummy_idx in range(len(answers)-1)]
	answered[0] = True
	word_str = answers[0]
	title_str = answers[0] + u"   –   " + answers[30]
	lbl_title.config(text=title_str)
	
	# set all entry boxes to be empty
	for idx in range(len(entry_mapping)):
		entry_mapping[idx].config(state=tk.NORMAL, justify=tk.LEFT)
		entry_mapping[idx].delete(0, tk.END)

	# set nominative singular to be solved
	entry_mapping[0].insert(0, word_str)
	entry_mapping[0].config(
		state="readonly", fg="green4", takefocus=0
	)

	# set instructive and comitative singulars to be blank
	if answers[13] == '':
		entry_mapping[13].insert(0, "–")
		entry_mapping[13].config(state="readonly", justify=tk.CENTER, takefocus=0)
		answered[13] = True
	if answers[14] == '':
		entry_mapping[14].insert(0, "–")
		entry_mapping[14].config(state="readonly", justify=tk.CENTER, takefocus=0)
		answered[14] = True

	# set initial focus to be in genitive singular entry box
	entry_mapping[1].focus_set()

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
	word_counter = 10
	max_words = len(declension_tables)
	print "max_words", max_words
	print "word_counter", word_counter
	if max_words < word_counter:
		words = random.sample(declension_tables, max_words)
		word_counter = max_words
	else:
		words = random.sample(declension_tables, word_counter)
		max_words = word_counter

	points = 0
	start_flag = True
	change_color_scheme("steel blue", "light steel blue")
	btn_skip.config(text="Skip", width=10)
	btn_skip.bind("<Button-1>", get_next_word)
	get_next_word("<Button-1>")

def return_press_handler(event):
	"""
	Event handler for an 'Enter key' press.
	"""
	global points, answered

	current_widget = root.focus_get()
	# if focus isn't an Entry widget, do nothing
	if not isinstance(current_widget, tk.Entry):
		return

	input_text = current_widget.get()
	# if the Entry box is empty, do nothing
	if len(input_text) == 0:
		return
	answer_idx = entry_mapping.index(current_widget) # entry_mapping's Entry widgets and the corresponding answers have the same indices

	# handle the fact that there can be multiple correct forms for each answer
	current_answers = []
	if isinstance(answers[answer_idx], tuple):
		current_answers.extend(answers[answer_idx])
	else:
		current_answers.append(answers[answer_idx])

	if input_text in current_answers:
		# if the answer given was correct
		entry_mapping[answer_idx].config(state="readonly", fg="green4", takefocus=0)
		answered[answer_idx] = True
			
		points += 1 # award 1 point for getting an entry right
		info_text = str(word_counter-1) + " more words in the deck. " + str(max_words - word_counter) + "/" + str(max_words) + " declensions done. Points: " + str(points)
		lbl_info.config(text=info_text)
		resize_frames(frm_table.grid_bbox()[2])

		if False not in answered:
			points += 5 # award 5 points for finishing whole declension table
			get_next_word("<Button-1")
			return

		# to find the next focus:
		focus_found = False
		counter = 1
		while not focus_found:
			if not answered[(answer_idx + counter) % 30]:
				entry_mapping[(answer_idx + counter) % 30].focus_set()
				focus_found = True
			else:
				counter += 1
			
	else:
		# if the answer given was incorrect
		entry_mapping[answer_idx].config(fg="red3")

def resize_frames(window_width):
	"""
	Function that resizes the title based on width of the title words
	and the desired width of the window ('window_width').
	"""
	label_width = lbl_title.winfo_reqwidth()
	frm_title.config(padx = (window_width - label_width) / 2) 
	frm_table.config(padx = (window_width - frm_table.grid_bbox()[2]) / 2)
	label_width = lbl_info.winfo_reqwidth()
	frm_info.config(padx = (window_width - label_width) / 2)
	button_width = btn_skip.winfo_reqwidth()
	frm_toolbar.config(padx = (window_width - button_width) / 2)


root.bind("<Return>", return_press_handler)
btn_skip.bind("<Button-1>", get_next_word)
root.wait_visibility()
init_game("<Button-1")
root.mainloop()