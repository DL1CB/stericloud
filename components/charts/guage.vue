<script>
import { Doughnut } from 'vue-chartjs'

export default {
  extends: Doughnut,
  props:['value'],
 
  data () {
    return {
      gradient: null,

    }
  },

  computed () {


  },


  mounted () {

    this.gradient = this.$refs.canvas.getContext('2d').createLinearGradient(0, 0, 0, 450)
    
    this.gradient.addColorStop(0, 'rgba(0, 231, 255, 0.9)')
    this.gradient.addColorStop(0.5, 'rgba(0, 231, 255, 0.25)');
    this.gradient.addColorStop(1, 'rgba(0, 231, 255, 0)');
    
    this.renderChart({
      labels:['remaining','consumed'],
      datasets: [
        {
          borderColor: 'lightgrey',
          pointBackgroundColor: 'white',
          borderWidth: 1,
          pointBorderColor: 'white',
          backgroundColor: [this.gradient , 'white'],
          data: [this.value,100-this.value]
        }
      ]
    }, { 
        cutoutPercentage: 70, 
        rotation: -1 * Math.PI, 
        circumference: Math.PI ,
        responsive: true, 
        maintainAspectRatio: true,
        legend: {
            display: false,
        }
    })
    
  }
}
</script>

