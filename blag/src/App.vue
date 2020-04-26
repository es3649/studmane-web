<template>
  <div id="app">
    <link href='https://fonts.googleapis.com/css?family=Signika' rel='stylesheet'>
    <link href='https://fonts.googleapis.com/css?family=Gayathri' rel='stylesheet'>
    <link rel="stylesheet" type="text/css" href="/css/blag.css"/>
    <link rel="stylesheet" type="text/css" href="/css/bootstrap.css"/>
    <nav class="navbar navbar-expand-lg navbar-light" style="background-color: #dadaec;">

      <a class="navbar-brand" href="/">
        <img src="/res/raw-270x270.png" width="30" height="30" alt="">
        Studmane Blag
      </a>

      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <router-link class="nav-link" to="/blag">Home</router-link>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">&lt; Prev</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Next &gt;</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Topics
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item disabled" href="#">Nothing here yet!</a>
              <!--<div class="dropdown-divider"></div>-->
            </div>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              Favorites
            </a>
            <div class="dropdown-menu" aria-labelledby="navbarDropdown">
              <a class="dropdown-item disabled" href="#">Nothing here yet!</a>
              <!--options-->
              <router-link class="nav-link" to="/cougarslament">Cougars Lament</router-link>
            </div>
          </li>
        </ul>
      </div>
    </nav>
    <div id="content">
      <router-view/>
      <div class="footer">
        <p class="center-text">Created by Eric Steadman on August 27, 2019</p>
      </div>
    </div>
  </div>
</template>

<script>
require("bootstrap")

export default {
  name: 'app',
}
</script>

<style scoped>
.center-text {
  text-align: center;
}

#content {
  min-height: 100vh;
  padding-bottom: 6rem;
  position: relative;
}

.footer {
  height: 6rem;
  padding: 1rem;
  width: 100%;
  color: #F0F0F8;
  background-color: #444458;
  position: absolute;
  bottom: 0;
}

</style>