<template>
    <b-card
    title="Uses / Persons"
    sub-title="last 10 days"
    class="shadow p-3 mb-5 bg-white rounded"
    >
        <usesmonthchart/>  
    </b-card>
</template>
<script>

import usesmonthchart from '@/components/charts/usesmonthchart'

export default {
  components: {
    usesmonthchart
  }
}

</script>
  