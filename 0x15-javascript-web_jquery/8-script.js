$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
  const res = JSON.parse(JSON.stringify(data));

  for (const val of res.results) {
    $('UL#list_movies').append(`<li>${val.title}</li>`);
  }
});
