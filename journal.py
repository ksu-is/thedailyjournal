# -*- coding: utf-8 -*-

from Tkinter import *
import tkFileDialog
from datetime import *
import random
import bisect
import json
import cPickle as pickle
import os.path

#============================================================

APP_WIDTH, APP_HEIGHT = 600,600

DATE_FORMAT = "%d/%m/%Y"
DATE_FORMAT_ORDERED = "%Y%m%d"

DEFAULT_DIR = "./"
DEFAULT_EXTENSION = ".jrn"

#============================================================
master = Tk()
master.geometry('{}x{}'.format(APP_WIDTH, APP_HEIGHT))

def date_s_to_o(sdate, _format=DATE_FORMAT):
	return datetime.strptime(sdate, _format)

def date_o_to_s(odate, _format=DATE_FORMAT):
	return odate.strftime(_format)

def stoday():
	return date_o_to_s(datetime.today())

#============================================================

class DialogRename:
	def __init__(self, parent, default):
		top = self.top = Toplevel(parent)
		self.value = default

		Label(top, text="Enter name for journal").pack()

		self.e = Entry(top)
		self.bok = Button(top, text="OK", command=self.ok)
		self.bcancel = Button(top, text="Cancel", command=self.cancel)
		self.e.insert(0, default)
		self.e.focus()

		self.e.pack(padx=5)
		self.bok.pack(pady=5,padx=10,side=LEFT,ipadx=10)
		self.bcancel.pack(pady=5,padx=10,side=RIGHT,ipadx=5)

	def ok(self):
		self.value = self.e.get()
		self.top.destroy()

	def cancel(self):
		self.top.destroy()

#============================================================
class JournalEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Journal):
			return [obj.name,  [ob.__dict__ for ob in obj.entries]]
		return json.JSONEncoder.default(self, obj) # Let the base class default method raise the TypeError

class JEntryDecoder(json.JSONDecoder):
	def __init__(self, *args, **kargs):
		json.JSONDecoder.__init__(self, object_hook=self.dict_to_object, *args, **kargs)

	def decode_json(self, jobj):
		j = Journal(jobj[0])
		j.entries = [JEntry(j[1]['date'], j[1]['text']) for entry in j[1]]
		return j

	def dict_to_object(self, d): 
		return (d['date'], d['text'], d['id'])

#============================================================
class JEntry(object):
	def __init__(self, date, text):
		self.date=date
		self.text=text
		self.id=date_o_to_s(date_s_to_o(date), DATE_FORMAT_ORDERED)

	def __lt__(self, other): return self.id < other.id
	def __gt__(self, other): return self.id > other.id
	def __eq__(self, other): return self.id == other.id
	def __repr__(self): return self.date+":"+self.text[0:15]
#============================================================
class Journal(object):

	def __init__(self, name="My Journal"):
		self.name = name
		self.entries = []

	def size(self):
		return len(self.entries)

	def check_format(self, date):
		try:
			date_s_to_o(date)
		except ValueError:
			raise ValueError("Incorrect date format, should be "+DATE_FORMAT)


	def add_entry(self, date, text=""):
		self.check_format(date)
		bisect.insort(self.entries, JEntry(date, text))

	# return index of entry with given date, (-1) if not found
	def find_entry(self, date):
		idate = bisect.bisect_left(self.entries, JEntry(date,""))
		if idate == len(self.entries) or self.entries[idate].date != date:
			return -1
		return idate

	def edit_entry(self, date, text):
		self.check_format(date)
		idate = self.find_entry(date)
		if idate == -1:
			self.add_entry(date, text)
		else:
			self.entries[idate].text = text


