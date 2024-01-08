const sideNav = document.querySelector('.sidenav');
const windowWidth = document.querySelector('body').clientWidth;

if (sideNav) {
  sideNav.className = windowWidth > 750 ? 'sidenav' : 'sidenav-sm';
}

function loadScript(url, callback, callbackError) {
  const script = document.createElement('script');
  script.type = 'module';

  script.onload = callback;
  script.onerror = callbackError;

  script.src = url;
  document.querySelector('body').appendChild(script);
}

const containerId = document.querySelector('.container').id;

if (containerId === 'documentation') {
  loadScript('../static/mains/getDocumentationData.js');
} else if (containerId === 'quickfacks') {
  loadScript('../static/mains/getQuickFactData.js');
}
