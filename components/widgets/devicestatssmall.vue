<template>
     <div class="d-flex">

        <div v-if="devicecount" class="p-2 text-center" v-b-tooltip.hover.bottom title="devices">
            <fa-layers>
              <fa icon="tablet" />
              <fa icon="tablet" transform="shrink-6 down-2" :style="{ color: 'white' }" />
              <fa icon="tint" transform="shrink-8  down-1" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
            </fa-layers>
            <div class="d-block">
               <animatednumber  :value='devicecount' :duration='500'  round='1'/>
            </div>
        </div>    

        <div v-if="onlinecount" class="p-2 text-center" v-b-tooltip.hover.bottom :title="onlinecount+' devices online'">
            <fa icon="wifi"  :style="{ color: 'rgba(0, 231, 255, 1)' }" />
            <animatednumber class="d-block" :value='onlinecount' :duration='500'  round='1'/>  
        </div>

        <div v-if="offlinecount" class="p-2 text-center text-danger" v-b-tooltip.hover.bottom :title="offlinecount+' devices offline'">
            <fa icon="wifi"/>
            <animatednumber class="d-block" :value='offlinecount' :duration='500'  round='1'/>  
        </div>

        <div v-if="fluidlevel >= 0" class="p-2 text-center" v-b-tooltip.hover.bottom :title="fluidlevel+'% fluid level'">
            <fa icon="tint" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
            <animatednumber class="d-block"  :value='fluidlevel' :duration='500'  round='1'/>
        </div>

        <div v-if="uses" class="p-2 text-center" v-b-tooltip.hover.bottom :title="uses+' uses'">
            <fa-layers>
               <fa icon="tint" transform="shrink-6 right-2 up-4" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
               <fa icon="hands" />
            </fa-layers>
            <animatednumber class="d-block" :value='uses' :duration='500'  round='1'/>
        </div>

        <div v-if="passersby" class="p-2 text-center" v-b-tooltip.hover.bottom :title="passersby+' passers by'">
            <fa icon="walking" />
            <animatednumber class="d-block" :value='passersby' :duration='500'  round='1'/>
        </div>

        <div v-if="batterylevel >= 0" class="p-2 text-center" v-b-tooltip.hover.bottom :title="'battery level ' +batterylevel +'%'+ chargingtext">
             <fa-layers v-if="charging">
                <fa icon="car-battery" transform="left-8"  /> 
                <fa icon="plug" transform="right-8"/>
            </fa-layers>
            <fa-layers v-else>
                <fa icon="car-battery"  /> 
            </fa-layers>

            <div class="d-block">
               <animatednumber  :value='batterylevel' :duration='500'  round='1'/>% 
            </div>
        </div>  

        <div v-if="servicein >= 0" class="p-2 text-center" v-b-tooltip.hover.bottom :title="servicein + ' days to service'">
            <fa icon="tools" />
            <animatednumber class="d-block" :value='servicein' :duration='500'  round='1'/>  
        </div>

        <div v-if="contractexpired" class="p-2 text-center text-danger" v-b-tooltip.hover.bottom title="contract expired">
            <fa icon="file-signature" />
        </div>

        <div v-if="maintain" class="p-2 text-center text-warning" v-b-tooltip.hover.bottom title="maintenance required">
            <fa icon="tools"/>
        </div>

        <div v-if="signalstrength >= 0">
          <div v-if="signalstrength" class="p-2 text-center" v-b-tooltip.hover.bottom :title="signalstrength+ '% signal strength'">
              <fa icon="wifi" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
              <animatednumber class="d-block" :value='signalstrength' :duration='500'  round='1'/>
          </div>
          <div v-else class="p-2 text-center text-danger" v-b-tooltip.hover.bottom title="offline">
              <fa icon="wifi"/>
          </div>
        </div>

    </div>
</template>
<script>
import animatednumber from 'animated-number-vue'
export default {
  props: {

    devicecount: {
      type: Number,
      default: 0
    },
    onlinecount: {
      type: Number,
      default: 0
    },
    offlinecount: {
      type: Number,
      default: 0
    },
    fluidlevel: {
      type: Number,
      default: -1
    },
    uses: {
      type: Number,
      default: 0
    },
    passersby: {
      type: Number,
      default: 0
    },
    batterylevel: {
      type: Number,
      default: -1
    },
    charging: {
      type: Boolean,
      default: false
    },
    servicein: {
      type: Number,
      default: -1
    },
    contractexpired: {
      type: Boolean,
      default: false
    },
    maintain: {
      type: Boolean,
      default: false
    },
    signalstrength: {
      type: Number,
      default: -1
    },
    
  },
  computed: {
     chargingtext: function(){
         if (this.charging){ return ', charging' } else { return ''}
     }  
  },  
  components: {
    animatednumber
  }
}
</script>