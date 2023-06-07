import requests
from login import HEADERS


params = lambda cid:{
    'cid': f'{cid}',
}
response = lambda cid, cookies: requests.get(f'https://welearn.sflep.com/student/course_info.aspx?cid=2384', params= cid, headers=HEADERS, cookies=cookies).content.decode().split('uid":')[1].split(',')[0]
UID = lambda cid, cookies:response(cid=cid, cookies=cookies)
