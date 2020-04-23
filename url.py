# coding=utf-8

import os
import sys
import handlers

from handlers.test import HelloworldHandlers
from handlers.Base_Handler import IndexHandlers, LoginHandlers, RegisterHadnlers, get_conn, AdminHandlers, PasswordResetHandlers

handlers = [
    (r"/helloworld/", HelloworldHandlers),
    (r"/", IndexHandlers),
    (r"/admin/", AdminHandlers), # 管理员登录
    (r"/login/", LoginHandlers), # 普通用户登录
    (r"/login/register/", RegisterHadnlers, {'conn':get_conn()}), # 普通用户注册
    (r"/login/reset/", PasswordResetHandlers) # 密码找回
]
