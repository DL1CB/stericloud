<template>
    <b-card
        title="Integrated light"
        sub-title="set the color and luminosity of the integrated light"
        class="shadow p-1 mb-5 bg-white rounded">

     
            <div class="d-inline-flex " >
                <div>
                    <div class="h5 p-3 text-center">
                    color
                    </div>
                    <color-picker 
                        v-bind="color" 
                        @input="onColor" 
                    />
                    <div class="h5 p-3 text-center">
                        <b-button-group >
                            <b-button variant="primary" :pressed.sync='buttons.on' @click="buttonOn">on</b-button>
                            <b-button variant="primary" :pressed.sync='buttons.off' @click="buttonOff">off</b-button>
                        </b-button-group>
                    </div>

                </div>
                <div class="pl-5">
                    <div class="h5 p-3">
                    luminosity
                    </div>
                    <vue-slider 
                        v-model="color.luminosity"
                        :adsorb="true"
                        :interval="10"
                        :marks="true"
                        direction="btt"
                        :height="250"
                        :dotStyle ="{ backgroundColor: 'rgba(0, 231, 255, 1)' }" 
                        @change="onIntensity"
                   
                    />
                 </div>
                     
            </div>


  
  
    
    </b-card>
</template>

<script>

import ColorPicker from '@radial-color-picker/vue-color-picker';

// import slider
import VueSlider from 'vue-slider-component/dist-css/vue-slider-component.umd.min.js'
import 'vue-slider-component/dist-css/vue-slider-component.css'
import 'vue-slider-component/theme/default.css'

export default {
    components: {
        ColorPicker,
        VueSlider
    },
    data() {
      return {
            color: {
            hue: 50,
            saturation: 100,
            luminosity: 50,
            alpha: 1,
          },
  
          buttons:{
              on: true,
              off: false
          }
      };
    },
    methods: {
        onColor(hue) {
            this.color.hue = hue;
        },
        onIntensity(luminosity) {
            this.color.luminosity = luminosity;
        },
        buttonOn(button) {
            this.buttons.on = true
            this.buttons.off = false
            this.color.luminosity = 50
        },

        buttonOff(button) {
            this.buttons.on = false
            this.buttons.off = true
            this.color.luminosity = 0
        },
    },
};
</script>