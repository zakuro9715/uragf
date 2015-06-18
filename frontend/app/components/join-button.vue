<template>
  <button v-on="click: join" class="btn btn-primary">このルームに参加する</button>
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
      name: 'on-joined',
      type: Function,
    },
  ],
  computed: {
    url: function() {
      return '/api/rooms/:id/joining/'.replace(':id', this.roomid);
    },
  },
  methods: {
    join: function() {
      onJoined = this.onJoined;
      request
        .put(this.url)
        .set('X-CSRFTOKEN', $.cookie('csrftoken'))
        .end(function(err, res) {
          if (err) {
            errors.report(err.status, JSON.stringify(res.body, null, 2));
          } else {
            onJoined();
          }
        });
    },
  },
};
</script>
