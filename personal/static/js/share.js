const url = 'https://hanguel-spelling-test.github.io/';

function setShare() {
  var resultImg = document.querySelector('#resultImg');
  var resultAlt = resultImg.firstElementChild.alt;
  const shareTitle = '한국어능력고사 결과';
  const shareDes = infoList[resultAlt - 1].name;
  const shareImage = url + 'img/lv' + resultAlt + '.png';
  const shareURL = url + 'page/result-' + resultAlt + '.html';

    Kakao.Link.sendDefault({
    objectType: 'feed',
    content: {
      title: shareTitle,
      description: shareDes,
      imageUrl: shareImage,
      link: {
        mobileWebUrl: shareURL,
        webUrl: shareURL
      },
    },
    buttons: [
      {
        title: '결과 확인하기',
        link: {
          mobileWebUrl: shareURL,
          webUrl: shareURL
        },
      }
    ]
  });
}

function shareTwitter() {
    window.open("http://twitter.com/share?url=" + encodeURIComponent(location.href) +"&text=" + document.title);
}

function shareURL() {
  copyToClipboard('https://hanguel-spelling-test.github.io/');
  alert('링크가 복사되었습니다!');
}