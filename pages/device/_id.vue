<template>
  <div>
  <b-container fluid>
    <b-row class="p-0 " >
      <b-col >
        <b-card> <!-- overlay img-src="https://picsum.photos/1024/480/?image=1001&blur=5"-->
          <b-card-body>

          <b-row class="p-0">
            <b-col lg="3" md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Fluid</h3>
                 <br/>
                <h2 class="text-center">
                  <fa icon="tint" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
                  <animatednumber class="h2" :value='current.uses' :duration='500' :delay='100' round='1'/>%
                </h2>
              </div>
            </b-col>

            <b-col lg="3" md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Uses</h3>
                 <br/>
                <h2 class="text-center">
                  <fa-layers class="mr-2">
                    <fa icon="tint" transform="shrink-6 right-2 up-4" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
                    <fa icon="hands" />
                  </fa-layers>
                  <animatednumber class="h2" :value='current.uses' :duration='500' :delay='100' round='1'/>
                </h2>
                <div class="text-center">627 <fa icon="award" /></div>
              </div>
            </b-col>

            <b-col lg="3" md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Passers by</h3>
                 <br/>
                <h2 class="text-center">
                  <fa class="d-inline" icon="walking" />
                  <animatednumber class="h2" :value='current.passersby' :duration='500' :delay='100' round='1'/>
                </h2>
                <div class="text-center">627 <fa icon="award" /></div>
              </div>
            </b-col>

            <b-col lg="3" md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Hygene Index</h3>
                 <br/>
                <h2 class="text-center">
                  <animatednumber class="h2" :value='current.batterylevel' :duration='500' :delay='100' round='1'/>%
                </h2>
                <fa v-if="hygeneindextrend > 0" class="d-inline" icon="chevron-up"/>
                <fa v-if="hygeneindextrend < 0" class="d-inline" icon="chevron-down"/>
                <p class="text-center">{{hygeneindexgoal || 0}}%<fa class="d-inline ml-1 mr-2" icon="carrot" /> | <fa class="d-inline ml-2 mr-1" icon="award" />{{hygeneindexrecord || 0}}%</p>
              </div>
            </b-col>  

            <b-col lg="3" md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Battery</h3>
                 <br/>
                <h2 class="text-center">
                  <fa icon="car-battery"  /> 
                  <animatednumber class="h2" :value='current.batterylevel' :duration='500' :delay='100' round='1'/>%
                </h2>
              </div>
            </b-col>      

            <b-col lg="3" md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Signal</h3>
                 <br/>
                <h2 class="text-center">
                  <fa icon="wifi" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
                  <animatednumber class="h2" :value='current.signalstrength' :duration='500' :delay='100' round='1'/>%
                </h2>
              </div>
            </b-col>   

            <b-col lg="3" md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Dosage</h3>
                 <br/>
                <h2 class="text-center">
                  <fa icon="tint" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
                  <animatednumber class="h2" :value='dosage' :duration='500' :delay='100' round='1'/>%
                </h2>
                 <br/>
                <vue-slider
                  v-model="dosage"
                  :adsorb="true"
                  :interval="10"
                  :marks="true"
                  :dotStyle ="{ backgroundColor: 'rgba(0, 231, 255, 1)' }"
                  tooltip="none"
                  direction="ltr"
                  />
              </div>
            </b-col>  

            <b-col lg="3" md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Light</h3>
                <br/>
                <Swatches inline v-model="color" :colors="colors" background-color="transparent"/>
              </div>
            </b-col> 
          
           <b-col lg="3" md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Uses</h3>
                 <br/>
                 <usesmonthchart class="mh-10"/>
              </div>
            </b-col> 

            <b-col lg="3" md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Fluid</h3>
                <br/>
                <fluidmonthchart class="mh-10"/>
              </div>
            </b-col>

            <b-col lg="3" md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Contract</h3>
                 <br/>
                <h2 class="text-center">expires in <animatednumber class="h2" :value='current.servicein' :duration='500' :delay='100' round='1'/> days</h2>
              </div>
            </b-col> 

            <b-col lg="3" md="4" sm="6" xs="12" class="align-items-center">
              <div class="my-2 h-100 p-4 text-center shadow" style="background-color: rgba(255, 255, 255, 0.2)">
                <h3>Maintenance</h3>
                <br/>
                <h2 class="text-center">service in <animatednumber class="h2" :value='current.servicein' :duration='500' :delay='100' round='1'/> days</h2>
              </div>
            </b-col>
          </b-row>

          </b-card-body>
        </b-card>
      </b-col>


 


    </b-row>
  </b-container>

  </div>
</template>

<script>

  
import animatednumber from 'animated-number-vue'
import VueSlider from 'vue-slider-component/dist-css/vue-slider-component.umd.min.js'
import 'vue-slider-component/dist-css/vue-slider-component.css'
import 'vue-slider-component/theme/default.css'

import Swatches from 'vue-swatches'
import "vue-swatches/dist/vue-swatches.min.css"

import usesmonthchart from '@/components/charts/usesmonthchart'
import fluidmonthchart from '@/components/charts/fluidmonthchart'

import { mapGetters } from 'vuex'

export default {

  data() {
    return {
      id: this.$route.params.id,
      hygeneindexgoal:82,
      hygeneindexrecord:75,
      hygeneindextrend:2,
      dosage: 30,
      color: '#1CA085',
      colors: [
        ['#51e5db', '#74ebe3', '#96f0ea', '#b9f5f1', '#dcfaf8', '' ]
      ],
      luminosity:80
    }
  },
  created: function(){
    this.$store.dispatch('device/fetch', this.id)
  },
  computed: {
    item() {
      return this.$store.getters['device/item']
    },
    current() {
      return {} //this.$store.getters['device/item'].current[0]
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
    animatednumber,
    VueSlider,
    Swatches,
    usesmonthchart,
    fluidmonthchart
  }
}
</script>

