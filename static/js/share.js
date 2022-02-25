const url = 'https://peanut-personalcolor.herokuapp.com/';

function shareKakao() {
  var shareImage = 'https://ifh.cc/g/0Jt2XM.png';
  const shareTitle = '퍼스널컬러';
  const shareDes = '퍼스널컬러 진단 서비스 Peanut';

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
    var sendText = "#퍼스널컬러 #테스트 #peanut"; // 전달할 텍스트
    var sendUrl = "https://peanut-personalcolor.herokuapp.com/"; // 전달할 URL
    window.open("https://twitter.com/intent/tweet?text=" + sendText + "&url=" + sendUrl);
}

function shareURL() {
  var url = 'https://peanut-personalcolor.herokuapp.com/';
  var textarea = document.createElement("textarea");
  document.body.appendChild(textarea);
  textarea.value = url;
  textarea.select();
  document.execCommand("copy");
  document.body.removeChild(textarea);
  alert("URL이 복사되었습니다.");
}