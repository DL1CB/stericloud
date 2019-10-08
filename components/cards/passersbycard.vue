<template>
    <b-card
    title="Passers by"
    sub-title="today"
    class="shadow p-3 mb-5 bg-white rounded"
    >
        <h1 class="text-center p-5">
          <fa class="d-inline" icon="walking" />
          <animatednumber class="ml-2" :value='passersby' :duration='500' :delay='100' round='1'/>
        </h1>
        <p class="text-center">2309 <fa icon="award" /></p>
    </b-card>
</template>
<script>

import animatednumber from 'animated-number-vue'

export default {
  props: ['passersby'],
  components: {
    animatednumber,
  }
}
</script>