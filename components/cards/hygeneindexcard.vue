<template>
    <b-card
    title="Hygene Index"
    sub-title="today"
    class="shadow p-3 mb-5 bg-white rounded"
    >
        <guage :value='hygeneindex || 0'/>
        <h1 class="text-center" >
          {{hygeneindex || 0}}% 
          <fa v-if="hygeneindextrend > 0" class="d-inline" icon="chevron-up" />
          <fa v-if="hygeneindextrend < 0" class="d-inline" icon="chevron-down" />

        </h1>
        <p class="text-center">{{hygeneindexgoal || 0}}%<fa class="d-inline ml-1 mr-2" icon="carrot" /> | <fa class="d-inline ml-2 mr-1" icon="award" />{{hygeneindexrecord || 0}}%</p>
    </b-card>
</template>
<script>
import guage from './guage'
export default {
  props:['hygeneindex','hygeneindexgoal','hygeneindexrecord','hygeneindextrend'],
  components: {
    guage,
  }
}
</script>

