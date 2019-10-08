<template>
    <b-card
    title="Fluid usage"
    sub-title="last 30 days"
    class="shadow p-3 mb-5 bg-white rounded"
    >
        <fluidmonthchart />
    </b-card>
</template>
<script>

import fluidmonthchart from '@/components/charts/fluidmonthchart'

export default {
  components: {
    fluidmonthchart
  }
}
</script>
