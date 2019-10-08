<template>
  <b-container>
    <b-form @submit="onSubmit" @reset="onReset" v-if="show">

        <b-form-group
        id="organisation"
        description="please enter your organisations details"
        label="Organisation"
        >
            <b-form-input id="input-name" v-model="organisation.name" placeholder="organisation name"  trim></b-form-input>
        </b-form-group>

        <b-form-group
            id="organisation"
            description="please enter your organisations address"
            label="Address">

            <b-form-input id="input-street" v-model="organisation.street" placeholder="street name"  trim></b-form-input>
            <b-form-input id="input-number" v-model="organisation.number" placeholder="street number"  trim></b-form-input>
            <b-form-input id="input-city" v-model="organisation.city" placeholder="city name"  trim></b-form-input>
            <b-form-input id="input-postalcode" v-model="organisation.postalcode" placeholder="zip ro postal code"  trim></b-form-input>
            <b-form-input id="input-state" v-model="organisation.state" placeholder="state or province"  trim></b-form-input>
            <b-form-input id="input-country" v-model="organisation.country" placeholder="country name"  trim></b-form-input>
          
        </b-form-group>
 
      <b-button type="submit" variant="primary">Save</b-button>
      <b-button type="reset" variant="danger">Clear</b-button>    

    </b-form>
  </b-container>
</template>

<script>
  export default {
    data() {
      return {
        organisation: {
            name: '',
            street : '',
            number : '',
            city : '',
            postalcode : '',
            state : ''
        },
        show: true
      }
    },
    methods: {
      onSubmit(evt) {
        evt.preventDefault()
        this.$store.dispatch('owner/createowner', this.organisation)   
      },
      onReset(evt) {
        evt.preventDefault()
        // Reset our form values
  
        this.organisation.name = ''
        this.organisation.street = ''
        this.organisation.number = ''
        this.organisation.city = ''
        this.organisation.postalcode = ''
        this.organisation.state = ''
        this.organisation.country = ''

        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>