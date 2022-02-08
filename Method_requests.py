import requests
import yaml
import json
class reBasePage(object):
    requestsbody='requestsbody'
    url='url'
    data='data'
    headers='headers'
    def get_cookies(self):
        a = requests.post(self.get_url('65url'), self.get_data('login'), headers=self.get_headers('headers_form'))
        return a.cookies

    def responsebody(self,Respomsebody):
        with open(self.requestsbody, 'w', encoding='utf-8') as d:
            yaml.dump(Respomsebody, d)

    def get_requestbody(self):
        with open(self.requestsbody, 'r', encoding='utf-8') as d:
            data = yaml.load(d, Loader=yaml.FullLoader)
        return data

    def get_url(self,url):
        with open(self.url, 'r', encoding='utf-8') as d:
            data = yaml.load(d, Loader=yaml.FullLoader)
        return data[url]

    def get_data(self,date):
        with open(self.data, 'r', encoding='utf-8') as d:
            data = yaml.load(d, Loader=yaml.FullLoader)
        return data[date]

    def get_headers(self,herders):
        with open(self.headers, 'r', encoding='utf-8') as d:
            data = yaml.load(d, Loader=yaml.FullLoader)
        return data[herders]

    def get_request(self,url,headers):
        ResponseBody=requests.get(self.get_url(url),headers=self.get_headers(headers),cookies=self.get_cookies())
        self.responsebody(ResponseBody.json())

    def post_request(self,url,body,headers):
        with open(self.data, 'r', encoding='utf-8') as d:
            data = yaml.load(d, Loader=yaml.FullLoader)
        for i in data[body]:
            if 'json' in headers:
                ResponseBody=requests.post(self.get_url(url),json.dumps(data[body][i]),headers=self.get_headers(headers),cookies=self.get_cookies())
                self.responsebody(ResponseBody.json())
            else:
                ResponseBody = requests.post(self.get_url(url),(data[body][i]),
                                             headers=self.get_headers(headers), cookies=self.get_cookies())
                self.responsebody(ResponseBody.json())


