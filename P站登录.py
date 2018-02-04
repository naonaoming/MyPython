import urllib
import urllib.request
from bs4 import BeautifulSoup

#url = 'https://www.zhihu.com/#signin'
url = 'https://accounts.pixiv.net/api/login?lang=zh'
#url = 'https://accounts.pixiv.net/login?lang=zh'
referer='https://accounts.pixiv.net/login?lang=zh&source=pc&view_type=page&ref=wwwtop_accounts_index'
user_agent = 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
headers = {'User-Agent' : user_agent,'X-Requested-With': 'XMLHttpRequest','Referer':referer,'Host': 'accounts.pixiv.net','Origin': 'https://accounts.pixiv.net'}
values = {}
values['post_key'] = '292caeedfe353a8af3046af64a5ae024'
values['password'] = 'a11111'
values['pixiv_id'] = '593173700@qq.com'
values['source'] = 'pc'
values['ref'] = 'wwwtop_accounts_index'
values['return_to'] = 'https://www.pixiv.net/'
values['g_recaptcha_response'] = ''
values['captcha'] = ''
data = urllib.parse.urlencode(values).encode(encoding='UTF-8')
#print(values)

try:
    request = urllib.request.Request(url,data,headers)
    #request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    page = response.read().decode('UTF-8')
    print(page)
    soup = BeautifulSoup(page,"html.parser")
    #print(soup.find(name="_xsrf"))
    
except urllib.error.URLError as e:
    print(e.code,':',e.reason)
