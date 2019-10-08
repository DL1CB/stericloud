<template>
    <b-card 
        title="Uses" 
        sub-title="today" 
        class="shadow p-3 mb-5 bg-white rounded"
        >
        <div class="p-5">
          <h1 class="text-center ">
              <fa-layers>
                  <fa icon="tint" transform="shrink-6 right-2 up-4" :style="{ color: 'rgba(0, 231, 255, 1)' }"/>
                  <fa icon="hands" />
              </fa-layers>
              <animatednumber class="ml-2" :value='uses' :duration='500' :delay='100' round='1'/>
          </h1>

        </div>
        
        <div class="text-center">627 <fa icon="award" /></div>
    </b-card>
</template>
<script>

import animatednumber from 'animated-number-vue'
export default {
  props: ['uses'],
  components: {
    animatednumber,
  }
}
</script>
