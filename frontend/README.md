# EventDRT フロントエンド

## What is it?

MONETマーケットプレイスを利用した、イベント×マルチモーダルのデモアプリのフロントエンド実装です。

開発環境としてはDocker on Mac、Vue 2.0 (typescript)による実装です。


本プロジェクトはデモアプリであるため、エラーハンドリングなどはほとんど行っていません。

あくまでも参考としての公開であり、実際のシステムに組み込む際には適宜追加の設計や実装が必要になる点にご注意ください。

## プロジェクトのセットアップと実行

まず、認証認可設定として、```vue-client/src/auth_config.json.org```を編集し
```vue-client/src/auth_config.json```として保存します。

```json
{
  "domain": "store-auth.monet-technologies.co.jp",
  "clientId": "your client id",
  "audience": "https://odb-api.monet-technologies.co.jp"
}
```

ここで編集する箇所は```clientId```の項目のみです。
MONETマーケットプレイスへの問い合わせ経由で連携したサービスアプリケーション用のクライアントIDの設定が必要です。

```bash
docker compose up -d
```
を実行することでコンテナが立ち上がり、コンテナ上で必要なモジュールのインストールとホスティングが開始されます。
ただし、実際の動作には別途バックエンド側も実行されている必要があります。

本プロジェクトのデフォルトの設定では、

- フロントエンド http://localhost:3000
- バックエンド http://localhost:15050

でのアクセスを想定しています。必要に応じて適宜変更してください。
なお、フロントエンドからバックエンドへのアクセス設定は```vue.config.js```内部に記述されています。