# SuperFastPython.com
# check the status of many webpages
import asyncio
from urllib.parse import urlsplit


# get the HTTP/S status of a webpage
async def get_status(url):
    # split the url into components
    url_parsed = urlsplit(url)
    # open the connection
    if url_parsed.scheme == "https":
        reader, writer = await asyncio.open_connection(
            url_parsed.hostname, 443, ssl=True
        )
    else:
        reader, writer = await asyncio.open_connection(url_parsed.hostname, 80)
    # send GET request
    query = f"GET {url_parsed.path} HTTP/1.1\r\nHost: {url_parsed.hostname}\r\n\r\n"
    # write query to socket
    writer.write(query.encode())
    # wait for the bytes to be written to the socket
    await writer.drain()
    # read the single line response
    response = await reader.readline()
    # close the connection
    writer.close()
    # decode and strip white space
    status = response.decode().strip()
    # return the response
    return status


# main coroutine
async def main():
    # list of top 10 websites to check
    sites = [
        "https://www.google.com/",
        "https://www.youtube.com/",
        "https://www.facebook.com/",
        "https://twitter.com/",
        "https://www.instagram.com/",
        "https://www.baidu.com/",
        "https://www.wikipedia.org/",
        "https://yandex.ru/",
        "https://yahoo.com/",
        "https://www.whatsapp.com/",
    ]
    # create all coroutine requests
    coros = [get_status(url) for url in sites]
    # execute all coroutines and wait
    results = await asyncio.gather(*coros)
    # process all results
    for url, status in zip(sites, results):
        # report status
        print(f"{url:30}:\t{status}")


# run the asyncio program
asyncio.run(main())
