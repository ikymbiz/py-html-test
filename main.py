import datetime

def greet():
    now = datetime.datetime.now()
    return f"こんにちは！現在は {now.strftime('%H時%M分')} です。これは外部ファイルから実行されています。"

# 画面に表示
print(greet())
