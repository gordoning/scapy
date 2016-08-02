import requests

# 下载某个地址的图片，放到指定的目录的位置
def download_pic(src):
    req = requests.get(url=src)
    fname = src.split("/")[-1]
    with open("meinv/"+fname,'wb') as file:
        file.write(req.content)


if __name__ == "__main__":
    src = "http://f.hiphotos.baidu.com/ imgad / pic / item / fcfaaf51f3deb48f397c42b3f71f3a292df57842.jpg".replace(' ','')
    download_pic(src)