<script>
import { Line } from 'vue-chartjs'

export default {
  extends: Line,
  props: ['chartdata', 'options'],
  data () {
    return {
      gradient: null,
      gradient2: null
    }
  },
  
  mounted () {

    // get a refence to the canvas and create linear gradients
    this.gradient = this.$refs.canvas.getContext('2d').createLinearGradient(0, 0, 0, 450)
    this.gradient2 = this.$refs.canvas.getContext('2d').createLinearGradient(0, 0, 0, 450)

    // define the gradients
    this.gradient.addColorStop(0, 'rgba(255, 0,0, 0.5)')
    this.gradient.addColorStop(0.5, 'rgba(255, 0, 0, 0.25)');
    this.gradient.addColorStop(1, 'rgba(255, 0, 0, 0)');
    
  
    this.gradient2.addColorStop(0, 'rgba(0, 231, 255, 0.9)')
    this.gradient2.addColorStop(0.5, 'rgba(0, 231, 255, 0.25)');
    this.gradient2.addColorStop(1, 'rgba(0, 231, 255, 0)');


    this.renderChart({
      labels: [1,2,3,4,5,6,7,8,9,10],
      datasets: [
        {
          label: 'Dispencer usage',
          borderColor: '#FC2525',
          pointBackgroundColor: 'white',
          borderWidth: 1,
          pointBorderColor: 'white',
          backgroundColor: this.gradient2,
          data: [3,5,7,8,5,6,27,81,84,66]
        },
        {
          label: 'Persons detected',
          borderColor: '#FC2525',
          pointBackgroundColor: 'white',
          borderWidth: 1,
          pointBorderColor: 'white',
          backgroundColor: this.gradient1,
          data: [66,87,77,6,7,65,44,66,33,45]
        }
      ]
    }, {responsive: true, maintainAspectRatio: true})
    
  }
}
</script>

