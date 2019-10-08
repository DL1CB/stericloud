<template>
   <div class="container"> 
  

  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    
      
      <router-link tag="div" class="navbar-brand" to="/" exact>
        <fa v-if="isNothome" class="d-inline ml-2" icon="home" />
      </router-link>

      <div class="collapse navbar-collapse justify-content-end">
        <ul class="navbar-nav">
          <li v-if="username">
            <a href="#" class="nav-link">
              Hello {{ username }}
            </a>
          </li>
          <li v-if="username">
            <a href="#" class="nav-link" @click="logout">
              Logout
            </a>
          </li>
          <li v-if="!username">
            <router-link v-if="!username" tag="a" class="nav-link" to="/signin" exact>
              Signin
            </router-link>
          </li>
          <li v-if="!username">
            <router-link v-if="!username" tag="a" class="nav-link" to="/signup" exact>
              Signup
            </router-link>
          </li>
        </ul>
      </div>
   
  </nav>

 </div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  computed: {
    username() {
      return this.$store.getters['auth/username']
    },
    isNothome(){
      return !(this.$route.path == "/")
    }
  },
  methods: {
    ...mapMutations({
      logout: 'auth/logout'
    })
  }
}
</script>