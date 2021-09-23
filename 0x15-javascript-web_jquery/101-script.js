function addListItem() {
  const newListItem = document.createElement('LI');
  newListItem.innerText = 'Item';
  $('ul.my_list').append(newListItem);
}

function removeLastListItem() {
  $('ul.my_list > li').last().remove();
}

function removeAllListItem() {
  $('ul.my_list').html('');
}

$().ready(a => {
  $('#add_item').on('click', addListItem);
  $('#remove_item').on('click', removeLastListItem);
  $('#clear_list').on('click', removeAllListItem);
});
