// content.js

// 스타일 시트에 클래스를 추가하여 스타일을 정의합니다.
const customStyle = document.createElement('style');
customStyle.innerHTML = `
    .black-box {
        position: absolute; /* 이미지와 겹치지 않도록 절대적인 위치로 설정합니다. */
        background-color: black;
        pointer-events: none; /* 이미지 위의 클릭 이벤트를 방지하기 위해 포인터 이벤트를 비활성화합니다. */
    }
`;

// <head> 요소에 스타일을 추가합니다.
document.head.appendChild(customStyle);

// 이미지 옆에 검은색 박스를 추가하는 함수
function addBlackBoxNextToImages() {
    const images = document.querySelectorAll('.imageSpecInfo_product_img__pQD6e img');
    images.forEach(img => {
        const imgRect = img.getBoundingClientRect();
        const box = document.createElement('div');
        box.classList.add('black-box'); // 'black-box' 클래스를 추가합니다.

        // 이미지 옆에 검은색 박스를 위치시킵니다. (이미지 오른쪽에 가로 길이의 절반만큼 떨어진 위치로 설정)
        box.style.top = `${imgRect.top + window.scrollY}px`; // 이미지의 위치와 동일한 높이로 설정합니다.
        box.style.left = `${imgRect.right + window.scrollX + imgRect.width / 3}px`; // 이미지의 오른쪽에 가로 길이의 절반만큼 떨어진 위치로 설정합니다.
        box.style.width = `${imgRect.width/2}px`; // 이미지 가로 길이의 절반만큼의 너비로 설정합니다.
        box.style.height = `${imgRect.height}px`; // 이미지와 동일한 높이로 설정합니다.

        // body 요소에 검은색 박스를 추가합니다.
        document.body.appendChild(box);
    });
}

// 링크 클릭하여 이미지를 불러온 후 이미지 옆에 이미지와 동일한 크기의 검은색 박스를 추가합니다.
function clickLinkAndAddBlackBoxNextToImages() {
    const link = document.querySelector('a[data-nclick="N=a:tab*f."]');
    link.click(); // 링크를 클릭하여 이미지를 불러옵니다.

    // 이미지를 불러온 후에 이미지 옆에 이미지와 동일한 크기의 검은색 박스를 추가합니다.
    setTimeout(addBlackBoxNextToImages, 2000); // 2초 후에 이미지를 검은색 박스로 뒤덮습니다. (이 숫자는 이미지가 나타나는 데 걸리는 시간에 따라 조정 가능)
}

// 링크 클릭하여 이미지를 불러온 후 이미지 옆에 이미지와 동일한 크기의 검은색 박스를 추가합니다.
clickLinkAndAddBlackBoxNextToImages();

// 화면 크기 변경 시 이미지 옆에 검은색 박스의 위치를 업데이트합니다.
window.addEventListener('resize', () => {
    // 검은색 박스를 모두 삭제하고 다시 추가합니다.
    const blackBoxes = document.querySelectorAll('.black-box');
    blackBoxes.forEach(box => box.remove());
    addBlackBoxNextToImages();
});
