<template>
  <div id="coming">
    <h2>Coming soon...</h2>
    <img src="res/raw-270x270.png">
    <h1>Studmane Blag!</h1>
    <h6>Powered by vuex</h6>
    
  </div>
</template>

<script>
export default {
  name: 'coming',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<style scoped>
#coming {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
