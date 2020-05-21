# @Time     : 2020/5/21 16:15
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

import json
from werkzeug.wrappers import Response

def SuccessResponse(code=200, data=None):
    response=Response()
    response.data=json.dumps(data)
    response.status_code=code
    response.headers=[('Content-Type','application/json')]
    return response

def FailureResponse(code=400, data=None):
    response=Response()
    response.data=data
    response.status_code=code
    response.headers=[('Content-Type','text/plain')]
    return response