<template>
    <div class="card shadow p-3 mb-3 bg-white">

        <div >
            <h5 class="text-center text-dark text-capitalize" v-b-tooltip.hover.top title="Humbold Strasse 14, Erlangen, Germany 91052, Room 3-69">
                {{ownername}} 
            </h5>
        </div>

        <devicestatssmall class="text-muted justify-content-center"  :devicecount='8' :onlinecount='6' :offlinecount='2' :uses='234' :passersby='1066'/>
  
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
