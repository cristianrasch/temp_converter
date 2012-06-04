# -*- coding: UTF-8 -*-

import gtk
import os
import sys

from lib.conversion import *

class App(object):
    def __init__(self):
        self.build_from_glade_file()
        self.configure_spin_buttons()
        
    def build_from_glade_file(self):
        self.builder = gtk.Builder()
        curr_dir = os.path.dirname(__file__)
        glade_xml = os.path.join(curr_dir, "app.glade")
        self.builder.add_from_file(glade_xml)
        self.builder.connect_signals(self)
        
    def configure_spin_buttons(self):
        farenheit_adj = gtk.Adjustment(lower=0, upper=212, step_incr=1, page_incr=10)
        self.farenheit = self.builder.get_object("farenheit")
        self.farenheit.set_adjustment(farenheit_adj)
        self.farenheit.set_value(32)
        
        celcius_adj = gtk.Adjustment(lower=-18, upper=100, step_incr=1, page_incr=10)
        self.celcius = self.builder.get_object("celcius")
        self.celcius.set_adjustment(celcius_adj)

        self.last_one_changed = self.farenheit
        
    def run(self):
        gtk.main()
        
    def on_spin_button_value_changed(self, widget): 
        self.last_one_changed = widget
        
    def on_convert_clicked(self, widget):
        degrees = self.last_one_changed.get_value()
        if self.last_one_changed == self.farenheit:
            self.celcius.set_value(farenheit_to_celcius(degrees))
        else:
            self.farenheit.set_value(celcius_to_farenheit(degrees))
    
    def on_main_window_delete_event(self, widget, data=None):
        gtk.main_quit()
        return False
    
    def on_quit_clicked(self, widget):
        self.on_main_window_delete_event(widget)
