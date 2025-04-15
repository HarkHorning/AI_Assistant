
logged_requests = []

user_style_left = """<li class="chat_div user_question"><p class="chat" id="response">"""
user_style_right = """</p><div class="avatar user_av col">U</div></li>"""

gemini_style_left = """<div class="chat_div gemini_response"><div class="avatar gem_av col">G</div><p class="chat " id="">"""
gemini_style_right = """</p></div>"""

def add_user_response(res):
    logged_requests.append(user_style_left + res + user_style_right)
    return logged_requests

def add_gem_response(res):
    logged_requests.append(gemini_style_left + res + gemini_style_right)
    return logged_requests
