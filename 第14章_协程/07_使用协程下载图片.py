import aiohttp
import asyncio

async def download_image(session, url):
    print("开始下载图片：", url)
    # 发送网络请求，获取图片，请求发出去后，要等待服务器把数据返回，等的这段时间就是IO等待
    response = await session.get(url)
    # 等待数据（图片数据可能分多次传输，需要等待数据全部读完，等的这段时间也是IO等待）
    content = await response.read()
    print("图片下载完成")
    # 保存图片到本地
    with open(url[-10:], 'wb') as file:
        file.write(content)
    # 释放连接资源（告诉 aiohttp，这个连接我不用了，你可以回收了）
    await response.release()
    # session.release()  # 这个方法是同步的，不需要await


async def main():
    url_list = [
        "https://n.sinaimg.cn/spider20260129/217/w600h417/20260129/3e26-917ee55a8a42b8626807c332c24981de.png",
        "https://n.sinaimg.cn/finance/transform/97/w630h267/20260129/97c4-b211cc51784830f09ee19e450475c93b.png",
        "https://n.sinaimg.cn/spider20260129/539/w1439h700/20260129/e09a-cc2ca319e00f701ccfca3ebc62aa8772.png",
    ]
    # 创建会话对象（发请求的工具）
    session = aiohttp.ClientSession()
    # 创建多个协程对象
    coroutine_list = [download_image(session, url) for url in url_list]
    # 将多个协程对象交给事件循环
    await asyncio.gather(*coroutine_list)
    # 关闭会话
    await session.close()

asyncio.run(main())
