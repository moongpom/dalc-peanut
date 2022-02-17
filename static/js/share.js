const url = 'https://127.0.0.1:8000';

function shareKakao() {
  var shareImage = document.querySelector('.mainImg');
  const shareTitle = '퍼스널컬러 진단 서비스 Peanut';
  const shareDes = 'Peanut은 퍼스널컬러를 쉽게 진단할 수 있는 서비스입니다';

    Kakao.Link.sendDefault({
    objectType: 'feed',
    content: {
      title: shareTitle,
      description: shareDes,
      imageUrl: shareImage,
      link: {
        mobileWebUrl: url,
        webUrl: url
      },
    },
    buttons: [
      {
        title: '나도 해보기',
        link: {
          mobileWebUrl: url,
          webUrl: url
        },
      }
    ]
  });
}

function shareTwitter() {
    var sendText = "#퍼스널컬러 #테스트 #peanut";
    window.open("https://twitter.com/intent/tweet?text=" + sendText + "&url=" + url);
}

function shareURL() {
  copyToClipboard(url);
  alert('링크가 복사되었습니다!');
}