import gql from 'graphql-tag'

export const state = () => ({
    item:{},
    stale:false,
    loading: 0,
    networkStatus : 0
  })
  
export const mutations = {

  setitem(state, item) {
    state.item = item
  },

  clearitem(state) {
    state.item = {}
  },

  loading(state,isLoading) {
    state.loading = isLoading
  },

  stale(state,isStale) {
    state.stale = isStale
  },

  networkStatus(state,statiusCode) {
    state.networkStatus = statiusCode
  }
}

export const getters = {

    item: state => {
        return state.item
    },

    loading: state => {
        return state.loading
    },
}

export const actions = {
  
  async fetch({ commit }, id){

    let client = this.app.apolloProvider.defaultClient
       
    commit('loading', 1 );

    await client.query({ 

      query: gql`query device($id: uuid!){
        devices_by_pk(id: $id ) {
          name 
          current: history(limit: 1, order_by: {eventid: desc}) {
            batterylevel
            charging
            created_at
            deviceid
            eventid
            fluidlevel
            maintenance
            passersby
            signalstrength
            uses
          } 
          control {
            dosage
            lighton
            lightcolor
            lightluminosity
          }
          owner {
            name
            location {
              street
              number
              city
              country
              postalcode
            }
          }
          location {
            indoorname
            north
            east
          }
        }
      }`,

      variables: {id:id},

      fetchPolicy: 'network-only'

    }).then((response) => { 
        commit('clearitem');
        commit('setitem',  response.data.devices_by_pk );
        commit('loading', 0 );
        commit('stale', response.data.stale );
        commit('networkStatus', response.data.networkStatus );
     })

  }

}