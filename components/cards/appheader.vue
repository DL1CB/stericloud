<template>
  <div class="card">
  <img src="~/assets/stericloudjumbo.png" class=" card-img img-fluid" alt="SteriCloud">
  <div class="card-img-overlay row">
    <div class="col d-none d-xl-block"> 
      <h1 class="display-3">{{appname}}</h1>
      <h5 class="display-4">smart hygene</h5>
      <devicestatssmall :devicecount='8' :onlinecount='6' :offlinecount='2' :uses='234' :passersby='1066'/>
    </div>

    <div class="col d-block d-sm-none"> 
      <h4>{{appname}}</h4>
      <devicestatssmall :devicecount='8' :onlinecount='6' :offlinecount='2' :uses='234' :passersby='1066'/>
    </div>
  </div>
  </div>
</template>
<script>
 
import devicestatssmall from '@/components/widgets/devicestatssmall'
export default {
  props:['appname'],
  components: {
    devicestatssmall
  }
}
</script>
