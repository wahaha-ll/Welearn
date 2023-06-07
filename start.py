from multiprocessing import Process as Speed
# from threading import Thread as Speed
from submit import submit

class RUN(Speed):

    def __init__(self, cid, uid, scoid, cookies):
        Speed.__init__(self)
        self.cid = cid
        self.uid = uid
        self.scoid = scoid
        self.cookies = cookies

    def run(self) -> None:
        # for i in range(len(self.scoid)):
        while(True):
            try:
                submit(cid=self.cid,uid=self.uid,scoid=self.scoid, cookies=self.cookies)
            except:
                print("出错啦！")