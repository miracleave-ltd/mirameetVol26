# 【タイトル】  
第26回目の開催となる【タイトル】です！  

---

## 今回のやりたいこと
GoogleMapではお気に入りの地図情報をリストとして保存することが出来ますが、リスト内の検索が出来ません・・・。  
では、作ってしまおう!!ということで、
今回は、お気に入りの地図情報をBigQueryに溜めて絞り込みを行い、GoogleMapに反映してみたいと思います！  
BigQueryの絞り込みや、GoogleMapの反映はGoogleMapAPI・BigQueryAPIを使用します。  
また、開発の実行環境はCloud Shell Editer、バックエンドのサーバーはClud Functionを使用します。  

## 事前準備
- Googleアカウント作成
- GCPアカウントの作成

## 手順
![](img/draw_flow_0.png)  
全体手順としては次の流れで進めます。  
 0.事前準備内容の確認  
 1.テストデータの登録  
 2.検索プログラムの作成  
 3.GoogleMapへ反映  

## 技術要素
参考サイトのリンクを記載しておきますので、参考にお使いください。  
- [GoogleMapAPI](https://developers.google.com/maps/documentation/javascript/local-context/samples/neighborhood)
- [BigQueryAPI](https://qiita.com/zaburo/items/344ed0caab369c2f94c5)
- [JSON形式のBigQuery取り込み](https://cloud.google.com/bigquery/docs/loading-data-cloud-storage-json#bq)

---

今回の手順ではGoogleChromeのみ使用します。OS問わずハンズオン可能です。
