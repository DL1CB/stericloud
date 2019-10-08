<template>
  <b-card
    title="Service"
    :sub-title="'due in days '+servicein+' days'"
    class="shadow p-3 mb-5 bg-white rounded"
  >
    <guage :value='servicein'/>
    
    <h1 class="text-center">
      <animatednumber :value='servicein' :duration='500' :delay='100' round='1'/>
      <fa class="d-inline" icon="tools" />
    </h1>

    <button type="button" class="container-fluid mt-4 btn btn-outline-primary btn-sm">Request early service</button>
    
  </b-card>
</template>
<script>

import animatednumber from 'animated-number-vue'
import guage from './guage'
export default {
  props:['servicein'],
  components: {
    guage,
    animatednumber
  }
}
</script>

