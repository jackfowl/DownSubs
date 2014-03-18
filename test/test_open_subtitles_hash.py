
import unittest
import os.path
import open_subtitles_hash

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
RESOURCE_PATH = os.path.join(DIR_PATH, 'resources')

class OpenSubtitleHashTest(unittest.TestCase):
    def download_resource(self, name, url):
        path = os.path.join(RESOURCE_PATH, name)
        if not os.path.isfile(path):
            import urllib2
            response = response = urllib2.urlopen(url)
            with open(path, 'w+') as handle:
                handle.write(response.read())

    def setUp(self):
        self.download_resource('breakdance.avi', 'http://www.opensubtitles.org/addons/avi/breakdance.avi')
        self.download_resource('dummy.rar', 'http://www.opensubtitles.org/addons/avi/dummy.rar')

    def test_hash_breakdance(self):
        resource_path = os.path.join(RESOURCE_PATH, 'breakdance.avi')
        self.assertEqual(open_subtitles_hash.hash_size(resource_path), 
                {'hash': '8e245d9679d31e12',
                'size': 12909756L})

    def test_hash_dummy(self):
        resource_path = os.path.join(RESOURCE_PATH, 'dummy.rar')
        self.assertEqual(open_subtitles_hash.hash_size(resource_path), 
                {'hash': '2a527d74d45f5b1b',
                'size': 2565922L})


