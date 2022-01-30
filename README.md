# document-template

本ツールはmeetup時の手順書テンプレートとしての利用想定となります。  
[Hokit](https://honkit.netlify.app/)を利用して、md → html変換を行い、GitHubPagesを利用して公開を行います。  
Honkitは、GitBookをForkして作成されています。  
作成方法などは以下を参考にしてください。  
https://honkit.netlify.app/
## 環境構築

1. イメージビルド  
    document-template配下で以下のコマンドを実行する。  
    ```
    docker-compose build
    ```
## 使い方

document-tempkate/honkit配下に`.md`ファイルを作成することでHTMLが作成できます。  
`SUMMARY.md`はサイドメニューに表示するページなどをまとめているファイルとなっており、自動でサイドメニューが作成されるわけではないので注意してください。

- Localサーバー起動  
    以下のコマンドを実行することでhttp://localhost:4000で手順書を確認することができます。
    ```
    sh restart.sh
    ```
- .md → .html変換
    ```
    sh build.sh
    ```
- GitHubPages用html作成  
    GitHubPagesにて公開する際、以下のコマンドを実行したうえでコミットしてください。  
    GitHub側の設定を行うことでPublicに公開されます。
    ```
    sh github-page.sh
    ```
- PDF作成
    ```
    sh pdf.sh
    ```