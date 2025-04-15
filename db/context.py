
logged_res = []

logged_requests = []

def add_user_response(res):
    logged_requests.insert(0, res)
    return logged_res

def add_gem_response(res):
    logged_res.insert(0, res)
    return logged_res