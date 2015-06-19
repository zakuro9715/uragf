<template>
  <nav class="navbar navbar-default">
    <div class="container">
      <div class="navbar-header">
        <a href="/" class="navbar-brand">対偶SNS</a>
      </div>
      <div class="collapse navbar-collapse">
        <ul class="nav navbar-nav">
          <li><a href="/rooms">部屋一覧</a></li>
        </ul>
      </div>
    </div>
  </nav>
  <div class="container">
    <router-view></router-view>
  </div>
</template>

<script>
module.exports = {
  data: {
    view: '',
    params: {
      roomId: '',
    },
  },
  components: {
    'home-view':      require('views/home.vue'),
    'room-view':      require('views/room.vue'),
    'room-list-view': require('views/room-list.vue'),
  },
}
</script>

<style>
html, body {
  font-size: 16px;
}
</style>
