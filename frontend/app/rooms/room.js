(function() {
  require('./timeline.less')

  var $ = require('jquery');
  var login = require('utils/login')
  var cookie = require('jquery-cookie');
  var request = require('superagent');

  var reportError = function(status, detail) {
    alert("エラーだよ\nstatus=" + status + "\n" + detail);
  };

  var room = new Vue({
    el: '#room',
    data: {
      roomId: null,
      joining: true,
      posts: [],
      postText: null,
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
      },
      post: function() {
        $data = this.$data;
        load = this.load
        url = this.baseUrl + 'posts/';
        console.log(this.postText);
        request
          .post(url)
          .send({text: this.postText})
          .set('X-CSRFTOKEN', $.cookie('csrftoken'))
          .end(function(err, res) {
            if (err) {
              reportError(err.status, JSON.stringify(res.body, null, 2));
            }
            else {
              load();
              $data.postText = '';
            }
          });
      },
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
              login();
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
