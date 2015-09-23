#!/usr/bin/python2
# -*- coding: utf-8 -*-

import requests, json
import pygtk, gtk

class PiTime(object):
	def __init__(self):
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_size_request(350, 250)
		self.window.set_position(gtk.WIN_POS_CENTER)
		self.window.set_title("Pi-Corn-Time")

		self.window.connect("delete_event", gtk.main_quit)

		vbox = gtk.VBox(False, 8)
        
		store = self.createListModel()
       	
		treeView = gtk.TreeView(store)
		self.createColumns(treeView)
			
		vbox.pack_start(treeView, True, True, 0)
		
		self.window.add(vbox)
		self.window.show_all()

	def main(self):
		gtk.main()
	
	def createListModel(self):
		
		store = gtk.ListStore(str, int, float, str)
		
		url = "https://yts.to/api/v2/list_movies.json"
		res = requests.get(url)
		dic = res.json()
		
		for i in range(20):
			mov = dic['data']['movies'][i]
			store.append([mov['title'], mov['year'], mov['rating'], mov['language']])
			
		return store
	
	def createColumns(self, treeView):
	
		rendererText = gtk.CellRendererText()
		col = gtk.TreeViewColumn("Movie", rendererText, text=0)
		col.set_sort_column_id(0)
		treeView.append_column(col)
		
		rendererText = gtk.CellRendererText()
		col = gtk.TreeViewColumn("Year", rendererText, text=1)
		col.set_sort_column_id(1)
		treeView.append_column(col)
		
		rendererText = gtk.CellRendererText()
		col = gtk.TreeViewColumn("Rating", rendererText, text=2)
		col.set_sort_column_id(2)
		treeView.append_column(col)
		
		rendererText = gtk.CellRendererText()
		col = gtk.TreeViewColumn("Language", rendererText, text=3)
		col.set_sort_column_id(3)
		treeView.append_column(col)	

PiTime = PiTime()
PiTime.main()
