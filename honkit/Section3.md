# 検索プログラムの作成  
この手順では、BigQueryを検索するプログラムをJavaScriptで作成します。  
また、作成したプログラムはNode.Jsで実行するため、サーバーレスで実行可能なCloud Funcitonにデプロイしていきます。  
![](img/draw_flow_0.png)  

## Cloud Functionの設定  
Cloud Functionを設定します。  
【ToDo】詳細な設定手順を記載する
![](img/draw_flow_0.png)  

## BigQueryAPIのコード  
BigQueryAPIにアクセスするコードを記述していきます。
requireでBigQueryAPIを読み込みます。
```
const { BigQuery } = require('@google-cloud/bigquery');
```
BigQueryのオブジェクトを生成し、BigQueryのプロジェクトIDを記述します。  
プロジェクトIDはアカウントによって異なります。  
```
const bigquery = new BigQuery({
    projectId: '【プロジェクトID】'
});
```
BigQueryを検索するSQLを記述します。  
今回はAddressをLIKE検索で絞り込みたいと思います。  
```
const query = "SELECT "+
              " features.properties.Location.GeoCoordinates.Latitude AS Latitude "+
              " , features.properties.Location.GeoCoordinates.Longitude AS Longitude "+
              " , features.properties.Location.BusinessName AS BusinessName "+
              "FROM TEST.TEST1 "+
              "WHERE features.properties.Location.Address LIKE '%【検索キーワード】%'";

```

BigQueryに登録されているデータは、ネストされた形式になっています。  
通常のSQLだとエラーとなるため、LegacySQLで取得する必要があるため、useLegacySqlを"true"に設定します。
```
//with options
const options = {
    query: query,
    useLegacySql: true,
}
```

次にメイン処理を追加します。
BigQueryAPIにリクエストを投げて、レスポンス情報を取得する簡単なロジックになります。  
```
exports.main = (req, res) => {
    bigquery.createQueryJob(options)
        .then(results => {
            const [job] = results;
            return job.getQueryResults();
        })
        .then(results => {
            const [rows] = results;
            res.header('Access-Control-Allow-Origin', "*");
            res.header('Access-Control-Allow-Headers', "Origin, X-Requested-With, Content-Type, Accept");
            res.status(200).send(rows);
        })
        .catch(error => {
            console.log(error);
        })
}
```

最後に、BigQueryにアクセスするため、BigQueryAPIの依存関係を追加します。  
```
  "dependencies": {
    "@google-cloud/bigquery": "^5.10.0"
  }
```

Cloud Functionをデプロイします。
【ToDo】詳細な設定手順を記載する
![](img/draw_flow_0.png)  

動作確認をします。
![](img/draw_flow_0.png)  

以上で、バックエンドの処理は完了です。

