window.addEventListener('load', function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    console.log($('UL.my_list').last());
    $('UL.my_list li:last-child').remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
