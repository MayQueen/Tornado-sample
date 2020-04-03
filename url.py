# coding=utf-8

import os
import sys

from handlers import *
# from handlers import HelloworldHandlers, IndexHandlers, LoginHandlers, UploadHandlers, AccessHandlers, IPAccess, RegisterHadnlers, get_conn

handlers = [
    (r"/helloworld/", HelloworldHandlers),
    (r"/", IndexHandlers),
    (r"/login/", LoginHandlers),
    (r"/upload/", UploadHandlers),
    (r"/access/", AccessHandlers),
    (r"/ipaccess/", IPAccess),
    (r"/register/", RegisterHadnlers, {'conn':get_conn()})
]
