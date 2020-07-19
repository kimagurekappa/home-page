<template>
  <div id="app">
    <h1>{{ msg }}</h1>
    <h3>Git Hub へのアクセス</h3>
    <ul>
      <li><a href="https://github.com/kimagurekappa" target="_blank" rel="noopener">Git Hub</a></li>
    </ul>
    <h3>You Tube へのアクセス</h3>
    <ul>
      <li><a href="https://www.youtube.com/channel/UC3M75vH5Y0kizWKaT2BnNyQ?view_as=subscriber" target="_blank" rel="noopener">You Tube</a></li>
    </ul>

      <el-menu :default-active="activeIndex" mode="horizontal" router>
      <el-menu-item index="home" :route="{ name:'home' , path: '/home-page/' }">Home</el-menu-item>
      <el-menu-item index=about :route="{ name:'about' , path: '/home-page/' }">About</el-menu-item>
    </el-menu>
    <router-view />

  </div>
</template>

<script>


export default {
  data () {
    return {
      msg: 'きまぐれかっぱ',
      name: 'app',
      activeIndex: '',
    }
  },
  mounted() {
      // 読み込まれたページをアクティブ
      this.activeIndex = this.$route.name;
  }
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: left;
  color: #2c3e50;
  margin-top: 60px;
}
</style>