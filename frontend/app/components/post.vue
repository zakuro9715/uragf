<template>
  <div class="post">
    <div class="post__header">
        <span class="post__username">[[ user.username ]]</span>
        <span class="post__date">at [[ date_created]]</span>
      </div>
      <div class="post__body">[[ text]]</div>
    </div>
  </div>
</template>

<script>
module.exports = {
  props: ['post'],
  replace: true,
}
</script>

<style>
.post {
  padding: 16px;
  border-bottom: solid 1px #e0e0e0;
  word-wrap: break-word;
}

.post .post__header {
  font-size: 0.8rem;
}

.post .post__username {
  font-weight: bold;
}

.post .post__date {
  color: #aaa;
}

.post .post__body {
  padding-top: 8px;
}
</style>
