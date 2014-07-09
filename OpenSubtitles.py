import xmlrpclib
import Files

proxy = xmlrpclib.ServerProxy("http://api.opensubtitles.org/xml-rpc")

def GetToken():
	token = ''
	response = proxy.LogIn('', '', 'pb', 'OS Test User Agent')
	if response['status'] == '200 OK':
		token = response['token']
	return token

token = GetToken()


def CreateQuery(hashCode = None, archiveSize = None, movieID = None, name = None, season = None, episode = None, tag = None):
        search = {'sublanguageid':'pb,pob'}
        if (not hashCode is None) and (not movieID is None):
                search['moviehash'] = hashCode
                search['moviebytesize'] = archiveSize
        elif (not movieID is None):
                search['imdbid'] = movieID
        elif (not tag is None):
                search['tag'] = tag
        elif (not name is None):
                search['query'] = name
                if (not season is None):
                        search['season'] = season
                        if (not episode is None):
                                search['episode'] = episode
        return search

def Legendas(fileName):
        result=[]
        episode = (Files.seriesEpisode(fileName))
        print(episode)
        if (episode['error'] is None):
                dados = (proxy.SearchSubtitles(token,[CreateQuery(name=episode['series'],season=episode['season'],episode=episode['episode'])]))#,tag=episode['tag']
                if dados['data']:
                        for elem in dados['data']:
                                result.append({})
                                result[-1]['url']=elem['ZipDownloadLink']
                                result[-1]['name']=elem['SubFileName']
                                #urllib.request.urlretrieve(elem['ZipDownloadLink'], elem['SubFileName']+".zip")
        else:
                raise(episode['error'])
        return result
