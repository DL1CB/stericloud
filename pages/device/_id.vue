<template>
  
  <section v-if="item.name" class="container">

    <deviceheadercard 
      :devicename   ='item.name' 
      :indoorname   ='item.location.indoorname'
      :ownername    ='item.owner.name' 
      :owneraddress  ='owneraddress(item.owner.location)'
      :pointnorth   ='item.location.north'
      :pointeast    ='item.location.east'
    />

    <b-card-group class="mt-3" deck>
      <usescard :uses='item.current[0].uses'/>
      <passersbycard :passersby='item.current[0].passersby'/>
      <fluidcard :fluidlevel='item.current[0].fluidlevel'/>
      <hygeneindexcard :hygeneindex='100'/>
    </b-card-group>

    <usesmonthcard/>
    <fluidmonthcard/>

    <b-card-group class="mt-3" deck>
      <servicecard :servicein='30'/>
      <batterycard :batterylevel='item.current[0].batterylevel'/>
      <contractcard :remainingtime='14' :contractexpired="false"/>
    </b-card-group>

    <b-card-group class="mt-3" deck>
      <fluiddosagecard/>
      <ledcolorcard/>
    </b-card-group>
    

  </section>


</template>

<script>

import deviceheadercard from '@/components/cards/deviceheadercard'
import usescard from '@/components/cards/usescard'
import passersbycard from '@/components/cards/passersbycard'
import hygeneindexcard from '@/components/cards/hygeneindexcard'
import fluidcard from '@/components/cards/fluidcard'
import usesmonthcard from '@/components/cards/usesmonthcard'
import fluidmonthcard from '@/components/cards/fluidmonthcard'

import servicecard from '@/components/cards/servicecard'
import batterycard from '@/components/cards/batterycard'
import contractcard from '@/components/cards/contractcard'

import fluiddosagecard from '@/components/cards/fluiddosagecard'
import ledcolorcard from '@/components/cards/ledcolorcard'

import { mapGetters } from 'vuex'

export default {

 data() {
  return {
    id: this.$route.params.id,
    }
  },

  computed: {
    item() {
      return this.$store.getters['device/item']
    }
  },

  mounted: function(){
     this.$store.dispatch('device/fetch', this.id)
  },

  methods: {
    owneraddress(location) {
      return location.street +' '+
             location.number +', '+
             location.city +' '+
             location.country +' '+
             location.postalcode 
    }
  },
  
  components: {
    deviceheadercard,
    usescard,
    passersbycard,
    hygeneindexcard,
    fluidcard,
    usesmonthcard,
    fluidmonthcard,
    servicecard,
    batterycard,
    contractcard,
    fluiddosagecard,
    ledcolorcard
  }
}
</script>

