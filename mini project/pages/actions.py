
from . models import Slider

class Actions:

    def stocker(self):
        from pandas_datareader import data as pdr
        import fix_yahoo_finance as yf
        import time
        import json
        yf.pdr_override()
        data = 0
        google = 0
        

        global list2
        list2 = []

        googler = ["Open", "High", "Low", "Close"]
        

        col = ["Date", "Low", "Open", "Close", "High"]

        try:
            data = pdr.get_data_yahoo(
                        tickers = ["005930.KS"],
                        start = "2018-12-15",
                        end = "2019-01-06",
                        auto_adjust = True,
                    )
            google = data[googler].reset_index()


            for i in range(len(google)):
                list1 = []
                for j in col:
                    if j == "Date":
                        a = str(google.loc[i][j])[2:10]
                        # str(google.loc[i][j])[:10]
                        list1.append(a)
                    else:
                        a = int(google.loc[i][j])
                        list1.append(a)
                list2.append(list1)
            
            json.dumps(list2)
            return list2
        
        except:
            pass



    def rssNewsHunter(self):
        from matplotlib.backends.backend_agg import FigureCanvasAgg
        import matplotlib.pyplot as plt
        from wordcloud import WordCloud
        from wordcloud import STOPWORDS
        from django.http import HttpResponse
        from urllib.request import Request, urlopen
        from bs4 import BeautifulSoup
        import datetime
        import re
        import os
        
        global titles
        titles = []
        counter = 0
        counter1 = 0
        counts = 0
        
        p = re.compile(r"https?://(\w*:\w*@)?[-\w.]+(:\d+)?(/([\w/_.]*(\?\S+)?)?)?")

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        path = ('mfdw_site/static/rss.txt')
        # mfdw_site/static
        # C:/Users/1990y/Downloads/CH11/mfdw_root/pages/rss.txt
        with open(path, 'r') as f:
            myNames = [p.search(line) for line in f]

        RealName = []

        for i in range(len(myNames)):
            if(str(type(myNames[i])) == "<class 'NoneType'>"):
                myNames[i]
            else:
                RealName.append(myNames[i])

        GoodName = []
        for j in range(len(RealName)):
            GoodName.append(RealName[j].group(0))

        news = GoodName

        
        for i in news:
            Url = i
                
            try:
                Req = Request(Url,headers={'User-Agent': 'Mozilla/5.0'})
                Webpage = urlopen(Req)
                Webpage = BeautifulSoup(Webpage, "html.parser")
                
            except:
                pass
                
            
            try:
                a = Webpage.findAll("url")

                for child in a:

                    if (str(type(child.find("news:title"))) != "<class 'NoneType'>"):
                        titles.append(child.find("news:title").text)
                        counts = counts + 1

                    if (str(type(child.find("title"))) != "<class 'NoneType'>"):
                        titles.append(child.find("title").text)
                        counts = counts + 1
            except:
                continue
                
                
            try:
                if (str(type(Webpage.find("title"))) != "<class 'NoneType'>"):
                    for childer in (Webpage.findAll("title")):
                        titles.append(childer.text)
                        counts = counts + 1
            except:
                continue


        font_path = 'mfdw_site/static//NanumGothic.ttf'
        stopwords = {'Page', 'Error', '잘못되었거나', 
                    'URL이', 'Page의', '찾으시는', 
                    '동아닷컴', '동아일보', '실시간뉴스', 
                    '파이낸셜뉴스', '없습니다',
                    '성인소설', '포토', '사진', 
                    '한국', '사설', '헤럴드경제\'', 
                    'ET투자뉴스', '\''}


        wordcloud = WordCloud(
            stopwords=stopwords,
            font_path = font_path,
            margin = 0,
            width = 560,
            height = 400,
        )

        wordcloud = wordcloud.generate_from_text(str(titles))

        array = wordcloud.to_array()

        
        fig = plt.figure(figsize=(56, 40))
        plt.imshow(array, interpolation="bilinear")
        plt.axis("off")
        plt.tight_layout(pad=0)



        now = datetime.datetime.now()
        nowDatetime = now.strftime('%Y_%m_%d_%H_%M_%S')

        namer = str(nowDatetime) +'.png'

        fig.savefig('mfdw_site/static/trend/'+ namer, bbox_inches='tight')

        Slider.create(namer)
