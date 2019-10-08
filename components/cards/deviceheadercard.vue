<template>

  <b-card
    overlay
    img-src="https://picsum.photos/id/347/900/150"
    class="overflow-hidden"
  >
    <b-row no-gutters>
      <b-col md="6">
         <b-card-body :title="nameandlocation">
          {{ownername}} | {{owneraddress}}
        </b-card-body>
        <devicestatssmall :signalstrength='signalstrength'/>
      </b-col>

      <b-col  md="6">
      <no-ssr>
        <l-map  style="height: 100%; width: 100%" :zoom=17 :center="[pointnorth, pointeast]">
          <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
          <l-marker :lat-lng="[pointnorth, pointeast]"></l-marker>
        </l-map>
      </no-ssr>
      </b-col>
    </b-row>
  </b-card>
</template>
<script>
import devicestatssmall from '@/components/widgets/devicestatssmall'
export default {
  props: ['devicename','indoorname','ownername','owneraddress','pointnorth','pointeast','signalstrength'],

  computed:{
    nameandlocation(){
      return this.devicename +' | '+this.indoorname
    }
  },

  components: {
    devicestatssmall
  }
}
</script>
