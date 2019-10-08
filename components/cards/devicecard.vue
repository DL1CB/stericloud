<template>
    <div class="card shadow p-3 mb-3 bg-white">

        <div >
            <h3 class="text-center text-dark text-capitalize" v-b-tooltip.hover.top title="Humbold Strasse 14, Erlangen, Germany 91052, Room 3-69">
                {{device.name}} 
            </h3>
        </div>

        <div >
            <h4 class="text-center mt-3">Fluid
                <fa icon="tint" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
                <animatednumber :value='current.fluidlevel' :duration='500'  round='1'/>%
            </h4>
        </div>
        
        <div class="row">
            <h6 class="text-center text-muted col">
            good for {{device.remainingtime}} days
            </h6>
        </div>

        <devicestatssmall class="text-muted justify-content-center" 
            :devicecount='0'
            :onlinecount='0'
            :uses='current.uses'
            :passersby='current.passersby'
            :batterylevel='current.batterylevel'
            :charging='current.charging'
            :servicein='device.servicein'
            :contractexpired='device.contractexpired'
            :maintain='current.maintain'
            :signalstrength='current.signalstrength'
        />
     
    </div>
</template>
<script>
import animatednumber from 'animated-number-vue'
import devicestatssmall from '@/components/widgets/devicestatssmall'
export default {

  props:['device'],

  computed:{
      current(){
          return this.device.history[0] || {}
      }
  },

  components: {
    animatednumber,
    devicestatssmall
  }
}
</script>

