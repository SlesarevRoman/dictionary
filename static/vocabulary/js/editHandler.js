function editHandler(e) {
  const cardId = e.target.parentElement.parentElement.id;
  const cardEl = document.getElementById(cardId);
  cardEl.nextElementSibling.style.display = 'flex';
  cardEl.classList.add('hide');
};

function editHandlerMobile(e) {
  const cardId = e.target.parentElement.id;
  const el = document.getElementById(cardId);
  const buttonBlock = el.getElementsByClassName('word-item__button-wrapper')[0];
  buttonBlock.style.display = buttonBlock.style.display == 'flex' ? 'none' : 'flex';
}
