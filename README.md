# 🤔
> phira api(游戏内):
> ```
>https://phira.5wyxi.com/

###### 以下请求头均无特殊需求
## phira 绑定账号:
```
post /login
请求体:{"email": ...,"password": ...}
返回示例:
{"error": "邮箱或密码错误"}
{"id": ..., "token": "...", "refreshToken": "...", "expireAt": "..."}
```
"id"与"token"在后续请求中均有用.

## phira 搜索:
```
get /chart?
请求体可不填.
```
###### 搜索id时无视type/division/tags/rating参数的内容。
参数(" --"后为该参数内容/解释):
- search --搜索内容,如:
  NULCTRL
- rating --评分,0.1为半颗星,如:
  0.1,1
- pageNum --返回单页谱面的最大数(≤30),如:
  28
  若>30:{"error":"单页实体数量过多"}
- type --搜索分区(-1-2),-1:热门;0:上架;1:特殊;2:未上架,如:
  0
- page --搜索的页码,如
  2
- tags --搜索的标签,不想要的标签应在前面添加"-",如:
  -高难
  高难
- order --排序方式依次为:
  updated --从新到旧
  -updated --从旧到新
  rating --按评分顺序
  -rating --按评分逆序
- division --页面分区依次为:
  regular --常规
  troll --整活
  plain --纯配置
  visual --观赏
- *uploader --上传者,填写玩家id(可不填)
返回值示例:
```
{"count":1,"results":[{"id":41170,"name":"少女绮想曲~dream battle","level":"IN Lv.15","difficulty":15.0,"charter":"lunaticnight","composer":"zun","illustrator":"","description":"aaaa","ranked":false,"reviewed":true,"stable":false,"stableRequest":false,"illustration":"https://phira.5wyxi.com/files/2756c503-7b59-4956-b168-965e51d16218","preview":"https://phira.5wyxi.com/files/b5eaf47b-7b21-4e9b-8eab-d0ba9a91cd05","file":"https://phira.5wyxi.com/files/fbf0623f-1a8d-4c1a-acc4-dc98da44a315","uploader":...,"tags":["regular"],"rating":0.9103876,"ratingCount":265,"created":"2025-07-08T10:08:22.864544Z","updated":"2025-07-08T10:08:22.864544Z","chartUpdated":"2025-07-08T10:08:22.864544Z"}]}
"count"为搜索结果的总数
"results"中"illustration"为.png格式,"preview"为.ogg,"file"为.pez(.zip)
下载:get对应url即可,无请求头要求.
```

## phira 针对对应谱面id的搜索:
```
get /chart/{id}
将id替换即可.
返回值示例:
{"id":24101,"name":"RE Aoharu","level":"IN Lv.15","difficulty":15.0,"charter":"NC Vigour","composer":"Nor","illustrator":"","description":null,"ranked":true,"reviewed":true,"stable":true,"stableRequest":false,"illustration":"https://phira.5wyxi.com/files/bbc92f10-e8aa-4215-b222-736d0725e1d7","preview":"https://phira.5wyxi.com/files/6fbf2067-4dc5-4c07-97d0-8fe2bd9aac19","file":"https://phira.5wyxi.com/files/4ee6fc2f-4bfe-4d88-bb89-0854eae9e244","uploader":...,"tags":["regular"],"rating":0.96387166,"ratingCount":31334,"created":"2024-07-22T15:36:17.341180Z","updated":"2024-07-22T15:45:50.174726Z","chartUpdated":"2024-07-22T15:36:17.341180Z"}
```
若针对多个谱面:
```
get /chart/multi-get?ids={id}
eg:ids=731,7707,...
返回值示例:
[{"id":731,"name":"RENDA JOCEKY","level":"SP Lv.?","difficulty":20.0,"charter":"縦連打はいいぞ","composer":"ルゼ","illustrator":"","description":"","ranked":false,"reviewed":true,"stable":false,"stableRequest":false,"illustration":"https://api.phira.cn/files/2618e366-0328-4196-acb0-0db5ba2ae9f6","preview":"https://api.phira.cn/files/a7216a14-0448-4d18-9887-f0badd6a3f46","file":"https://api.phira.cn/files/5bf30fa0-f495-4908-9c82-1daeac71c368","uploader":1124,"tags":["visual"],"rating":0.88318634,"ratingCount":18516,"created":"2023-04-23T11:29:40.931192Z","updated":"2023-04-23T11:29:40.931192Z","chartUpdated":"2023-04-23T11:29:40.931192Z"},...]
```

## 查询 phira 某用户的最近游玩:
```
get /record?
```
参数(" --"后为该参数内容/解释):
- player --游玩者,填写玩家id
返回值示例:
```
[{"id":126770474,"player":...,"chart":20442,"score":976394,"accuracy":0.99749845,"perfect":1631,"good":6,"bad":0,"miss":2,"speed":1.0,"max_combo":1289,"best":true,"best_std":true,"mods":0,"full_combo":false,"time":"2026-01-01T03:46:16.773893Z","std":0.026064176,"std_score":544687.56},...]
```

对于查询对应谱面的指定名次:
```
get record/query/{谱面id}?pageNum=20&includePlayer=true&best=true&page=3&std=false
```
###### 搜索时无视best/std参数的内容。
参数(" --"后为该参数内容/解释):
- includePlayer --返回内容是否包含对应玩家的信息
- pageNum --返回单页谱面的最大数(≤30),如:
  28
  若>30:{"error":"单页实体数量过多"}
- page
```
返回值示例:
{"count":3688,"results":[{"id":38864193,"player":22544,"chart":322,"score":936160,"accuracy":0.98472375,"perfect":2675,"good":25,"bad":4,"miss":29,"speed":1.0,"max_combo":1364,"best":true,"best_std":true,"mods":0,"full_combo":false,"time":"2024-02-17T01:58:44.827588Z","std":0.037143614,"std_score":433693.34,"playerName":"小涡_Gary","playerAvatar":"https://api.phira.cn/files/b5578206-067b-43a3-a704-6a20c78296f4","playerBadges":[]},...]}
```

*phira.moe查询的b20+r10:
```
get /record/get-pool/{玩家id}
返回值示例:
{
  "bestPool": [
    {
      "record": 82615873,
      "chart": 7707,
      "rks": 16.80515003179701
    },
  ],
  "recentPool": [
    {
      "record": 82615873,
      "chart": 7707,
      "rks": 16.80515003179701
    },...
  ],
  "rks": 10.142620149388586
}
```
以获取所有谱面的id.

## 查询 phira 某用户的信息:
```
get /user/{玩家id}
返回值示例:
{"id":...,"name":"...","avatar":"https://api.phira.cn/files/968fc111-86a9-4918-9072-8653d22b007e","badges":[],"language":"zh-CN","bio":"喵。采购","exp":0,"rks":7.581084,"joined":"2023-06-23T06:28:55.157546Z","last_login":"2026-01-01T06:12:29.357481Z","roles":0,"banned":false,"login_banned":false,"follower_count":0,"following_count":0,"following":false}
```

###### 以下请求头均需{"authorization":"Bearer {玩家token}"}

## 查询 phira 用户站板娘:
```
get /me/char?
```
参数(" --"后为该参数内容/解释):
- locale,返回的语言,如:
  zh-CN
返回值示例:
```
{"id": "fred2","name": "芙莱（正装）","intro": "...","illust": "@","artist": "清水QR","designer": "清水QR","name_size": 1.0,"baseline": false,"illu_adjust": [0.22,-0.07,0.0,0.0]}
```

## 查询 phira 自身信息(额外返回email):
```
get /me
返回值示例:
{"id":...,"name":"...","avatar":"https://api.phira.cn/files/968fc111-86a9-4918-9072-8653d22b007e","badges":[],"language":"zh-CN","bio":"喵。采购","exp":0,"rks":7.581084,"joined":"2023-06-23T06:28:55.157546Z","last_login":"2026-01-01T07:44:17.601158Z","roles":0,"banned":false,"login_banned":false,"follower_count":0,"following_count":0,"email":"..."}
```

## 查询 phira 活动信息:
```
get message/list
返回值示例:
[{"id":96986,"title":"里糖杯Ⅱ","content":"活动 `里糖杯Ⅱ` 已开始。\n\nThe event `里糖杯Ⅱ` is started.","author":"Mivik","time":"2025-07-09T17:44:21.396461Z"},...]
```
