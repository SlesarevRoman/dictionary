const currentUrl = window.location.pathname;
  let activeNavId = 'home'

  switch (currentUrl) {
    case '/':
      activeNavId = 'home'
      break
    case '/memorization':
      activeNavId = 'memorization'
      break
    default:
      activeNavId = 'home'
      break
  };

document.getElementById(activeNavId).classList.add('active');

function menuToggle() {
  const elementId = 'navbarText';
  document.getElementById(elementId).classList.toggle('show');
};
