const url = 'https://fourtonfish.com/hellosalut/?lang=fr'

$(
  $.get(url, (data, textStatus) => {
    $('DIV#hello').text(data.hello);
  })
);
