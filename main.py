#!/usr/bin/env python

# -*- coding: UTF-8 -*-

import sys
from ui.app import App

required_libs_present = True

try:  
    import pygtk  
    pygtk.require("2.0")  
except:
    err = "PyGTK not availible"
    required_libs_present = False

try:  
    import gtk  
    import gtk.glade  
except:  
    required_libs_present = False
    err = "GTK not availible"

if not required_libs_present:
    print(err)
    sys.exit(1)

if __name__ == "__main__":
    application = App()
    application.run()
