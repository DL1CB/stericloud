<template>
  <section class="container">

    <div class="content-fluid">
      <ownerheadercard :ownername='owner.name'/>
    </div>
 
      <b-card-group class="mt-3" deck >
        <nuxt-link tag="div" :to='"/device/"+device.id' v-for="device in owner.devices" v-bind:key="device.id"  >
          <devicecard class="h-100" :device='device'/>
        </nuxt-link>
      </b-card-group>
   
   </section>
</template>

<script>

import ownerheadercard from '@/components/cards/ownerheadercard'
import devicecard from '@/components/cards/devicecard'

export default {
  computed: {
    owner() {
      return this.$store.getters['owner/owner']
    }
  },
  mounted: function(){
     this.$store.dispatch('owner/fetchowner', this.$route.params.id )
  },
  components: {
    ownerheadercard,
    devicecard
  }
}
</script>

