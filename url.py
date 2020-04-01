# coding=utf-8

import os
import sys

from handlers import HelloworldHandlers

handlers = [
    (r"/", HelloworldHandlers),
]