import hashlib,base64,random,string
from application import app
import requests,json

class MemberService():
    @staticmethod
    def geneAuthCode(member_info):
        m = hashlib.md5()
        str = "%s-%s-%s" % (member_info.id,member_info.salt,member_info.status)
        m.update(str.encode('utf-8'))
        return m.hexdigest()

    @staticmethod
    def geneSalt( length = 16):
        keylist = [random.choice((string.ascii_letters + string.digits)) for i in range( length )]
        print('密码:',''.join(keylist))

        return (''.join(keylist))



    @staticmethod
    def getWechatOpenid(code):
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code'.format(
            app.config['MINA_APP']['appid'], app.config['MINA_APP']['appkey'], code)
        r = requests.get(url)
        res = json.loads(r.text)
        openid = None
        if 'openid' in res:
            openid = res['openid']
        return openid