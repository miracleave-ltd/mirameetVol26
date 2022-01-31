# GoogleMapへ反映  
この手順では、GoogleMapJavaSciriptAPIを使い、BigQueryの情報を絞り込んでピン止めするプログラムを  
Web上で開発出来るCloud Shell Editerを使って開発していきます。  
また、開発したプログラムはCloud Shell Editerで実行し、動作確認をしていきます。  
![](img/draw_flow_0.png)  


## ソースコードの取得  
Googleが提供しているSimpleMapのソースコードをベースに作成していきます。
Googleドキュメントを開きます。  
https://developers.google.com/maps/documentation/javascript/examples/map-simple  

少しページをスクロールしたところにサンプルのソースコードがあります。  
Google Cloud Shellを選択し、コードを取得します。  
![](img/draw_flow_0.png)  

Cloud Shell Editerが開き、ソースコードが配置されています。  
フロントエンドの動作確認は全てCloud Shell Editer上から可能です。  
![](img/draw_flow_0.png)  

まずは、サンプルコードを実行してみましょ。  
左欄からDebugを選び、再生ボタンをクリックします。  
![](img/draw_flow_0.png)  

右上にあるプレビューボタンからWebページの動作を確認します。
![](img/draw_flow_0.png)  

## BigQueryとの連携
手順②で作成したCloud FunctionではBigQueryにアクセスし、検索結果をレスポンスで返却しているので、  
Cloud FuctionのURLをTypeScriptから実行し、レスポンス情報を取得して、GoogleMapAPIに反映します。  

Cloud Functionにアクセスし、レスポンス情報から緯度経度と、建物名を取得します。  
```
   var center;
   var data = new Array();
   fetch(`https://us-central1-sinuous-branch-322702.cloudfunctions.net/function-2`)
    .then(response => {
        console.log(response.status);
        response.json().then(userInfo => {
            for (var i = 0; i < userInfo.length; i++) {
                console.log(userInfo[i].Latitude);
                center = {lat: Number(userInfo[i].Latitude), 
                          lng: Number(userInfo[i].Longitude)};
                data.push({
                        position: new google.maps.LatLng(
                            Number(userInfo[i].Latitude), 
                            Number(userInfo[i].Longitude)),
                        content: userInfo[i].BusinessName});
                console.log(data);
```

緯度経度にピン立てをします。  
複数の住所情報がBigQueryから渡されることを考慮し、ループ処理でピン立てをします。  
ピン立ての変数を宣言します。  
```
let marker: google.maps.Marker;
```
処理を追加します。  
```
                for (var i = 0; i < data.length; i++) {
                  marker = new google.maps.Marker({
                      position: data[i].position,
                      map: map
                });
```

建物名を吹き出しに追加します。  
吹き出しの変数を宣言します。  
```
let infoWindow: google.maps.InfoWindow;
```
処理を追加します。  
```
                infoWindow = new google.maps.InfoWindow({
                      position: data[i].position,
                      content: data[i].content,
                  });
                infoWindow.open(map);
```

プレビューボタンより、動作を確認します。  
![](img/draw_flow_0.png)  

BigQueryに登録したスター情報を絞り込んで検索出来ています。  
また、ピンや吹き出しも追加出来ています。  
![](img/draw_flow_0.png)  
