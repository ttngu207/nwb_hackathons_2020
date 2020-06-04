import os
import datajoint as dj
import pathlib

os.environ['DJ_SUPPORT_ADAPTED_TYPES'] = 'TRUE'
os.environ['DJ_SUPPORT_FILEPATH_MANAGEMENT'] = 'TRUE'

dj.config['stores']['nwb_store']['stage'] = pathlib.Path(dj.config['stores']['nwb_store']['stage']).resolve().as_posix()
dj.config['stores']['nwb_store']['location'] = pathlib.Path(dj.config['stores']['nwb_store']['location']).resolve().as_posix()
