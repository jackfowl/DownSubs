

if __name__ == '__main__':
    import unittest
    suite = unittest.TestLoader().discover('./test')
    unittest.TextTestRunner(verbosity=2).run(suite)
