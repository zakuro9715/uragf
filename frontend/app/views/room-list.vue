<template>
  <h1>部屋一覧</h1>

  <div>
    <ul>
      <li v-repeat="room: rooms">
        <a href="/rooms/[[ room.slug ]]/">[[ room.name ]]</a>
      </li>
    </ul>
  </div>
</template>

<script>
var request = require('superagent');
var errors  = require('utils/errors');

module.exports = {
  props: ['params'],
  data: function() {
    return {
      rooms: [],
      url: '/api/rooms/',
    };
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
};
</script>
