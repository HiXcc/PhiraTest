import requests
import json
from datetime import datetime, timezone, timedelta
import shutil
import os

def get_phira_id_name(id):
    link = f"https://phira.5wyxi.com/chart?tags=&division=regular&search=%23{id}&rating=0.3%2C1&page=1&type=2&pageNum=28&order=-updated"
    results = requests.get(link)
    try:
        return results.json()["results"][0]["name"]
    except:
        return ""
    
def bind_command(user,email:str, password:str):
    if not os.path.exists("account.json"):
        with open("account.json","w",encoding="utf-8") as f:
            f.write("{}")
    with open("account.json","r",encoding="utf-8") as f:
        account:dict = json.loads(f.read())
    j = {"email": email,"password": password}
    r = requests.post("https://phira.5wyxi.com/login",json=j)
    r = r.json()
    if "error" in r:
        print(r["error"])
    else:
        account.update({user:[r["token"],str(r["id"])]})
        with open("account.json","w",encoding="utf-8") as f:
            json.dump(account,f)
        #https://phira.5wyxi.com/user/108942
        reply_headers = {"authorization": f"Bearer {r["token"]}"}
        reply_req = requests.get(f"https://phira.5wyxi.com/user/{str(r["id"])}",headers=reply_headers).json()
        print(f"绑定完成:\n名称:{reply_req["name"]}\nrks:{reply_req["rks"]}\navatar:{reply_req["avatar"]}")
    
def phira_command(user,chart_id:str, std:bool=False):
    if not os.path.exists("account.json"):
        with open("account.json","w",encoding="utf-8") as f:
            f.write("{}")
    with open("account.json","r",encoding="utf-8") as f:
        account:dict = json.loads(f.read())
    if user in account:
        user = account[user]
        #https://phira.5wyxi.com/record/list15/47605?std=false
        #https://phira.5wyxi.com/record?player=108942
        #std:无暇度
        if chart_id[0] == "#":
            chart_id = chart_id[1:]
        url = f"https://phira.5wyxi.com/record/list15/{chart_id}?std={str(std).lower()}"
        header = {"authorization": f"Bearer {user[0]}"}
        r = requests.get(url,headers=header)
        r = r.json()
        for i in r:
            song_name = get_phira_id_name(i["chart"])
            if str(i["player"]) == user[1]:
                if get_phira_id_name(chart_id) != "":
                    utc_time = datetime.fromisoformat(i["time"].replace('Z', '+00:00'))
                    beijing_time = utc_time.replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
                    text = f"{song_name}(#{i["chart"]}):\n分数:{i["score"]}\nacc:{i["accuracy"]*100}%\n判定详情:{i["perfect"]}-{i["good"]}-{i["bad"]}-{i["miss"]},maxcombo:{i["max_combo"]},fc:{i["full_combo"]}\n无暇度:±{i["std"]*1000}ms,{i["std_score"]}\n倍速:{i["speed"]}\n上传时间:{beijing_time.strftime('%Y-%m-%d %H:%M:%S.%f')}\n排名:{i["rank"]}"
                    print(text)
                    break
    else:
        print(f"未绑定账号!请绑定.")

def pr_command(user):
    if not os.path.exists("account.json"):
        with open("account.json","w",encoding="utf-8") as f:
            f.write("{}")
    with open("account.json","r",encoding="utf-8") as f:
        account:dict = json.loads(f.read())
    if user in account:
        user = account[user]
        #https://phira.5wyxi.com/record/list15/47605?std=false
        #https://phira.5wyxi.com/record?player=108942
        #std:无暇度
        url = f"https://phira.5wyxi.com/record?player={user[1]}"
        header = {"authorization": f"Bearer {user[0]}"}
        r = requests.get(url,headers=header)
        r = r.json()
        for i in r:
            song_name = get_phira_id_name(i["chart"])
            if song_name != "":
                utc_time = datetime.fromisoformat(i["time"].replace('Z', '+00:00'))
                beijing_time = utc_time.replace(tzinfo=timezone.utc).astimezone(timezone(timedelta(hours=8)))
                text = f"{song_name}(#{i["chart"]}):\n分数:{i["score"]}\nacc:{i["accuracy"]*100}%\n判定详情:{i["perfect"]}-{i["good"]}-{i["bad"]}-{i["miss"]},maxcombo:{i["max_combo"]},fc:{i["full_combo"]}\n无暇度:±{i["std"]*1000}ms,{i["std_score"]}\n倍速:{i["speed"]}\n上传时间:{beijing_time.strftime('%Y-%m-%d %H:%M:%S.%f')}"
                print(text)
                break
            else:
                print(f"未找到{i["chart"]}这个谱面")
                continue
    else:
        print(f"未绑定账号!请绑定.")

def download_command(chart_id):
    if chart_id[0] == "#":
        chart_id = chart_id[1:]
    link = f"https://phira.5wyxi.com/chart?tags=&division=regular&search=%23{chart_id}&rating=0.3%2C1&page=1&type=2&pageNum=28&order=-updated"
    try:
        url = requests.get(link).json()["results"][0]["file"]
        name = requests.get(link).json()["results"][0]["name"]
        unnamed = ["?","/","\\",":","*","|","<",">","\""]
        for string in unnamed:
            name = name.replace(string,"")
        r = requests.get(url,stream=True)
        with open(f"{name}-{chart_id}.pez","wb") as file:
            shutil.copyfileobj(r.raw,file)
        print(f"file:{url}\n{name}-{chart_id}.pez")
    except KeyError:
        print(f"未找到#{chart_id}这个谱面")

while True:
    a = input("请输入命令\n1:绑定账号\n2:查询对应编号谱面的排行榜\n3:查询最近一次上传成功的成绩\n4:下载谱面\n5:quit\n")
    if a.isdigit():
        a = int(a)
        match a:
            case 1:
                print("请依次填写用户名,phira邮箱,phira密码")
                user = input("请输入用户名:")
                account = input("请输入邮箱:")
                password = input("请输入密码:")
                bind_command(user,account,password)
            case 2:
                print("请依次填写用户名,谱面id,是否是无暇度排行")
                user = input("请输入用户名:")
                id = input("谱面id:")
                std = input("是否是无暇度排行(true/false):")
                phira_command(user,id,std)
            case 3:
                user = input("请输入用户名:")
                pr_command(user)
            case 4:
                chart_id = input("请输入谱面id:")
                download_command(chart_id)
            case 5:
                break
    else:
        print("输入无效,请输入对应数字")