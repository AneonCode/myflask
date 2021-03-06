
# coding: utf-8

# In[ ]:

# -*- coding: <utf-8> -*-
import requests
import json
from bs4 import BeautifulSoup
import sys
import webbrowser
import sqlite3
import os
import time
import urllib
from urllib.request import urlopen

def spyder_pic(index,i,title):
    search = urllib.parse.quote(title)
    url = 'http://image.baidu.com/search/avatarjson?tn=resultjsonavatarnew&ie=utf-8&word=' + search + '&cg=girl&pn=1&rn=60&itg=0&z=0&fr=&width=&height=&lm=-1&ic=0&s=0&st=-1&gsm=1e0000001e'
    req = urllib.request.Request(url=url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'})
    page = urllib.request.urlopen(req)
    rsp = page.read().decode('unicode_escape')
    rsp_data = json.loads(rsp, strict=False)
    for image_info in rsp_data['imgs']:
        #print(image_info['objURL'])
        if(image_info['objURL'][9:17]=='hiphotos' or image_info['objURL'][7:11]=='icon' or image_info['objURL'][11:17]=='renwen' or image_info['objURL'][9:13]=='dimg'):
            continue
        r = urllib.request.Request(url=image_info['objURL'],headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'})
        try:
            resp=urlopen(r)
            code=resp.getcode()
            if(code==403 or code==503 or code==502 or code == 404):
                continue
            else:
                add_img(index,i,image_info['objURL'])
                break
        except Exception:
            continue
    page.close()

while True:
    ### index:
    #0：科技 1：运动 2：社科 3：娱乐 4：食物 5：摄影 6：生活方式 7：学科 8：文学
    # 科技 运动 娱乐 社科 摄影 美食 文学
    
    
    # 要使用的一些函数
    
    def insert_to_db(index,i,title,link,link_img="NULL",abstract="NULL"):
        if index==0:
            c.execute("REPLACE INTO SCIENCE VALUES( (?), (?), (?), (?), (?))",(i,title,link,link_img,abstract))
        if index==1:
            c.execute("REPLACE INTO SPORTS VALUES( (?), (?), (?), (?), (?))",(i,title,link,link_img,abstract))
        if index==2:
            c.execute("REPLACE INTO ENTERTAINMENT VALUES( (?), (?), (?), (?), (?))",(i,title,link,link_img,abstract))
        if index==3:
            c.execute("REPLACE INTO SOCIAL VALUES( (?), (?), (?), (?), (?))",(i,title,link,link_img,abstract))
        if index==4:
            c.execute("REPLACE INTO SHOOT VALUES( (?), (?), (?), (?), (?))",(i,title,link,link_img,abstract))
        if index==5:
            c.execute("REPLACE INTO FOOD VALUES( (?), (?), (?), (?), (?))",(i,title,link,link_img,abstract))
        if index==6:
            c.execute("REPLACE INTO LITERATURE VALUES( (?), (?), (?), (?), (?))",(i,title,link,link_img,abstract))
    
    
    def add_img(index,i,link_img):
        if index==0:
            c.execute("UPDATE SCIENCE set LINK_IMG = (?) where ID = (?)",(link_img,i))
        if index==1:
            c.execute("UPDATE SPORTS set LINK_IMG = (?) where ID = (?)",(link_img,i))
        if index==2:
            c.execute("UPDATE ENTERTAINMENT set LINK_IMG = (?) where ID = (?)",(link_img,i))
        if index==3:
            c.execute("UPDATE SOCIAL set LINK_IMG = (?) where ID = (?)",(link_img,i))
        if index==4:
            c.execute("UPDATE SHOOT set LINK_IMG = (?) where ID = (?)",(link_img,i))
        if index==5:
            c.execute("UPDATE FOOD set LINK_IMG = (?) where ID = (?)",(link_img,i))
        if index==6:
            c.execute("UPDATE LITERATURE set LINK_IMG = (?) where ID = (?)",(link_img,i))


    def add_abstract(index,i,abstract):
        if index==0:
            c.execute("UPDATE SCIENCE set ABSTRACT = (?) where ID = (?)",(abstract,i))
        if index==1:
            c.execute("UPDATE SPORTS set ABSTRACT = (?) where ID = (?)",(abstract,i))
        if index==2:
            c.execute("UPDATE ENTERTAINMENT set ABSTRACT = (?) where ID = (?)",(abstract,i))
        if index==3:
            c.execute("UPDATE SOCIAL set ABSTRACT = (?) where ID = (?)",(abstract,i))
        if index==4:
            c.execute("UPDATE SHOOT set ABSTRACT = (?) where ID = (?)",(abstract,i))
        if index==5:
            c.execute("UPDATE FOOD set ABSTRACT = (?) where ID = (?)",(abstract,i))
        if index==6:
            c.execute("UPDATE LITERATURE set ABSTRACT = (?) where ID = (?)",(abstract,i))
    
    # 连接数据库
    if os.path.exists("db/article.db"):
        os.unlink("db/article.db")
    if os.path.exists(r"static/images/NG\d*.jpg"):
        os.remove(r"static/images/NG\d*.jpg")
    conn = sqlite3.connect('db/article.db')
    print("Opened database successfully")
    c = conn.cursor()
    
    
    
    # 创建表
    
    c.execute('''CREATE TABLE SCIENCE
            (ID INT PRIMARY KEY      NOT NULL,
            TITLE            TEXT     NOT NULL,
            LINK             TEXT      NOT NULL,
            LINK_IMG         TEXT,
            ABSTRACT         TEXT);''')
    print('Table_Science created successfully')#科技
    
    c.execute('''CREATE TABLE SPORTS
            (ID INT PRIMARY KEY      NOT NULL,
            TITLE            TEXT     NOT NULL,
            LINK             TEXT      NOT NULL,
            LINK_IMG         TEXT,
            ABSTRACT         TEXT);''')
    print('Table_Sports created successfully')#运动
    
    c.execute('''CREATE TABLE SOCIAL
            (ID INT PRIMARY KEY      NOT NULL,
            TITLE            TEXT     NOT NULL,
            LINK             TEXT      NOT NULL,
            LINK_IMG         TEXT,
            ABSTRACT         TEXT);''')
    print('Table_Social created successfully')#社科
    
    c.execute('''CREATE TABLE ENTERTAINMENT
            (ID INT PRIMARY KEY      NOT NULL,
            TITLE            TEXT     NOT NULL,
            LINK             TEXT      NOT NULL,
            LINK_IMG         TEXT,
            ABSTRACT         TEXT);''')
    print('Table_Entertainment created successfully')#娱乐
    
    c.execute('''CREATE TABLE FOOD
            (ID INT PRIMARY KEY      NOT NULL,
            TITLE            TEXT     NOT NULL,
            LINK             TEXT      NOT NULL,
            LINK_IMG         TEXT,
            ABSTRACT         TEXT);''')
    print('Table_Food created successfully')#食物
    
    c.execute('''CREATE TABLE SHOOT
            (ID INT PRIMARY KEY      NOT NULL,
            TITLE            TEXT     NOT NULL,
            LINK             TEXT      NOT NULL,
            LINK_IMG         TEXT,
            ABSTRACT         TEXT);''')
    print('Table_Shoot created successfully')#摄影
    
    c.execute('''CREATE TABLE LITERATURE
            (ID INT PRIMARY KEY      NOT NULL,
            TITLE            TEXT     NOT NULL,
            LINK             TEXT      NOT NULL,
            LINK_IMG         TEXT,
            ABSTRACT         TEXT);''')
    print('Table_Literature created successfully')#文学
    
    conn.commit()
    
    for index in range(7):
        i=0
        # 知乎爬取
        index_zh = [['19556664'],#科技
                ['19552706'],#运动
                ['19550429','19569409'],#电影 二次元
                ['19551585','19550921','19569848', '19551557'],#社科
                ['19569883'],#摄影
                ['19562435'],#食品安全
                ['19550434','19551016','19585156']#艺术 字体
                ]
        
        
        for h in index_zh[index]:
            url = 'https://www.zhihu.com/topic/'+h+'/hot'
            
            wbdata = requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}, stream=True).text
            
            soup = BeautifulSoup(wbdata,'lxml')
            #soup
            
            news_titles = soup.select('div .feed-item.feed-item-hook.folding > div > div > h2 > a')
            news_abs = soup.select('div .zh-summary.summary.clearfix ')
            #Zhihu = {}
            j=i
            for n in news_titles:
                i = i+1
                title = n.get_text(strip=True)
                
                link = "http://www.zhihu.com"+n.get("href")
                insert_to_db(index,i,title,link)
                spyder_pic(index,i,title)
                #print("爬取一张图")
                #data = {
                #    '标题':title,
                #    '链接':link,
                #}
                #Zhihu[i] = data
            i=j
            for n in news_abs:
                i = i+1
                abstract = n.get_text(strip=True)
                add_abstract(index,i,abstract)
                #if(n.select('img')!=[]):
                #   temp = n.select('img')
                #  link_img=temp[0].get('data-original')
                   # add_img(index,i,link_img)
                #test
        #Zhihu
        #Zhihu[1]['abstract']
        #webbrowser.open('www.zhihu.com'+Zhihu[1]['链接'], new=0, autoraise=True)
    
        # 今日头条爬取
        
        index_tt = [['tech'],#科技
                    ['sports'],#运动
                    ['entertainment','funny','game'],#娱乐 搞笑 游戏
                    ['world','military','society'],#国际 军事 社会
                    [],#摄影
                    ['food'],#美食
                    ['regimen','history']#文学 历史   
                   ]
        for h in index_tt[index]:
            url = 'https://www.toutiao.com/api/pc/feed/?category=news_'+h+'&utm_source=toutiao&widen=1&max_behot_time=0&max_behot_time_tmp=0&tadrequire=true&as=A195094EFDC8F33&cp=59ED588F63F3DE1'
            wbdata = requests.get(url, stream=True).text
            
            data = json.loads(wbdata, strict=False)
            news = data['data']
            
            for n in news:
                if 'label' in n:
                    if n['label'] != '广告':
                        i=i+1
                        title = n['title']
                        if 'abstract' in n:
                            abstract = n['abstract']
                        else:
                            abstract = 'NULL'
                        link = 'http://www.toutiao.com'+n['source_url']
                        insert_to_db(index,i,title,link,"NULL",abstract)
                        if 'image_url' in n:
                            link_img = n['image_url']
                            add_img(index,i,link_img)
                        else:
                            spyder_pic(index,i,title)
                        
        
        # 果壳网爬取
        
        index_gk = [['科学','互联网','电子','计算机','电子产品','网络'],
                    ['运动'],
                    [],
                    ['社会科学','大学','生活','健康','睡眠'],
                    ['摄影'],
                    ['食物'],
                    ['人文','历史']
                    ]
        for h in index_gk[index]:
            url = 'http://www.guokr.com/ask/tag/'+h+'/'
            
            wbdata = requests.get(url, stream=True).content
            
            soup = BeautifulSoup(wbdata,'lxml')
            
            news_titles = soup.select('div .ask-list-detials > h2 > a')
            news_abs = soup.select('div .ask-list-detials > div > p[class="ask-list-summary"] ')
            
        #Guokr = {}
        j=i
        for n in news_titles:
            i = i+1
            title = n.get_text()
            link = n.get("href")
            
            insert_to_db(index,i,title,link)
            spyder_pic(index,i,title)
            #data = {
            #    '标题':title,
            #    '链接':link,
            #}
            #Guokr[i] = data
        i=j
        for n in news_abs:
            i = i+1
            abstract = n.get_text(strip=True)
            add_abstract(index,i,abstract)
            #Guokr[i]['摘要'] = abstract
    
        # 国家地理中文网爬取
        index_ng = [['science/science'],#科学
                    ['travel/adventure/'],#户外探险
                    ['animals/photo/'],#动物影像
                    ['animals/protection/','photography/picture_story/'],#动物保护 图片故事
                    ['photography/photo_tips/','travel/destinations/'],#摄影技巧 旅行目的地
                    [],
                    ['culture_list']#人文
                   ]
        for h in index_ng[index]:
            url = 'http://www.nationalgeographic.com.cn/'+h+'/'
            
            wbdata = requests.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}, stream=True).content
            
            soup = BeautifulSoup(wbdata,'lxml')
            
            news_titles = soup.select("div .showImg-list > dl > dt > a")
            news_abs = soup.select("div .showImg-list > dl > dd > a")
            news_imgs = soup.select("div .showImg-list > dl > a > img")
            
            j=i
            for n in news_titles:
                i = i+1
                title = n.get('title')
                
                link = 'http://www.nationalgeographic.com.cn'+n.get('href')
                insert_to_db(index,i,title,link)
                
            i=j
            for n in news_abs:
                i = i+1
                abstract = n.get_text(strip=True)
                add_abstract(index,i,abstract)
            i=j
            for n in news_imgs:
                try:
                    i = i+1
                    link_img = n.get('src')
                    urllib.request.urlretrieve(link_img,'static/images/NG%s.jpg' %i)
                    add_img(index,i,'static/images/NG%s.jpg'%i)
                except BaseException:
                    spyder_pic(index,i,title)
                
        
            # 简书爬取
            
        index_js = [['V2CqjW','V2CqjW'],#科学 IT互联网
                    ['snqjhw'],#运动
                    ['0856231c8e98','00bd0686bc41','1hjajt'],#游戏 欧美剧 电影 
                    ['GQ5FAs','fcd7a62be697','71169ced18ac'],#谈谈情说说爱 世间事 大学生活 
                    ['7b2be866f564'],#摄影
                    ['daf38cbac488 '],#食物
                    ['dqfRwQ','f6b4ca4bb891','8c92f845cd4d','e7d2d4045b36']#文学            
        ]
        for h in index_js[index]:
            url = 'http://www.jianshu.com/c/'+ h
            
            wbdata = requests.get(url, stream=True).content
        
        soup = BeautifulSoup(wbdata,'lxml')
        
        news_titles = soup.select('div .content > a')
        news_abs = soup.select('div .content > p')
        img_url = soup.select('div #list-container > ul > li')
        
        j=i
        for n in news_titles:
            i = i+1
            title = n.get_text()
            link = 'http://www.jianshu.com'+n.get('href')
            insert_to_db(index,i,title,link)
        i=j
        for n in news_abs:
            i = i+1
            abstract = n.get_text(strip=True)
            add_abstract(index,i,abstract)
        i=j
        for n in img_url:
            i = i+1
            if n.get('class')[0] == 'have-img':
                m = n.select('a > img')
                link_img = m[0].get('src')
                add_img(index,i,link_img)
            else:
                spyder_pic(index,i,title)
    
        id = ['科技', '运动', '娱乐', '社科', '摄影', '美食', '文学']
        print(id[index]+" Operation done successfully");


    conn.commit()
    conn.close()
    print('Sleeping...')
    time.sleep(43200)


# In[ ]:



