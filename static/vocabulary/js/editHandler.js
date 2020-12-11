function clickHandler(e) {
  const elementId = e.target.id
  const elParent = document.getElementById(elementId).parentElement;
  elParent.nextElementSibling.style.display = 'flex';
  elParent.classList.add('hide');
};
