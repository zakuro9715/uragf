<template>
  <div class="form-group">
    <textarea v-model="postText" class="form-control"></textarea>
    <button v-on="click: post" class="btn btn-primary form-control">投稿</button>
  </div>
</template>

<script>
var errors  = require('utils/errors');
var cookie  = require('jquery-cookie');
var request = require('superagent');

module.exports = {
  props: [
    {
      name: 'roomid',
      type: String,
      required: true,
    },
    {
      name: 'on-posted',
      type: Function,
    },
  ],
  data: {
    postText: '',
  },
  computed: {
    url: function() {
      return '/api/rooms/:id/posts/'.replace(':id', this.roomid);
    },
  },
  methods: {
    finishPost: function(post) {
      this.postText = '';
      if(this.onPosted) {
        this.onPosted(post);
      }
    },
    post: function() {
      var finishPost = this.finishPost;
      request
        .post(this.url)
        .send({text: this.postText})
        .set('X-CSRFTOKEN', $.cookie('csrftoken'))
        .end(function(err, res) {
          if (err) {
            errors.report(err.status, JSON.stringify(res.body, null, 2));
          } else {
            finishPost(res);
          }
        });
    },
  },
};
</script>
