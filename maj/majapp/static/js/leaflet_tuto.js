window.addEventListener("load", function() {
    
    //　マップの作成
    var map = L.map('map').setView([35.7, 139.6], 13);

    // マーカの右クリック（Contextmenuの設定)
    var markerContextMenu = {
        contextmenu: true,
        contextmenuItems:[{
            text: '建築情報を表示',
            index: 0,
            callback: onMarkerClick
        }, {
            text: 'この建築物をお気に入りに登録',
            callback: onMarkerRightClick
        }]
    }
    
    // マーカーの作成
    var marker = L.marker([35.7, 139.6], markerContextMenu).addTo(map);
    // var marker = L.marker([42.7, 141.8]).addTo(map);

    // レンダリング処理
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap'
    }).addTo(map);

    // // マーカーへのポップアップ機能
    // marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();

    // マーカクリック時の挙動定義

    function onMarkerClick(e) {
        window.open('/test.html', '_blank') //新しいタブを開きページを表示
    }

    marker.on('click', onMarkerClick)

    // 右クリックイベント関数作成

    function onMarkerRightClick(e) {
        window.open('/okiniiri.html', '_blank') //新しいタブを開きページを表示
    }

    // marker.on('contextmenu', onMarkerRightClick)


    // イベント対応

    var popup = L.popup();

    function onMapClick(e) {
        popup
            .setLatLng(e.latlng)
            .setContent("you clicked the map at" + e.latlng.toString())
            .openOn(map)
    }

    map.on('click', onMapClick)

});
