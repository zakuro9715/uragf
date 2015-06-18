(function() {
  var request = require('superagent');
  var Vue     = require('vue');
  var errors  = require('utils/errors');


  var roomList = new Vue({
    el: '#room-list',
    data: {
      rooms: [],
      url: '/api/rooms/'
    },
    methods: {
      load: function() {
        $data = this.$data;

        request
          .get(this.url)
          .end(function(err, res) {
            if (err) {
              errors.report(err.status, JSON.stringify(res.body, null, 2));
            } else {
              $data.rooms = res.body.results;
            }
          });
      },
    },
    ready: function() {
      this.load();
    },
  });
})();
