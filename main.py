'''
@Description:
@Author: michael
@Date: 2020-12-09 19:48:20
LastEditTime: 2020-12-29 20:00:00
LastEditors: michael
'''

# coding=utf-8

import uvicorn
from fastapi import FastAPI
from routers import User
from routers import Verify
from routers import PrivateMessage
from routers import MyInfo
from routers import FilesShare
from routers import FriendRequest
from routers import NewsOperation
from routers import GpOperation
from routers import Check
from routers import Bookmarked

from routers import ThirdPartyRouter

from routers import OssOperationRouter
from routers import OsLocalOperation

from routers import WebOperationRouter

from routers import MessageList
from routers import LeaveMessage


from routers import OtherRouter

from routers import TestRouter

# 测试
# from fastapi import FastAPI, Request, Path, Query, Header
# from fastapi.exceptions import RequestValidationError
# from fastapi.responses import JSONResponse

app = FastAPI()

# 测试路由 - 暂时废弃
app.include_router(TestRouter.router)

# 用户路由
app.include_router(User.router)

# 发送邮件验证码和验证路由
app.include_router(Verify.router)

# 发送私聊和已读取私聊路由
app.include_router(PrivateMessage.router)

# 我的消息列表页路由
app.include_router(MyInfo.router)

# 文件共享路由
app.include_router(FilesShare.router)

# 好友请求路由
app.include_router(FriendRequest.router)

# GP详情页请求路由
app.include_router(GpOperation.router)

# 收藏请求路由
app.include_router(Check.router)

# 收藏请求路由
app.include_router(Bookmarked.router)

# 新闻请求路由
app.include_router(NewsOperation.router)

# 消息列表 分页 路由
app.include_router(MessageList.router)

# 留言请求路由
app.include_router(LeaveMessage.router)

# 云信账号路由 - 内部用
app.include_router(ThirdPartyRouter.router)

# 阿里云 OSS 路由 - 内部用
app.include_router(OssOperationRouter.router)

# 本地 OS 路由 - 内部用
app.include_router(OsLocalOperation.router)

# web 端操作路由
app.include_router(WebOperationRouter.router)


# 测试开发新的功能的路由 - 内部用
# app.include_router(OtherRouter.router)

# 临时加到上面的接收 POST 请求的一个东西, 用来查看报错后的 request 参数的 - 将来可能会被替换掉
# @app.exception_handler(RequestValidationError)
# async def request_validation_exception_handler(request: Request, exc: RequestValidationError):
#     print(f"参数不对{request.method} {request.url}")
#     print(exc.body)
#     return JSONResponse({"code": "400", "message": exc.errors(),"aaa":str(exc.body)})
