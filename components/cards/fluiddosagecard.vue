<template>
    <b-card
    title="Fluid dosage"
    sub-title="set the fluid dosage volume"
    class="shadow p-1 mb-5 bg-white rounded"
    >
    <div class="row p-3" >
      <div class="col col-4 p-3">
        <vue-slider
        v-model="value"
        :adsorb="true"
        :interval="10"
        :marks="true"
        direction="btt"
        :height="250"
        :dotStyle ="{ backgroundColor: 'rgba(0, 231, 255, 1)' }"
        />
      </div>
      <div class="col col-8  border border-secondary rounded-circle row align-items-center p-3" style="font-size: 20px;">
         <fa v-if="value" icon="tint" class="col" :size='iconsize' :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
      </div>
    </div>

     <button type="button" class="container-fluid mt-4 btn btn-outline-primary btn-sm">Dispense fluid</button>
     
    </b-card>
</template>

<script>

// import component
import VueSlider from 'vue-slider-component/dist-css/vue-slider-component.umd.min.js'
import 'vue-slider-component/dist-css/vue-slider-component.css'
import 'vue-slider-component/theme/default.css'

export default {
  components: {
    VueSlider
  },
  data: function () {
    return {
      value: 20
     
      
    }
  },
  computed: {
    iconsize: function(){
      const size = Math.trunc(this.value / 10)
      return ""+size.toString()+"x" 
    }
  }
}
</script>
<style>
 input.vue-slider-sr-only  {
   background-color: rgba(0, 231, 255, 1)
 }
</style>
