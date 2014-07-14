
import unittest
import file_util

class TestParseFunctions(unittest.TestCase):
    def test_parse_exception(self):
        self.assertRaises(file_util.FileNameParseError,
            file_util.parse_name,
            'episode.avi')

    def test_parse_extended_pattern(self):
        file_meta = file_util.parse_name('Misfists_s04e04_1080p.avi')
        self.assertEqual(file_meta, {'name': 'Misfists', 
            'season': 4, 
            'episode': 4})

    def test_parse_extended_br_pattern(self):
        file_meta = file_util.parse_name('Supernatural_t01e01_720p.mkv')

        self.assertEqual(file_meta, {'name': 'Supernatural', 
            'season': 1, 
            'episode': 1})

    def test_parse_simple_pattern(self):
        file_meta = file_util.parse_name('Bones.s01e04.LQ.avi')

        self.assertEqual(file_meta, {'name': 'Bones', 
            'season': 1, 
            'episode': 4})

    def test_parse_short_pattern(self):
        file_meta = file_util.parse_name('Bones.01x03.avi')

        self.assertEqual(file_meta, {'name': 'Bones', 
            'season': 1, 
            'episode': 3})

