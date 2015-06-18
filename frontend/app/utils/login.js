module.exports = function() {
  location.href = '/accounts/login/?next=' + location.pathname;
}
