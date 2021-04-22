'''
@Description:
@Author: michael
@Date: 2020-04-09 10:54:10
LastEditTime: 2020-04-09 20:00:00
LastEditors: michael
'''
# coding=utf-8

# 加载 jinja2 模板包
from starlette.templating import Jinja2Templates

# 挂载模版目录
view = Jinja2Templates(directory='templates')

# 第三方 OSS 服务操作类
class TempManage:


    # 用户登陆页面模板
    async def webLogin(self, request):

        # 返回需要渲染的模板和值
        return view.TemplateResponse(
            '/web_api/login.html',
            {
                'request':request  # 一定要返回request
            }
        )


    # 文件提取页面模板
    async def fileDownload(self, request):

        # 返回需要渲染的模板和值
        return view.TemplateResponse(
            '/web_api/index.html',
            {
                'request':request,  # 一定要返回request
                'args':'文件提取页面'  # 额外的参数可有可无
            }
        )

    
    # 文件提取验证码页面模板
    async def verifyCode(self, request):

        # 返回需要渲染的模板和值
        return view.TemplateResponse(
            '/web_api/verify_code.html',
            {
                'request':request  # 一定要返回request
            }
        )


    # 错误提示页面模板
    async def errorPage(self, message):

        # 返回需要渲染的模板和值
        return view.TemplateResponse(
            '/web_api/error.html',
            {
                'request': message['request'],  # 一定要返回request
                'code': message['code'],  # 额外的参数可有可无
                'message': message['message']
            }
        )










tempManage = TempManage()
