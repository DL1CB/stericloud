<template>
  <b-container >
    <h1 class="display-5">{{owner.name}}</h1>
    <devicestatssmall :devicecount='8' :onlinecount='6' :offlinecount='2' :uses='234' :passersby='1066' :contractexpired='true'/>
    <devices/>
  </b-container>
</template>

<script>

import devicestatssmall from '@/components/widgets/devicestatssmall'
import devices from '@/components/devices'

export default {
  created: function(){
     this.$store.dispatch('owner/fetchowner', this.$route.params.id )
  },
  computed: {
    owner() {
      return this.$store.getters['owner/owner']
    }
  },
  mounted: function(){
     //this.$store.dispatch('owner/fetchowner', this.$route.params.id )
  },
  components: {
    devicestatssmall,
    devices
  }
}
</script>

