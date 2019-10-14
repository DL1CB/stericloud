<template>
<div id="nav-scroller">
  <b-container fluid  >
   
    <b-navbar sticky toggleable="lg" variant="dark" type="dark">
      
      <b-navbar-brand class="text-uppercase" href="#">
        <h1>Stericloud</h1>
      </b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"/>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav pills  v-b-scrollspy:nav-scroller class="ml-auto">    <!-- Right aligned nav items -->
          <b-nav-item href="#user" @click="scrollIntoView">USER</b-nav-item>
          <b-nav-item href="#owner" @click="scrollIntoView">OWNER</b-nav-item>
          <b-nav-item href="#maintainer" @click="scrollIntoView">MAINTAINER</b-nav-item>
          <b-nav-item href="#"><div class="text-primary">LOG IN</div> </b-nav-item>
        </b-navbar-nav>
      </b-collapse>
      </b-navbar>

     
  </b-container>
  
<b-container fluid>
  <b-carousel
    id="carousel-fade"
    style="text-shadow: 0px 0px 2px #000"
    fade
    controls
    indicators
    img-width="1024"
    img-height="480"
  >
    <b-carousel-slide
      caption="Where is the closest hygene dispencer ?"
      img-src="https://picsum.photos/1024/480/?image=1001"
    ></b-carousel-slide>
    <b-carousel-slide
      caption="If hygene is important ... become an owner"
      img-src="https://picsum.photos/1024/480/?image=348"
    ></b-carousel-slide>
    <b-carousel-slide
      caption="earn as you maintain dispencers"
      img-src="https://picsum.photos/1024/480/?image=189"
    ></b-carousel-slide>
  </b-carousel>
</b-container>  

<b-container class="mt-4" fluid>
  <b-row >
    <b-col sm class="text-center mb-1">
      <b-button href="#" variant="primary">Find a Dispencer</b-button>
    </b-col>
    <b-col sm class="text-center mb-1">
      <b-button href="#" variant="primary">Get a Dispencer</b-button>
    </b-col>
    <b-col sm class="text-center mb-1">
      <b-button href="#" variant="primary">Become a Maintainer</b-button>
    </b-col>
  </b-row>
</b-container>
<b-container class="mt-4" fluid>
  <b-row >
    <b-col sm class="text-center">
      <b-card bg-variant="default" border-variant="light" text-variant="dark" title="For users">
        <b-card-text>
          <b-nav vertical>
            <b-nav-item>About Hygene</b-nav-item>
            <b-nav-item>Cities</b-nav-item>
            <b-nav-item>Help</b-nav-item>
            <b-nav-item>Safety</b-nav-item>
            <b-nav-item>Events</b-nav-item>
          </b-nav>
        </b-card-text>
       
      </b-card>
    </b-col>
    <b-col sm class="text-center">
      <b-card bg-variant="default" border-variant="light" text-variant="dark" title="For owners">
        <b-card-text>
          <b-nav vertical>
            <b-nav-item>Become an Owner</b-nav-item>
            <b-nav-item>Why Stericloud</b-nav-item>
            <b-nav-item>Cleaning</b-nav-item>
            <b-nav-item>Maintenance</b-nav-item>
            <b-nav-item>Pricing</b-nav-item>
          </b-nav>
        </b-card-text>
       
      </b-card>
    </b-col>
    <b-col sm class="text-center">
      <b-card bg-variant="default" border-variant="light" text-variant="dark" title="For maintainers">
        <b-card-text>
          <b-nav vertical>
            <b-nav-item>Become a Maintainer</b-nav-item>
            <b-nav-item>Cities</b-nav-item>
            <b-nav-item>Training</b-nav-item>
            <b-nav-item>Safety</b-nav-item>
            <b-nav-item>Events</b-nav-item>
          </b-nav>
        </b-card-text>
      </b-card>
    </b-col>
    
  </b-row>
</b-container>


</div>
</template>

<script>
  export default {
    methods: {
      // Convenience method to scroll a heading into view.
      // Not required for scrollspy to work
      scrollIntoView(evt) {
        evt.preventDefault()
        const href = evt.target.getAttribute('href')
        const el = href ? document.querySelector(href) : null
        if (el) {
          this.$refs.content.scrollTop = el.offsetTop
        }
      }
    },
    data() {
      return {
        text: `
          Quis magna Lorem anim amet ipsum do mollit sit cillum voluptate ex nulla
          tempor. Laborum consequat non elit enim exercitation cillum aliqua
          consequat id aliqua. Esse ex consectetur mollit voluptate est in duis
          laboris ad sit ipsum anim Lorem. Incididunt veniam velit elit elit veniam
          Lorem aliqua quis ullamco deserunt sit enim elit aliqua esse irure. Laborum
          nisi sit est tempor laborum mollit labore officia laborum excepteur
          commodo non commodo dolor excepteur commodo. Ipsum fugiat ex est consectetur
          ipsum commodo tempor sunt in proident.
        `
      }
    }
  }
</script>
