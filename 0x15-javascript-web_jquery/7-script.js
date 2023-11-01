$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
  const res = JSON.parse(JSON.stringify(data));
  $('DIV#character').text(`${res.name}`);
});
