import numpy as np
import h5py

def np2str(n):
    return [bytes.decode(s) for s in n] if n.size>1 else n.astype(str)

def load_h5(filename):
    f = h5py.File(filename,'r')
    __dict__=dict((k,v[()]) for k,v in zip(f.keys(), f.values()))
    for k,v in zip(__dict__.keys(), __dict__.values()):
        if type(v) == np.bytes_:
            __dict__[k] = str(np.char.decode(v))
        elif type(v) == bytes:
            __dict__[k] = v.decode()
        elif type(v)==np.ndarray and v.dtype.char=='S':
            __dict__[k] = np2str(v)
    f.close()
    return __dict__

# db = load_h5('55-4_training.h5')
# print(db.keys())