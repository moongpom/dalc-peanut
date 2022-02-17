const url = 'https://127.0.0.1:8000';

function shareKakao() {
  var shareImage = 'https://ifh.cc/g/0Jt2XM.png';
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
        title: '확인하기',
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
  var url = 'https://127.0.0.1:8000';
  var textarea = document.createElement("textarea");
  document.body.appendChild(textarea);
  textarea.value = url;
  textarea.select();
  document.execCommand("copy");
  document.body.removeChild(textarea);
  alert("URL이 복사되었습니다.");
}