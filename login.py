import requests
from fake_useragent import UserAgent
import time
import json
from book import BOOK

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}

SESSION = requests.session()
SESSION.headers

def LOGIN (account, pwd, cookies): 
    data = lambda account,pwd: {
    'rturl': '/connect/authorize/callback?client_id=welearn_web&redirect_uri=https%3A%2F%2Fwelearn.sflep.com%2Fsignin-sflep&response_type=code&scope=openid%20profile%20email%20phone%20address&code_challenge=1Q93Ff_Qm4XKrjSsRn58i7z-2tSVf3R2PUAE12y0xw8&code_challenge_method=S256&state=OpenIdConnect.AuthenticationProperties%3DxwKIxq8DUjVBHnTH4A6oLijs_g-jOFvj1zv68XCrOdgbLfTl7jX4fXgMA-dItBZRB37aKlqFUvhMJrS1OIbFm7xAThHIkJIcna1Pzuj4xXGFevSfhnBOq65FcekrridfINyE9VsVG0H81jE7-vq2B-3UHxTHouwOIkTFfJUXWOEVLSzElfipkzTsKCdo_M7KED05kyOTdE2zBsDxOBa7LyVFUE3jK96pfzj_B_3euQPz0suj671ZNLk0uSH2e3zmg9c2FgZfrnsyfHiRx5OLQ1ze3pZTGOF6cCVr0uctAclqMiZvlnPAJg6GNk55tMxVtoi9H7IHLdfTUeT-Jx2FBg&x-client-SKU=ID_NET472&x-client-ver=6.23.1.0',
    'account': f'{account}',
    'pwd': f'{pwd}',
    }
    login = SESSION.post('https://sso.sflep.com/idsvr/account/login', cookies=cookies, headers=HEADERS, data=data(account, pwd))   
    get_CALLBACK(login=login, cookies=cookies)

    # get_ASPNET()
    # COOKIES.update(SESSION.cookies.get_dict())
    # get_AREA()
    # COOKIES.update(SESSION.cookies.get_dict()) 

def get_COOK():
    return requests.utils.dict_from_cookiejar(requests.get('https://welearn.sflep.com/', headers=HEADERS).cookies)

def get_CALLBACK(login, cookies): 
    return SESSION.get('https://sso.sflep.com/idsvr'+json.loads(login.content.decode())['data'],cookies=cookies, headers=HEADERS)
    

def get_ASPNET(cookies):
    params = {
    'code': 'AFD5D7730E22E1CAECBF7BFE909694C8BF19293DF959CDC62F5AF6D083ADD314',
    'scope': 'openid profile email phone address',
    'state': 'OpenIdConnect.AuthenticationProperties=zAXAJfonJNULb0lVmSiDI-xlc8Ac66zEYq_4o49ZY7qmObP0e23oq24UmIHQFmFCjusltWRhVpN0MSWKBPe4SBoPC-W0GpXn-Pj5Iy8tM_TPGVtKZeb75OjzVu1y-f2QjILLtbMVskRC1LhmhgLh1B_YBU5R9VjiIuScw-MmQRq-Fm7wyVLO5Hs0bZoJ2BoX7Jovdb15f53ccIjxac1q2gdWQ6Y3giSspgOq9VgC2D4R4pgPR8TlpURCn0aeWJNP2-M3_9kFYYWxmKkliNVZGXs51U5E4NZVf4H2V7taj8bXGABF6D61breYZ5ZUqmurU3Pf_GL2QOyXKK8R-5SJlw',
    'session_state': '7WVVlWxaeauKNCEMnHSqj5NWxk77E_8MgtKmbw4t72E.6620A7E130841C3E222C3CE25B5E949C',
    }
    SESSION.get('https://welearn.sflep.com/signin-sflep', params=params, cookies=cookies, headers=HEADERS)

def get_AREA(cookies):
    SESSION.get('https://welearn.sflep.com/user/loginredirect.aspx', cookies=cookies, headers=HEADERS)



