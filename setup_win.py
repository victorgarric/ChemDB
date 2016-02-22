from distutils.core import setup
import py2exe
import os, sys
from glob import glob
import PyQt5

data_files=[('',['C:/Python34/DLLs/sqlite3.dll','C:/Python34/Lib/site-packages/PyQt5/icuuc53.dll','C:/Python34/Lib/site-packages/PyQt5/icudt53.dll','C:/Python34/Lib/site-packages/PyQt5/icuin53.dll','C:/Python34/Lib/site-packages/PyQt5/Qt5Gui.dll','C:/Python34/Lib/site-packages/PyQt5/Qt5Core.dll','C:/Python34/Lib/site-packages/PyQt5/Qt5Widgets.dll']),
('data',['data/configure','data/model.sqlite','data/loading.jpg']),
('platforms',['C:/Python34/Lib/site-packages/PyQt5/plugins/platforms/qminimal.dll','C:/Python34/Lib/site-packages/PyQt5/plugins/platforms/qoffscreen.dll','C:/Python34/Lib/site-packages/PyQt5/plugins/platforms/qwindows.dll'])
]
qt_platform_plugins = [("platforms", glob(PyQt5.__path__[0] + r'\plugins\platforms\*.*'))]
data_files.extend(qt_platform_plugins)
msvc_dlls = [('.', glob(r'''C:/Windows/System32/msvc?100.dll'''))]
data_files.extend(msvc_dlls)

setup( 
    windows = ["ChemDB.py"], 
    zipfile = None, 
    data_files = data_files,
    options = {
        'py2exe': {
            'includes' : ['sip','PyQt5.QtCore','PyQt5.QtGui',"sqlite3",'xlrd','xlwt',"_sqlite3","PyQt5"],
        }
    }, 
) 