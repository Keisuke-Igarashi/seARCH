const archs_js = archs; 
const markers = [];
var map;


window.addEventListener("load", function() {
    
    //　マップの作成
    map = L.map('map').setView([35.7, 139.6], 4);


    // マーカーの作成
    // 検索結果が空白以外の場合のみマーカ作成する
    if (archs_js != ''){

        archs_js.forEach(function(element,index) {
            
            //マーカの作成
            markers.push(L.marker([element.latitude, element.longitude]).addTo(map));

            //マーカーのダブルクリックイベントの登録
            markers[index].on('dblclick', function addToFavarite(){
     
                //建物IDを取得する
                var architecture_id = element.architecture_id;

                //axiosライブラリを利用してPOSTリクエストする
                axios.post('/favorite', {
                    architecture_id: architecture_id
                })
                .then(function (response) {
                    console.log(response);
                })
                .catch(function (error){
                    console.log(error);
                })
                 
            })
            
            //マーカーのクリックイベントの登録
            markers[index].on('onclick', function onMarkerClick(){

                window.open('/test.html', '_blank') //新しいタブを開きページを表示
            
            })
        })


    }

     
    // marker.on('contextmenu', onMarkerRightClick)
    

    // var marker = L.marker([35.7, 139.6], markerContextMenu).addTo(map);
    // var marker = L.marker([42.7, 141.8]).addTo(map);

    // レンダリング処理
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap'
    }).addTo(map);

    // // マーカーへのポップアップ機能
    // marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();

   
    // イベント対応

    // var popup = L.popup();

    // function onMapClick(e) {
    //     popup
    //         .setLatLng(e.latlng)
    //         .setContent("you clicked the map at" + e.latlng.toString())
    //         .openOn(map)
    // }

    // map.on('click', onMapClick)


});