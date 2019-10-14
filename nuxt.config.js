
module.exports = {
  mode: 'spa',
  /*
  ** Headers of the page
  */
  head: {
    title: 'STERICLOUD' || process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1, shrink-to-fit=no' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' },
      { name: 'keywords', content: '' },
      { name: 'description', content: '' },
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: 'FFF' },
  /*
  ** Global CSS
  */
  css: [
    '@radial-color-picker/vue-color-picker/dist/vue-color-picker.min.css'
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://bootstrap-vue.js.org/docs/
    'bootstrap-vue/nuxt',
    // Doc: https://axios.nuxtjs.org/usage
    //'@nuxtjs/axios',
    //'@nuxtjs/pwa',
    '@nuxtjs/apollo',
    ['nuxt-fontawesome', {
      component: 'fa', 
      imports: [
        //import whole set
        {
          set: '@fortawesome/free-solid-svg-icons',
          icons: ['fas']
        }
      ]
    }],
    ['nuxt-leaflet', { /* module options */ }],
  ],

  /*
  ** Apollo-Client module configuration
  ** See https://
  */
  apollo: {
    clientConfigs: {
      default: '~/apollo/client-configs/default.js'
    }
  },

  /*
  ** Axios module configuration
  ** See https://axios.nuxtjs.org/options
  */
  axios: {
  },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
    }
  }
}
