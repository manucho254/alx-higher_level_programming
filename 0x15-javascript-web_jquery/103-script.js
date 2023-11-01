window.addEventListener('load', function () {
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      const lang = $('INPUT#language_code').val();
      $.get(
        `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
        function (data) {
          const res = JSON.parse(JSON.stringify(data));
          $('DIV#hello').text(`${res.hello}`);
        }
      );
    }
  });
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.get(
      `https://hellosalut.stefanbohacek.dev/?lang=${lang}`,
      function (data) {
        const res = JSON.parse(JSON.stringify(data));
        $('DIV#hello').text(`${res.hello}`);
      }
    );
  });
});
