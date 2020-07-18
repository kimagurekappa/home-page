<template>
  <div id="app">
  <tab-menu></tab-menu>
    <div class="hello">
    <h1>{{ msg }}</h1>
    <h3>Git Hub へのアクセス</h3>
    <ul>
      <li><a href="https://github.com/kimagurekappa" target="_blank" rel="noopener">Git Hub</a></li>
    </ul>
    <h3>You Tube へのアクセス</h3>
    <ul>
      <li><a href="https://www.youtube.com/channel/UC3M75vH5Y0kizWKaT2BnNyQ?view_as=subscriber" target="_blank" rel="noopener">You Tube</a></li>

    </ul>
  </div>
  </div>
</template>

<script>
import TabMenu from '@/components/TabMenu'

export default {
  data () {
    return {
      msg: 'Welcome to home page for KimagureKappa!'
    }
  },
  name: 'App',
  components: {
    TabMenu
  }
}

</script>
