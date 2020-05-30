def authenrize():
    pass

def register_auth(app):
    app.before_request_funcs.setdefault(None, []).append(authenrize)
    return 
