<template>
  <b-card
    title="Contract"
    sub-title="expires in 84 days"
    class="shadow p-3 mb-5 bg-white rounded"
  >
    <guage :value='remainingtime'/>

    <h1 class=" text-center">
      <animatednumber :value='remainingtime' :duration='500' :delay='100' round='1'/> 
      <fa class="d-inline" icon="calendar-day" />
      <fa v-if="contractexpired" class="d-inline text-danger" icon="exclamation" />
    </h1>

    <button type="button" class="container-fluid mt-4 btn btn-outline-primary btn-sm">Extend Contract</button>

  </b-card>
</template>
<script>

import animatednumber from 'animated-number-vue'
import guage from './guage'

export default {
  props:['remainingtime','contractexpired'],
  components: {
    guage,
    animatednumber
  }
}
</script>

