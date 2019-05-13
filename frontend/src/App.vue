<template>
  <div id="app">
    <navbar></navbar>
    <div class="container">
      <div class="columns">
        <div class="column col-10 p-centered">
          <primarylist v-bind:url="this.server_url"></primarylist>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import navbar from './components/navbar.vue'
import primarylist from './components/primary_list.vue'

export default {
  name: 'app',
  components: {
    navbar,
    primarylist
  },
  data: function() {
    return {
      server_url: 'http://localhost:8000/todos/'
    }
  }
}
</script>

<style>
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
