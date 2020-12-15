#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests


# In[2]:


import json


# In[3]:


import urllib


# In[4]:


import pandas as pd


# In[5]:


from pandas import DataFrame


# In[6]:


api_key = "4d6aca65473af926115dec15546b1228"


# In[7]:


user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"


# In[8]:


session = requests.Session()


# In[9]:


session.headers.update( {'User-agent': user_agent, 'referer': None, 'Authorization': 'KakaoAK ' + api_key} )


# In[10]:


url_tpl = "https://dapi.kakao.com/v2/search/web"


# In[11]:


wanted_word = "코로나"


# In[12]:


page = 1


# In[13]:


size = 50


# In[14]:


content_list = []
    
for i in range(0,6):
    page = i + 1      # 1~6까지가 된다.
    
    # API에 전달할 파라미터 인코딩
    params = {"page": page, "query": wanted_word, "size": size}
    query = urllib.parse.urlencode(params)
    
    # 최종 접속 주소 구성
    api_url = url_tpl + "?" + query
    api_url
    
    # API에 접근하여 데이터 가져오기
    r = session.get(api_url)

    if r.status_code != 200:
        print("[%d Error] %s" % (r.status_code, r.reason))
        continue
        
    # 가져온 결과를 딕셔너리로 변환
    r.encoding = "utf-8"
    blog_dict = json.loads(r.text)

    # DataFrame 생성
    blog_df = DataFrame(blog_dict['documents'])
    
    # 내용에 해당하는 컬럼만 리스트로 추출하여 미리 준비한 리스트에 병합
    content_list += list(blog_df['contents'])
    
content_list


# In[15]:


text = " ".join(content_list)
text


# In[16]:


from konlpy.tag import Okt


# In[20]:


from collections import Counter


# In[17]:


nlp = Okt()


# In[18]:


nouns = nlp.nouns(text)
nouns


# In[19]:


words = []

for n in nouns:
    if len(n) > 1:
        words.append(n)
        
words


# In[21]:


count = Counter(words)
most = count.most_common(100)
most


# In[ ]:




