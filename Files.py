import struct, os, re, sys, ntpath

def hashSize(file): 
      try:         
          longlongformat = 'q'  # long long 
          bytesize = struct.calcsize(longlongformat) 
              
          f = open(file, "rb") 
              
          filesize = os.path.getsize(file) 
          hash = filesize 
              
          if filesize < 65536 * 2: 
                 return "SizeError" 
           
          for x in range(int(65536/bytesize)): 
                  buffer = f.read(bytesize) 
                  (l_value,)= struct.unpack(longlongformat, buffer)  
                  hash += l_value 
                  hash = hash & 0xFFFFFFFFFFFFFFFF #to remain as 64bit number  
                   

          f.seek(max(0,filesize-65536),0) 
          for x in range(int(65536/bytesize)): 
                  buffer = f.read(bytesize) 
                  (l_value,)= struct.unpack(longlongformat, buffer)  
                  hash += l_value 
                  hash = hash & 0xFFFFFFFFFFFFFFFF 
           
          f.close() 
          returnedhash =  "%016x" % hash 
          return {'hash':returnedhash,'size':filesize,'error':None} 
    
      except(IOError): 
           return {'hash':None,'size':None,'error':"IOError"}

def seriesEpisode(name):
      default = {'series':None,'season':None,'episode':None,'tag':None,'error':None}
      try:
            result = default.copy()
            fS_E_=r"[sS][0-9]{2}[eE][0-9]{2}"
            fS_=r"[sS][0-9]{2}"
            fE_=r"[eE][0-9]{2}"
            pattern = re.compile(fS_E_)
            parts = pattern.split(name)
            result['series'] = re.sub("[._]", "", parts[0])

            strS_E_ = pattern.findall(name)[0]
            pattern = re.compile(fS_)
            result['season'] = re.sub("[sS]","",pattern.findall(strS_E_)[0])
            

            pattern = re.compile(fE_)
            result['episode'] = re.sub("[eE]","",pattern.findall(strS_E_)[0])
            
            result['tag'] = re.sub("\..{3}$", "", name)
            
      except:
            result = default
            result['error'] = sys.exc_info()
      finally:
            return result
