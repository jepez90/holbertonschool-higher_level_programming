function fetchHello() {
  const url = 'https://www.fourtonfish.com/hellosalut/';
  const languageCode = $('INPUT#language_code').val();
  const params = {
    lang: languageCode
  }

  $.get(url, params, data => {
    $('DIV#hello').text(data.hello);
  });

}

function detectEnter(event){
  if(event.which == '13'){
    fetchHello();
  }

}

$().ready(a => {
  $('INPUT#btn_translate').on('click', fetchHello);
  $('INPUT#language_code').keydown(detectEnter);
});
