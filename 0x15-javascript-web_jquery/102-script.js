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


$().ready(a => {
  $('INPUT#btn_translate').on('click', fetchHello);
});
