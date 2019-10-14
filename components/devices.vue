<template>
  <b-container fluid>
    <b-row>
      <b-col sm="6" md="6" lg="4" xl="3" class="p-0 pr-1 pb-1" v-for="device in owner.devices" v-bind:key="device.id">

        <nuxt-link :to='"/device/"+device.id' class="h6 text-dark text-capitalize" style="text-decoration:none">
          
          <b-card  class="mb-3 text-center shadow">
            <b-card-title class="text-reset lead">{{device.name}}</b-card-title>
            <b-card-body v-for="current in device.history" v-bind:key="current.id">

                <devicestatssmall class="text-muted justify-content-center" 
                    :devicecount='0'
                    :onlinecount='0'
                    :fluidlevel=current.fluidlevel
                    :uses='current.uses'
                    :passersby='current.passersby'
                    :batterylevel='current.batterylevel'
                    :charging='current.charging'
                    :servicein='device.servicein'
                    :contractexpired='device.contractexpired'
                    :maintain='current.maintain'
                    :signalstrength='current.signalstrength'
                />

                 <h6 class="text-center text-muted mt-2">
                    good for {{device.remainingtime || 5 }} days
                </h6>
            </b-card-body>
            
          </b-card>
        </nuxt-link>
      </b-col>
    </b-row>
  </b-container>
</template>



<script>

import animatednumber from 'animated-number-vue'
import devicestatssmall from '@/components/widgets/devicestatssmall'

export default {
  created: function(){
     this.$store.dispatch('owner/fetchowner', this.$route.params.id )
  },
  computed: {
    owner() {
      return this.$store.getters['owner/owner']
    }
  },

  components: {
    animatednumber,
    devicestatssmall
  }
}
</script>

