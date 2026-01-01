# 🤔
> phira api:
> ```
>https://phira.5wyxi.com/
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
参数(" --"后为该参数内容/解释):
- search --搜索内容,如:
  NULCTRL
- rating --评分,0.1为半颗星,如:
  0.1,1
- pageNum --返回单页谱面的最大数(<31),如:
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
- division --分区依次为:
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
