$('DIV#add_item').on('click', e => {
  const newItem = document.createElement('LI')
  newItem.innerText='Item'
  $('UL.my_list').append(newItem);
});
