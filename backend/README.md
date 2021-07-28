# EventDRT バックエンド

## What is it?

MONETマーケットプレイスを利用した、イベント×マルチモーダルのデモアプリのバックエンドサーバです。

Python 3.8.5での動作を確認しています。


本プロジェクトはデモアプリであるため、デモアプリであるためエラーハンドリングなどはほとんど行っていません。

あくまでも参考としての公開であり、実際のシステムに組み込む際には適宜追加の設計や実装が必要になる点にご注意ください。


## プロジェクトのセットアップ

```bash
pip install -r requirements.txt
```

## プロジェクトの実行

auth_config.json.orgを自身のAPIキーに書き換え、auth_config.jsonとして保存します。

```json
{
  "MONET_KEY": "your_api_key"
}
```

その後、以下のコマンドでEventDRT用のバックエンドサーバが立ち上がります。

```bash
python proxy_server.py
```

フロントエンド側の設定に応じてポートなどは適宜変更してください。