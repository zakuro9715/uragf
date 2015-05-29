(function() {
  var request = window.superagent;

  var reportError = function(status, detail) { 
    alert("エラーだよ\nstatus=" + status + "\n" + detail);
  };

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
              reportError(err.status, JSON.stringify(res.body, null, 2));
            }
            else {
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
