<template>
  <div v-if="joining">
    <post-form roomid="[[route.params.id]]" on-posted="[[onPosted]]"></post-form>
    <div class="timeline">
      <post v-repeat="posts"></post>
    </div>
  </div>
  <join-button v-if="!joining" roomid="[[route.params.id]]" on-joined="[[onJoined]]"></join-button>
</template>

<script>
var $       = require('jquery');
var errors  = require('utils/errors');
var login   = require('utils/login')
var request = require('superagent');

module.exports = {
  components: {
    'post':        require('components/post.vue'),
    'post-form':   require('components/post-form.vue'),
    'join-button': require('components/join-button.vue'),
  },
  props: ['params'],
  data: function() {
    return {
      joining: true,
      posts: [],
    }
  },
  methods: {
    load: function() {
      lastPost = this.posts[-1];
      $data = this.$data;
      url = '/api' + this.route.path + '/posts/';
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
    $data = this.$data;
    load = this.load;
    url = '/api' + this.route.path + '/joining/';
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
};
</script>

<style>
.timeline {
  box-shadow: 2px 2px 1px #aaa;
  background-color: white;
  border-radius: 3px;
  border: solid 1px #e0e0e0;
}
</style>
