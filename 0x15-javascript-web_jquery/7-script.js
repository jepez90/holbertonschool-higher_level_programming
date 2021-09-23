const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'
$.get(url, (data, textStatus) => {
  if (textStatus !== 'success') {
    console.log('error: ', textStatus)
  } else {
    $('DIV#character').html(data.name);
  }
})
