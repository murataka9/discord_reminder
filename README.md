# discord_reminder
Discord 版 リマインくんっぽいの

## どんなの？ / What's this?
リマインくん <入力>
- `- w <week>` 毎週`<week>`曜日に通知
- `- t <time>` 時間`<time>`に通知 書式 `<HH:MM>`

追加予定:wq

## Usage
1. install discord.py using pip
2. nohup python3 main.py &

## Require
- Python 3.x

&&

```zsh
$ pip3 install discord
```

&&

Please create key.py like bottom OR Get from admin if you're not admin -- Your Token is secure

```Python3
def Token():
    token = 'Your Token (string)'
    return token
```