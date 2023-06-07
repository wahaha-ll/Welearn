import requests, time
from login import HEADERS, SESSION
from threading import Thread



params =lambda uid: {
    'uid': f'{uid}',
}

data = lambda uid, cid, scoid: {
    'action': 'keepsco_with_getticket_with_updatecmitime',
    'uid': f'{uid}',
    'cid': f'{cid}',
    'scoid': f'{scoid}',
    'session_time': '1000',
    'total_time': '1000',
    'timelimitsec': '1800',
    'endcaltime': 'false',
    'nocache': '',
}

def sub_time (uid, cid, scoid, cookies):
    time.sleep(10)
    print(SESSION.post('https://welearn.sflep.com/Ajax/SCO.aspx', params=params(uid=uid), cookies=cookies, headers=HEADERS, data=data(uid=uid, cid=cid, scoid=scoid)).text)


    # threads = [submit_thread(uid, cid, scoid, COOKIES) for i in range(10*count)]
    # time.sleep(1)
    # [i.start() for i in threads]

class submit_thread(Thread):
     
    def __init__(self, uid, cid, scoid, cookies):
        Thread.__init__(self)
        self.uid = uid
        self.cid = cid
        self.scoid = scoid
        self.cookies = cookies

    def run(self):
        sub_time(uid=self.uid, scoid=self.cid, cid=self.cid, count=1)
        print(requests.post('https://welearn.sflep.com/Ajax/SCO.aspx', params=params(uid=self.uid), cookies=self.cookies, headers=HEADERS, data=data(uid=self.uid, cid=self.cid, scoid=self.scoid)).text)



    
    

        

