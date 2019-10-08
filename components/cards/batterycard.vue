<template>
  <b-card
      title="Battery"
      sub-title="good for 172 days"
      class="shadow p-3 mb-5 bg-white rounded"
    >
      <guage :value="batterylevel"/>
      
      <h1 class="text-center">
        <animatednumber :value='batterylevel' :duration='500' :delay='100' round='1'/>% 
        <fa v-if="charging" class="d-inline" icon="plug" />
      </h1>
     
      <button type="button" class="container-fluid mt-4 btn btn-outline-primary btn-sm">Remote Restart</button>
    
    </b-card>
</template>
<script>

import animatednumber from 'animated-number-vue'
import guage from './guage'

export default {
  props: ['batterylevel','charging'],
  components: {
     guage,
     animatednumber
  }
}
</script>

