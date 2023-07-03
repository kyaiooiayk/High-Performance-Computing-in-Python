#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span></li><li><span><a href="#What-is-caching?" data-toc-modified-id="What-is-caching?-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>What is caching?</a></span></li><li><span><a href="#How-is-caching-used-behind-the-scene" data-toc-modified-id="How-is-caching-used-behind-the-scene-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>How is caching used behind the scene</a></span></li><li><span><a href="#Using-and-controlling-caching" data-toc-modified-id="Using-and-controlling-caching-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Using and controlling caching</a></span></li><li><span><a href="#References" data-toc-modified-id="References-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>References</a></span></li></ul></div>

# # Introduction
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# **What?** Code profiling
#
# </font>
# </div>

# # What is caching?
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Caching: a mechanism that minimizes unnecessary computations and speeds up your programs.
# - Caching consists in keeping recently (or frequently) used data in a memory location that has cheap and fast access for repeated queries.
#
# - We'll talk about the TTL Cache here, but other types of cache are also available. Which one to use highly depends on your needs. There are:
#     - **LFUCache** (Least Frequently Used): keeps a count of how often an item is retrieved and discards items that are least used
#     - **LRUCache** (Least Recently Used): discards the least recently used items
#     - **RRCache** (Random Replacement): randomly select items and discard them
#
# </font>
# </div>

# # How is caching used behind the scene
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - Let’s consider an application where caching is commonly used: web servers.
# - What we want is to store the content of each post in local memory (an object in RAM for example) and reusing it later if the user requests the same link later.
#
# </font>
# </div>

# In[1]:


import requests

# initialize cache a the beginning
cache = dict()


def extract_article_content(url):
    response = requests.get(url)
    content = response.content
    return content


def fetch_article(url):
    if url not in cache:
        content = extract_article_content(url)
        cache[url] = content

    return cache[url]


# In[2]:


url = "http://google.co.uk"


# In[3]:


get_ipython().run_cell_magic(
    "timeit", "-n 1", "# run it for the first time\nfetch_article(url)"
)


# In[4]:


get_ipython().run_cell_magic(
    "timeit", "-n 1", "# Run it again and it will be much faster\nfetch_article(url)"
)


# # Using and controlling caching
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-info">
# <font color=black>
#
# - `maxsize` specifies the number of objects we store in the cache. I set it to 100 but it can vary depending on your use case.
# - `ttl` is short for Time To Live which is basically the time each result is being stored in a cache. After this time, the cached result expires. I arbitrarily set it to 86400s which corresponds to a full day.
#
# </font>
# </div>

# In[5]:


from cachetools import cached, TTLCache

cache = TTLCache(maxsize=100, ttl=86400)


@cached(cache)
def extract_article_content(url):
    response = requests.get(url)
    content = response.content
    return content


# In[6]:


get_ipython().run_cell_magic(
    "timeit",
    "-n 1",
    "# run it for the first time\ncontent = extract_article_content(url)",
)


# In[7]:


get_ipython().run_cell_magic(
    "timeit",
    "-n 1",
    "# run it for the first time\ncontent = extract_article_content(url)",
)


# # References
# <hr style="border:2px solid black"> </hr>

# <div class="alert alert-warning">
# <font color=black>
#
# - https://towardsdatascience.com/how-to-speed-up-your-python-code-with-caching-c1ea979d0276
#
# </font>
# </div>
