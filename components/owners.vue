<template>
  <b-container fluid>
    <b-row>
      <b-col  sm="6" md="6" lg="4" xl="3" class="p-0 pr-1 pb-1" v-for="owner in owners" v-bind:key="owner.id">
        <nuxt-link :to='"/owner/"+owner.id' class="h6 text-dark text-capitalize" style="text-decoration:none">
          <b-card  class="h-100 mb-3 text-center shadow">
            <b-card-title class="text-reset lead">{{owner.name}}</b-card-title>
            <devicestatssmall class="text-reset text-muted justify-content-center"  :devicecount='8' :onlinecount='6' :offlinecount='2' :uses='234' :passersby='1066'/>
          </b-card>
        </nuxt-link>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>


import devicestatssmall from '@/components/widgets/devicestatssmall'
export default {
  created: function(){
     this.$store.dispatch('fetchowners')
  },
  computed: {
    owners() {
      return this.$store.getters['owners']
    }
  },
  components: {
    devicestatssmall
  }
}
</script>