<template>
  <b-card
    title="Fluid"
    sub-title="good for 3 days"
    class="shadow p-3 mb-5 bg-white rounded"
  >
    <guage :value='fluidlevel'/>
    <h1 class="text-center">{{fluidlevel}}%</h1>
    <p class="text-center">
      <fa class="d-inline" icon="phone-volume" />
      <fa class="d-inline" icon="user" />
    </p>
  </b-card>
</template>
<script>
import guage from './guage'
export default {
  props: ['fluidlevel'],
  components: {
    guage
  }
}
</script>

