import requests
import json
from login import HEADERS, SESSION
from subemit_time import sub_time
from time import sleep

PARAMS = lambda uid: {
    'uid': f'{uid}',
}

data = lambda cid,scoid,uid : {
    'action': 'setscoinfo',
    'cid': f'{cid}',
    'scoid': f'{scoid}',
    'uid': f'{uid}',
    'data': '{"cmi":\
                    {"completion_status":"completed","interactions":"",\
                            "launch_data":"",\
                            "progress_measure":"1",\
                            "score":{"scaled":"100","raw":"100"},\
                            "session_time":1800,\
                            "success_status":"successed",\
                            "total_time":1800,"mode":"normal"},\
                            "adl":{"data":[]},\
                            "cci":{"data":[],\
                                    "service":{\
                                                "dictionary":{"headword":"","short_cuts":""},\
                                                "new_words":[],\
                                                "notes":[],\
                                                "writing_marking":[],\
                                                "record":{"files":[]},\
                                                "play":{"offline_media_id":"9999"}\
                                                },\
                                    "retry_count":"1",\
                                    "submit":{\
                                            "info":""\
                                            },\
                                    "other":{"info":""}}}',
    'isend': 'false',
    'nocache': '',
}

def submit(cid, uid, scoid,cookies):
    sleep(1)
    SESSION.post(f'https://welearn.sflep.com/Ajax/SCO.aspx?uid={uid}', data = {'action': 'isPausing', 'uid': f'{uid}', 'nocache': ''}).content.decode()
    SESSION.post(f'https://welearn.sflep.com/Ajax/SCO.aspx?uid={uid}', data = {'action': 'checkNoCaptcha', 'uid': f'{uid}', 'nocache': ''}).content.decode()
    url = 'http:'+json.loads(SESSION.post(f'https://welearn.sflep.com/Ajax/SCO.aspx?uid={uid}', data = {'action': 'scoAddr', 'cid': f'{cid}', 'scoid': f'{scoid}', 'nocache': ''}).content.decode())['addr'].split('|')[0]
    SESSION.get(url=url, cookies=cookies, headers=HEADERS)
    SESSION.post(f'https://welearn.sflep.com/Ajax/SCO.aspx?uid={uid}', data = {'action': 'startsco160928', 'cid':f'{cid}', 'scoid': f'{scoid}', 'uid': f'{uid}', 'progress' : '1', 'crate' : '100', 'status' : 'passed', 'cstatus' : 'completed', 'trycount' : '0', 'endcaltime' : 'false', 'nocache': ''}).content.decode()
    SESSION.get(f'https://welearn.sflep.com/student/StudyCourse.aspx?cid={cid}&classid={uid}&sco={scoid}', cookies=cookies, headers=HEADERS)
    sleep(1)
    SESSION.post(f'https://welearn.sflep.com/Ajax/SCO.aspx?uid={uid}', data = {'action': 'updatecmitime', 'uid': f'{uid}', 'cid':f'{cid}', 'scoid': f'{scoid}', 'total_time': '3000', 'session_time' : '100', 'nocache': ''}).content.decode()
    sleep(2)
    SESSION.post(f'https://welearn.sflep.com/Ajax/SCO.aspx?uid={uid}', data = {'action': 'savescoinfo160928', 'cid':f'{cid}', 'scoid': f'{scoid}', 'uid': f'{uid}', 'progress' : '1', 'crate' : '100', 'status' : 'passed', 'cstatus' : 'completed', 'trycount' : '0', 'endcaltime' : 'false', 'nocache': ''}).content.decode()
    SESSION.post('https://welearn.sflep.com/Ajax/SCO.aspx', params=PARAMS(uid), cookies=cookies, headers=HEADERS, data=data(cid=cid,scoid=scoid,uid=uid))
