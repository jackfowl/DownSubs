
import re

class FileNameParseError(Exception):
    pass

def parse_name(name):
    file_meta = re.search('(\w+)(?:_|\.)(?:s|t)?(\d+)(?:e|x)(\d+)', name)
    if not file_meta: 
        raise FileNameParseError("Can't parse file name %s" % name)
    return {'name': file_meta.group(1),
            'season': int(file_meta.group(2)),
            'episode': int(file_meta.group(3))}
