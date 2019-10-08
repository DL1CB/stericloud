<template>
  <section class="container">
    <div class="content-fluid">
      <appheader appname="SteriCloud"/>
    </div>
    <b-card-group columns >
      <nuxt-link :to='"/owner/"+owner.id' v-for="owner in owners" v-bind:key="owner.id"  >
        <ownercard class="mt-2" :ownername="owner.name"/>
      </nuxt-link>
    </b-card-group>
   </section>
</template>

<script>


import appheader from '@/components/cards/appheader'
import ownercard from '@/components/cards/ownercard'


export default {
  computed: {
    owners() {
      return this.$store.getters['owners']
    }
  },

  mounted: function(){
     this.$store.dispatch('fetchowners')
  },
  components: {
    appheader,
    ownercard
  }
}
</script>

