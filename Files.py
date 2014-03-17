import struct
import os

LONG_LONG_FORMAT = 'q'
WORD_SIZE = 65536
BYTESIZE = struct.calcsize(LONG_LONG_FORMAT)
STEPS = int(WORD_SIZE / BYTESIZE)

class FileTooSmallError(IOError):
    pass

def hash_step(handle, value):
    for x in xrange(STEPS):
        buff = handle.read(BYTESIZE)
        (low_value,) = struct.unpack(LONG_LONG_FORMAT, buff)
        value += low_value
        value &= 0xFFFFFFFFFFFFFFFF # to remain as 64bit number  
    return value

def hash_file(handle, filesize):
    value = hash_handle(handle, filesize)
    handle.seek(max(0, filesize - WORD_SIZE), 0)
    value = hash_handle(handle, value)
    return {'hash': "%016x" % (value),
            'size': filesize}

def hash_size(path):
    filesize = os.path.getsize(path)
    if filesize < (WORD_SIZE * 2):
        raise FileTooSmallError('File too small to hash')

    with open(path, 'rb') as handle:
        hash_file(handle, filesize)

