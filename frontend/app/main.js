require('bootstrap.js')
require('bootstrap.css')

var Vue    = require('vue')
var Router = require('vue-router')

Vue.config.delimiters = ['[', ']'];
Vue.use(Router);

var app = Vue.extend(require('./app.vue'))

var router = new Router({
  history: true,
})

router.map({
  '/': {
    component: 'home-view',
  },
  '/rooms/:id/': {
    component: 'room-view',
  },
});

router.start(app, '#app');

