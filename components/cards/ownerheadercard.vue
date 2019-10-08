<template>
  <div class="card">
    <img src="https://picsum.photos/id/1081/900/150" class="card-img img-fluid" alt="Steripower">
    <div class="card-img-overlay row ">
      
      <div class="col d-none d-xl-block">
        <h1 class="display-4">{{ownername}}</h1>
        <devicestatssmall :devicecount='8' :onlinecount='6' :offlinecount='2' :uses='234' :passersby='1066' :contractexpired='true'/>
      </div>

      <div class="col col d-block d-sm-none">
        <h4 >{{ownername}}</h4>
      </div>

    </div>
  </div>
</template>
<script>
 
import devicestatssmall from '@/components/widgets/devicestatssmall'
export default {
  props:['ownername'],
  components: {
    devicestatssmall
  }
}
</script>
