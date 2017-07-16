import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import pandas

#import re
listurl = 'http://roll.news.sina.com.cn/news/shxw/zqsk/index_{}.shtml'
comurl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=sh&newsid=comos-{}&group=&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=20'
newstotal = []


def getNews(newsurl):
        result = {}
        res = requests.get(newsurl)
        res.encoding = 'utf-8'
        soup = BeautifulSoup(res.text,'html.parser')
        result['title'] = soup.select('#artibodyTitle')[0].text
        if soup.select('.time-source span a'):
                result['medianame'] = soup.select('.time-source span a')[0].text
        else:
            result['medianame'] = '未知'
        timesource = soup.select('.time-source')[0].contents[0].strip()
        result['dt'] = datetime.strptime(timesource,'%Y年%m月%d日%H:%M')
        result['content'] = ' '.join([p.text.strip() for p in soup.select('#artibody p')[:-1]])
        result['editor'] = soup.select('.article-editor')[0].text.strip('责任编辑：')
        result['comment'] = getCommentCount(newsurl)
        #print(result)
        return result


def getCommentCount(newsurl):
        newsid = newsurl.split('/')[-1].rstrip('.shtml').lstrip('doc-i')
        comment = requests.get(comurl.format(newsid))
        jd = json.loads(comment.text.strip('var data='))
        #print(dir(jd['result']))
        if 'count' in jd['result']:
            return jd['result']['count']['total']
        else:
            return 0


def NewsList(url):
        newsDetails=[]
        res = requests.get(url)
        res.encoding = 'gb2312'
        soup1 = BeautifulSoup(res.text, 'html.parser')
        contentlist = soup1.select('.list_009 a')
        for link in contentlist:
                newsDetails.append(getNews(link['href']))
        return newsDetails

for i in range(1,3):
        newsurl = listurl.format(i)
        newsCollected = NewsList(newsurl)
        newstotal.append(newsCollected)


df = pandas.DataFrame(newstotal)
print(df.head())