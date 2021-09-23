const url = 'https://swapi-api.hbtn.io/api/films/?format=json'

$.get(url, (data, textStatus) => {

  ulContent = document.createDocumentFragment();
  data.results.forEach((movie) => {
    const listItem = document.createElement('LI');
    listItem.innerText = movie.title;
    elements.append(listItem);
  });
  $('UL#list_movies').append(elements);

})
