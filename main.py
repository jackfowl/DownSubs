#!/usr/bin/env python

import sys

if __name__ == '__main__':
    option = sys.argv[1]
    if option == 'test':
        sys.dont_write_bytecode = True
        import unittest
        suite = unittest.TestLoader().discover('./test')
        unittest.TextTestRunner(verbosity=2).run(suite)
    elif option == 'setup':
        from distutils.core import setup
        import py2exe
        setup(console=['Face.pyw'])

