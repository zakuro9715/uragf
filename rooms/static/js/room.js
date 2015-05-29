(function() {
  var request = window.superagent;

  var reportError = function(status, detail) { 
    alert("エラーだよ\nstatus=" + status + "\n" + detail);
  };

  var room = new Vue({
    el: '#room',
    data: {
      roomId: null,
      joining: true,
      posts: [],
      baseUrl: '/api/rooms/:id/'
    },
    methods: {
      load: function() {
        lastPost = this.posts[-1];
        $data = this.$data;
        url = this.baseUrl + 'posts/';
        if (lastPost) {
          url += '?from=' + lastPost.date_created;
        }

        request
          .get(url)
          .end(function(err, res) {
            if (err) {
              reportError(err.status, JSON.stringify(res.body, null, 2));
            }
            else {
              $data.posts = res.body.results.concat($data.posts);
            }
          });
      },
      join: function() {
        $data = this.$data;
        load = this.load
        url = this.baseUrl + 'joining/';
        request
          .put(url)
          .set('X-CSRFTOKEN', $.cookie('csrftoken'))
          .end(function(err, res) {
            if (err) {
              reportError(err.status, JSON.stringify(res.body, null, 2));
            }
            else {
              $data.joining = true;
              load();
            }
          });
      }
    },
    ready: function() {
      // /rooms/:id/
      this.roomId = window.location.pathname.split('/')[2];
      this.baseUrl = this.baseUrl.replace(':id', this.roomId);

      $data = this.$data;
      load = this.load;
      url = this.baseUrl + 'joining/';
      request
        .get(url)
        .end(function(err, res) { 
          if(err) {
            if (err.status == 403) {
              location.href = '/accounts/login/?next=' + location.pathname;
            } else if (err.status == 404) {
              $data.joining = false;
            }
          }
          else {
            load();
          }
        });
    },
  });
})();
