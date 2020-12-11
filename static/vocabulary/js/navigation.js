const currentUrl = window.location.pathname;
  let activeNavId = 'home'

  switch (currentUrl) {
    case '/':
      activeNavId = 'home'
      break
    case '/profile':
      activeNavId = 'profile'
      break
    default:
      activeNavId = 'home'
      break
  };

  document.getElementById(activeNavId).classList.add('active');