class JournalDisplay(Journal):
	"""docstring for Journal"""
	def __init__(self, name="My Journal", file_path=None):
		super(JournalDisplay, self).__init__(name)
		self.file_path = file_path
		self.name = name
		self.text = Text(master)
		self.date = Label(master)
		self.back = Button(master, text="◀")
		self.next = Button(master, text="▶")
		self.rename(name)
		self.init_grid()
		self.init_events()
		self.set_date()


	def init_grid(self):
		# putting objects on grid
		self.back.grid(row=0, column=0, sticky=W)
		self.date.grid(row=0, column=0, sticky=W+E)
		self.next.grid(row=0, column=0, sticky=E)

		self.text.grid(row=1, column=0, sticky=W+E+N+S, padx=10, pady=10)

		# configurations
		self.back.configure(font="Arial 15", width=4)
		self.date.configure(font="Arial 15")
		self.next.configure(font="Arial 15", width=4)

		self.text.configure(font="Arial 12", wrap=WORD)

		master.grid_rowconfigure(1, weight=1)
		master.grid_columnconfigure(0, weight=1)

	def init_events(self):
		self.back.configure(command=self.cb_back)
		self.next.configure(command=self.cb_next)

		master.bind('<Control-r>', self.cb_rename)
		master.bind('<Control-s>', self.cb_save) 
		master.bind('<Control-l>', self.cb_load) # L not 1
		master.bind('<Control-o>', self.cb_load) # open = load

	def get_stext(self):
		return str(self.text.get("1.0",END))[:-1] # DUE TO BUG in get method, it adds \n so i need to strip it

	def get_sdate(self): # get the string of a date of current entry
		return str(self.date['text'])

	def get_odate(self): # get the object of a date of current entry
		return date_s_to_o(self.get_sdate())

	def set_date(self, sdate=None):
		self.date['text'] = stoday() if sdate is None else sdate

	def set_text(self, stext=""):
		self.text.delete(1.0, END)
		self.text.insert(END, stext)

	def update_text(self):
		self.edit_entry(self.date['text'], self.get_stext())

	# setting the current journal to point to today entry. if doesnt exist creates it (happens when loading older journal)
	def set_today(self):
		date = stoday()
		self.set_journal_day(date)

	# set the journal graphics to given indexed entry in the journal
	def set_journal_day_i(self, idate):
		self.set_date(self.entries[idate].date)
		self.set_text(self.entries[idate].text)		

	# set the journal graphics to given date, creating it if not exist
	def set_journal_day(self, date):
		idate = self.find_entry(date)
		if idate == -1:
			self.add_entry(date)
			idate = self.find_entry(date)
		self.set_journal_day_i(idate)

	def day_back(self):
		self.set_journal_day(date_o_to_s(self.get_odate() - timedelta(days=1)))

	def day_next(self):
		self.set_journal_day(date_o_to_s(self.get_odate() + timedelta(days=1)))

	def rename(self, value=None):
		if value is None:
			d = DialogRename(master, self.name)
			d.top.grab_set()
			master.wait_window(d.top)
			value = d.value
		self.name = value
		self.file_path = DEFAULT_DIR + self.name + DEFAULT_EXTENSION #if self.file_path is None else self.file_path
		master.title(self.name)

	#=== save/load journal ===#
	def decode_json(self, f):
		jobj = json.load(f,cls=JEntryDecoder)
		j = Journal(jobj[0])
		j.entries = [JEntry(entry[0], entry[1]) for entry in jobj[1]]
		return j

	def load(self, file_name=None):
		f = tkFileDialog.askopenfile(mode='r') if file_name is None else open(file_name, "r")
		if f is None: return
		decoded_journal = self.decode_json(f)
		self.name = decoded_journal.name
		self.entries = decoded_journal.entries
		f.close()
		self.set_today()
		self.rename(self.name)

	def save(self):
		self.update_text()
		#f = tkFileDialog.asksaveasfile(mode='w', defaultextension=".json") if self.file_path is None else open(self.file_path, "w")
		f = open(self.file_path, "w")
		if f is not None: # asksaveasfile return `None` if dialog closed with "cancel"
			text2save = json.dump(self, f, cls=JournalEncoder) #pickle.dump(self.entries, f)
			f.close()
			self.file_path = f.name


	# callbacks wrappers
	def cb_back(self):
		self.day_back()
	def cb_next(self):
		self.day_next()
	def cb_rename(self, e):
		self.rename()
	def cb_save(self, e):
		self.save()
	def cb_load(self, e):
		self.load()

#============================================================

j = JournalDisplay() 
if os.path.exists(j.file_path):
	j.load(j.file_path)

#============================================================

#============================================================

#============================================================
mainloop()
#
