let w1 = window


const archs_js = archs;     
const markers = [];
var map;
var response_json;


window.addEventListener("load", function() {
    
    //　マップの作成
    map = L.map('map').setView([35.7, 139.6], 4);

    
    // レンダリング処理
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap'
    }).addTo(map);

    // マーカーの作成
    // 検索結果が空白以外の場合のみマーカ作成する
    if (archs_js != ''){

        archs_js.forEach(function(element,index) {
            
            //マーカの作成
            markers.push(L.marker([element.latitude, element.longitude]).addTo(map));

            //マーカーのツールチップ表示
            let tooltip = archs_js[index].architecture_name.toString();
            markers[index].bindTooltip(tooltip).openTooltip();

            //マーカーのクリックイベントの登録
            markers[index].on('click', function onMarkerClick(){
                
                //建物IDを取得する
                var architecture_id = element.architecture_id;

                //axiosライブラリを利用してPOSTリクエストする
                axios.post('/detail', {
                    architecture_id: architecture_id
                })
                .then(function (response) {
                    console.log(response.data); 
                    // window.open('/detail');
                    window.location.href = '/detail';
                })
                .catch(function (error){
                    console.log(error);
                })          
            
            })

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
                    alert('お気に入り登録が完了しました');
                })
                .catch(function (error){
                    console.log(error);
                })
                 
            })
            
           
        })


    }

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