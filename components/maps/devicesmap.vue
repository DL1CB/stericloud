<template>
<div id="map-wrap" style="height: 100vh">
 <no-ssr>
   <l-map :zoom=13 :center="center">
     <l-tile-layer url="http://{s}.tile.osm.org/{z}/{x}/{y}.png"></l-tile-layer>
     <l-marker :lat-lng="center">
        <l-icon>
            <fa icon="tint" class="fa-2x" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
        </l-icon>
     </l-marker>
   </l-map>
 </no-ssr>
</div>
</template>
<script>

export default {
  data () {
    return {
      url: 'http://{s}.tile.osm.org/{z}/{x}/{y}.png',
      zoom: 13,
      center: [47.413220, -1.219482],
      fluid:17
    }
  }
}
</script>