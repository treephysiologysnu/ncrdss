const id2CompletedFlag = {
    tab3: ['address'],
    tab4: ['table_base', 'table_SpcClasses', 'table_currentSpc'],
    tab5: ['table_thinning', 'table_ForManPlan'],
}; // tab id 를 입력하면, 체크해야할 manager.completedFlags[key] 에서 key가 뭔지 알려줌.

const checkTabCompleted = function (id) {
    const flagsToCheck = id2CompletedFlag[id];
    for (const flag of flagsToCheck) {
        if (!manager.completedFlags[flag])
            return false;
    }
    return true;
}

const tabClick = ({ target }) => {
    const { dataset: { id = '' }} = target;
    console.log(id);
    if (Object.keys(id2CompletedFlag).includes(id)) {
        if (!checkTabCompleted(id)) {
            alert('이전 입력들이 완료되지 않았습니다.')
            // return false;
        }
    }
    document.querySelectorAll('.tab-li').forEach(t => t.classList.remove('selected'));
    document.querySelectorAll('.tab-a').forEach(t => t.classList.remove('selected'));
    target.classList.add('selected');
    document.querySelectorAll('.page-content').forEach(t => t.classList.add('hidden'));
    document.querySelector(`#${id}`).classList.remove('hidden');
    if (id === 'tab2' && String(target_address) === "") { // 지도를 다시 로딩해서 제대로 출력되게 함
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