# @Time     : 2020/5/21 16:15
# @Author   : Chao Zheng
# @Email    : chaoszh@foxmail.com

import json
from flask import make_response

def SuccessResponse(code=200, data=None):
    headers = {
        'content-type':'application/json'
    }
    data={
        "code": code,
        "data": data
    }
    response=make_response(data, code)
    response.headers=headers
    return response

def FailureResponse(code=400, data=None):
    headers = {
        'content-type':'application/json'
    }
    data={
        "code": code,
        "error_msg": data
    }
    response=make_response(data, code)
    response.headers=headers
    return response