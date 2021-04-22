'''
@Description:
@Author: michael
@Date: 2020-04-08 10:54:10
LastEditTime: 2020-04-09 20:00:00
LastEditors: michael
'''
# coding=utf-8

# 加载第公共文件
from views.Base import *

# 加载自己创建的包
from views.web_api.templates.TempManage import tempManage


# 第三方 OSS 服务操作类
class WebOperation:

    # 验证登陆的链接类型 - 同时返回相应登陆类型的得到的内容
    async def returnWebCloud(self, request, share_id):

        # 判断是否为数字字符
        if share_id.isnumeric() is False or len(share_id) > 9 :
            return {'request':request, 'code':201, 'message':'非法参数'}

        # 获取链接分享日志
        dbo.resetInitConfig('test', 'os_share_log')
        condition = {'id':share_id}
        field = {'_id':0}
        find_result = await dbo.findOne(condition, field)
        if find_result is None:
            message = {'request':request, 'code':202, 'message':'无效的链接'}
            return await tempManage.errorPage(message)

        # logs = await self.shareLogs(share_id)

        # 查找传入链接的日志记录
        # action = False
        # for value in logs:
        #     if value['id'] == share_id:
        #         log_result = value
        #         action = True
        #         break;

        # 判断是否有记录
        # if action is False:
        #     message = {'request':request, 'code':202, 'message':'无效的链接'}
        #     return await tempManage.errorPage(message)

        print(find_result)
        # return find_result
        # 判断链接指定访问类型
        if find_result['access_type'] == '1':
            '''账号密码登陆'''
            # 查看用户是否登陆

            # 查看登陆用户是否是指定用户，比如指定用户A, 或者是否是分享者自己登陆

            # 提取分享日志中的目录或文件

            # 记录操作到访问日志

            return await tempManage.webLogin(request)

        elif log_result['access_type'] == '2':
            '''提取码'''
            # 查看是否输入提取码

            # 提取分享日志中的目录或文件

            # 记录操作到访问日志
            
            return await tempManage.verifyCode(request)

        else:
            # 提取分享日志中的目录或文件

            # 记录操作到访问日志
            return 333

        return await self.fileDownload(request)


    # 用户登陆验证
    async def returnWebLoginVerify(self, request, username, password):

        if username == '1' and password == '1':
            return await tempManage.returnWebCloud(request)
        else:
            message = { 'request':request, 'code':201, 'message':'登陆失败' }

        return await tempManage.errorPage(message)


    # 提取码验证
    async def returnVerifyCode(self, request, verify_code):

        return '这里是提取码页面验证方法 - 待开发'


    # 拟定一批权限的 share_url 
    async def shareLogs(self, share_id):

        '''
        以下参数为数据库定义字段，并非需要传入的参数
        :param id string 模拟自增ID
        :param share_url string 实际分享的链接 url
        :param access_uid string 允许链接查看的用户，默认所有人可以查看 用 * 来表示
        :param share_uid string 分享链接的用户
        :param access_type string 访问类型：
                                        1 需要输入 - 用户名和密码 - 才可以查看和下载文件
                                        2 需要输入 - 提取码 - 才可以查看和下载文件
                                        3 普通链接 - 有可能用不上这个
        :param access_address string 给予权限访问的目录或文件

        :param access_num integer 允许访问的次数 默认-无限
        :param actual_access_num integer 实际访问的次数 默认0

        :param download_num integer 允许下载的次数 默认-无限
        :param actual_download_num integer 实际下载的次数 默认0

        :param create_time integer 日志的创建时间 默认0
        :param expiration_time string 链接过期时间: 默认 0(永久有效)
        访问时间和下载时间后面再增加
        '''

        logs = [
            {
                'id': '1',
                'share_url':'http://localhost:8000/api/file/web/web_cloud?id=1',
                'access_uid': '*',
                'share_uid': '999',
                'access_type': '1',
                'access_address': '11&asdfasdfasdfasdfasdfasdfasdf',
                'access_num': '-',
                'actual_access_num': 0,
                'download_num': '-',
                'actual_download_num': 0,
                'create_time': 0,
                'expiration_time': '111'
            },
            {
                'id': '2',
                'share_url':'http://localhost:8000/api/file/web/web_cloud?id=2',
                'access_uid': '11',
                'share_uid': '999',
                'access_type': '2',
                'access_address': '22&asdfasdfasdfasdfasdfasdfasdf',
                'access_num': '-',
                'actual_access_num': 0,
                'download_num': '-',
                'actual_download_num': 0,
                'create_time': 0,
                'create_time': 0,
                'expiration_time': '222'
            },
            {
                'id': '3',
                'share_url':'http://localhost:8000/api/file/web/web_cloud?id=2',
                'access_uid': '11',
                'share_uid': '999',
                'access_type': '3',
                'access_address': '22&asdfasdfasdfasdfasdfasdfasdf',
                'access_num': '-',
                'actual_access_num': 0,
                'download_num': '-',
                'actual_download_num': 0,
                'create_time': 0,
                'create_time': 0,
                'expiration_time': '222'
            }
        ]

        return logs


    # 返回登陆模板
    async def returnWebLogin(self, request):
        return tempManage.webLogin(request)


    # 返回文件提取模板
    async def returnFileDownload(self, request):
        return tempManage.fileDownload(request)









webOperation = WebOperation()
