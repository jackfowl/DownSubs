
import unittest
from open_subtitles import OpenSubtitles

class TestParseFunctions(unittest.TestCase):
    def test_search_movie(self):
        open_subtitles = OpenSubtitles()
        open_subtitles.get_token('', '')
        result = open_subtitles.search(query='Dexter', season=1, episode=1)
        self.assertTrue(len(result) > 0) 

