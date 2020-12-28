const tabClick = ({ target }) => {
    const { dataset: { id = '' }} = target;
    document.querySelectorAll('.tab-li').forEach(t => t.classList.remove('selected'));
    document.querySelectorAll('.tab-a').forEach(t => t.classList.remove('selected'));
    target.classList.add('selected');
    document.querySelectorAll('.page-content').forEach(t => t.classList.add('hidden'));
    document.querySelector(`#${id}`).classList.remove('hidden');
    if (id == 'tab2' & target_address == "") { // 지도를 다시 로딩해서 제대로 출력되게 함
        map.relayout();
        map.setCenter(new daum.maps.LatLng(36.36086, 127.38442));
    }
};

const bindClickListener = () => {
    document.querySelectorAll('.tab-a').forEach(tab => {
        tab.addEventListener('click', tabClick);
    })
};
document.addEventListener('DOMContentLoaded', () => {
    bindClickListener();
});