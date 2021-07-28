# store-tutorial-eventdrt

こちらはMONETマーケットプレイスを利用したデモアプリ「イベント×マルチモーダル」の公開リポジトリです。

デモアプリの構成は以下の通りです(PlantUMLを利用しています)。


```plantuml
@startuml

skinparam shadowing false
skinparam RoundCorner 5
skinparam ArrowColor DimGray
skinparam FontColor DimGray
skinparam sequenceLifeLineBorderColor DimGray


skinparam participant {
  BackgroundColor Tomato
  BorderColor #DDDDDD
  FontColor White
}

skinparam boundary {
  BackgroundColor Aqua
  BorderColor DimGray
}

skinparam BoxPadding 10
title デモアプリ構成

actor "Enduser" as enduser

box "開発対象"
    participant "Frontend" as frontend
    participant "Backend" as backend
end box

box "MONET Authentication"
    participant "MONET 認証サーバ" as auth #888888
end box

box "MONET Gateway"
    boundary    "MONET Gateway" as gw
end box


box "API"
    participant "デマンド交通サービス開発キット" as drtkit #888888
    participant "..." as other #888888
end box
group ログインセッション
enduser -> frontend: ログイン
frontend -> auth: 認証要求
auth -> frontend: IDトークン
end
group APIリクエスト
enduser -> frontend: 各種操作
frontend -> backend: IDトークンを\n付与してリクエスト
backend -> gw: GW用のAPIキーや\nパラメータを付与して中継
gw -> drtkit: リクエスト
drtkit -> gw: レスポンス
gw -> backend
backend -> frontend
end

@enduml
```

バックエンドはPythonで実装し、フロントエンドはVue 2.0(typescript)で実装しています。
詳細はそれぞれのディレクトリを参照してください。
