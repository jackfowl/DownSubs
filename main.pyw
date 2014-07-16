#!/usr/bin/env python

import sys

def run_test():
    sys.dont_write_bytecode = True
    import unittest
    suite = unittest.TestLoader().discover('./test')
    unittest.TextTestRunner(verbosity=2).run(suite)

def run_setup():
    from distutils.core import setup
    import py2exe
    setup(console=['application.py'])

def run_main():
    from application import Application
    app = Application()                       
    app.master.title('SubDownloader')    
    app.mainloop()    


if __name__ == '__main__':
    option = 'main'
    if len(sys.argv) > 1:
        option = sys.argv[1]
    options = {
        'test': run_test,
        'setup': run_setup,
        'main': run_main
    }
    options[option]()
       
