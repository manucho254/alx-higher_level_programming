$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
  const res = JSON.parse(JSON.stringify(data));
  $('DIV#hello').text(`${res.hello}`);
});
