var preset_coordinates = (33.45066339978431, 126.56769289645109);

var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = {
        center: new daum.maps.LatLng(36.36086, 127.38442), // 지도의 중심좌표
        level: 3 // 지도의 확대 레벨
    };

var target_address = new String();

//지도를 미리 생성
var map = new daum.maps.Map(mapContainer, mapOption);
//주소-좌표 변환 객체를 생성
var geocoder = new daum.maps.services.Geocoder();
//마커를 미리 생성
var marker = new daum.maps.Marker({
    position: new daum.maps.LatLng(0, 0),
    map: map
});
var coords = {'lat':0, 'lng':0};
// 지도가 이동, 확대, 축소로 인해 중심좌표가 변경되면 마지막 파라미터로 넘어온 함수를 호출하도록 이벤트를 등록합니다
kakao.maps.event.addListener(map, 'center_changed', function() {

    // 지도의 중심좌표를 얻어옵니다
    var latlng = map.getCenter();
    coords = latlng;
    update_marker(latlng);
});

function update_marker(x, y) {
    marker.setPosition(x, y);
};

function parse_jibunAddress(jibunAddress) {
    result = new String();
    for (const item of jibunAddress.split(' ')) {
        if (item[item.length - 1] == '리')
            continue;
        if (item.match(/\d+/g) != null)
            break
        result = result + ' ' + item;
    }
    if (result[result.length-1] == '산')
        return result.slice(1, result.length - 2);
    else
        return result.slice(1, result.length);
}

function addressSearch() {
    var userAddress = document.getElementById('address-input').value;
    new daum.Postcode({
        oncomplete: function(data) {
            var addr = data.address; // 최종 주소 변수
            target_address = parse_jibunAddress(data.jibunAddress);
            if (obj[target_address] != undefined) {
                update_option(obj[target_address]);
                setAddress(target_address); // save to manager
            }
            else
                alert('자료가 부족하여 아직 해당 지역에는 적용이 불가합니다.');
            // 주소 정보를 해당 필드에 넣는다.
            document.getElementById("address-input").value = addr;

            // 주소로 상세 정보를 검색
            geocoder.addressSearch(data.address, function(results, status) {
                // 정상적으로 검색이 완료됐으면
                if (status === daum.maps.services.Status.OK) {
                    var result = results[0]; //첫번째 결과의 값을 활용
                    // 해당 주소에 대한 좌표를 받아서
                    coords = new daum.maps.LatLng(result.y, result.x);
                    // 지도 중심을 변경한다.
                    map.setCenter(coords);
                    // 마커를 결과값으로 받은 위치로 옮긴다.
                    marker.setPosition(coords);
                    updateAddressInput();
                }
            });
        }
    }).open({
        q: userAddress
    });
}
