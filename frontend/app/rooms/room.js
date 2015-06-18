(function() {
  require('./timeline.less');

  var $       = require('jquery');
  var errors  = require('utils/errors');
  var login   = require('utils/login')
  var cookie  = require('jquery-cookie');
  var request = require('superagent');
  var Vue     = require('vue');

  var room = new Vue({
    el: '#room',
    components: {
      'post':        require('components/post.vue'),
      'post-form':   require('components/post-form.vue'),
      'join-button': require('components/join-button.vue'),
    },
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
              errors.report(err.status, JSON.stringify(res.body, null, 2));
            } else {
              $data.posts = res.body.results.concat($data.posts);
            }
          });
      },
      onJoined: function() {
        this.joining = true;
        this.load();
      },
      onPosted: function() {
        this.load();
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
              login();
            } else if (err.status == 404) {
              $data.joining = false;
            }
          } else {
            load();
          }
        });
    },
  });
})();
