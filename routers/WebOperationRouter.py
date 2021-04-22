'''
@Description:
@Author: michael
@Date: 2020-04-08 10:54:10
LastEditTime: 2020-04-08 20:00:00
LastEditors: michael
'''
# coding=utf-8

# 第三方包
from fastapi import APIRouter

# 自己创建的包
from views.WebOperation import webOperation

# 加载数据验证模型
from models.OssModel import UrlSignModel

# 加载请求,响应,表单,模块
from fastapi import Response, Request, Form



# 创建 APIRouter 实例
router = APIRouter()




# 网盘文件提取入口验证
@router.get('/api/file/web/web_cloud/{share_id}')
async def webCloud(request:Request, share_id):
    # param = sts_download.__dict__
    print(share_id)
    return await webOperation.returnWebCloud(request, share_id)


# 第三方 OSS - 下载文件 - 注：模拟 APP 端下载过程用的，服务器本身用不上本接口
@router.get('/api/file/web/web_login')
async def webLogin(request:Request):
    return await webOperation.returnwebLogin(request)


# 验证用户登陆
@router.post('/api/file/web/web_login_verify')
async def webLogin(request:Request,
                    username:str=Form(...),  # 直接去请求体里面获取username键对应的值并自动转化成字符串类型
                    password:str=Form(...)  # 直接去请求体里面获取pwd键对应的值并自动转化成整型
):

    print(username)
    print(password)
    return await webOperation.returnWebLoginVerify(request, username, password)


# 验证提取码
@router.post('/api/file/web/verify_code')
async def verifyCode(request:Request, verify_code:str=Form(...)):

    print(verify_code)
    return await webOperation.returnVerifyCode(request, verify_code)