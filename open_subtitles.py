
import xmlrpclib

class TokenException(Exception):
    pass

class OpenSubtitles(object):
    def __init__(self):
        self.proxy = xmlrpclib.ServerProxy("http://api.opensubtitles.org/xml-rpc")
        self.token = None

    def get_token(self, user, passwd):
        response = self.proxy.LogIn(user, passwd, 'pb', 'OS Test User Agent')
        if response['status'] != '200 OK':
            raise TokenException('%s while getting token' % response['status'])
        self.token = response['token']

    def search(self, **kwargs):
        """The possible options are:
            moviehash, moviebytesize, imdbid, tag, query, season, episode"""

        kwargs['sublanguageid'] = 'pb,pob'
        result = self.proxy.SearchSubtitles(self.token, [kwargs])
        if result:
            return map(lambda k: {'url': k['ZipDownloadLink'], 'name': k['SubFileName']}, 
                result['data'])



