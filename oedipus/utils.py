from django.conf import settings
import defaults
import os.path
import pickle

def get_default( var_name ):
    """Returns default or overriden global settings"""
    if getattr(settings, var_name, None):
        return getattr(settings, var_name)
    return getattr(defaults, var_name)

def get_pickle( page_name ):
    """Returns deserialized data or None"""
    sphinx_root = get_default('SPHINX_ROOT')
    data_file = '%(root)s/build/pickle/%(file_root)s.fpickle' % {'root':sphinx_root, 'file_root':page_name}
    if not os.path.exists(data_file):
        return None
    data = pickle.load( open(data_file) )
    return data
