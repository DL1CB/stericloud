import gql from 'graphql-tag'

export const state = () => ({
    latestownerid: null,
    owner: {},
    loading: 0,
    saving: 0,
    stale: false,
    networkStatus : 0
  })
  
export const mutations = {

  setowner(state, owner) {
    state.owner = owner
  },

  clearowner(state) {
    state.owner = {}
  },

  loading(state,isLoading) {
    state.loading = isLoading
  },

  saving(state,isSaving) {
    state.saving = isSaving
  },

  stale(state,isStale) {
    state.stale = isStale
  },

  networkStatus(state,statiusCode) {
    state.networkStatus = statiusCode
  }
}

export const getters = {

  owner: state => {
    return state.owner
  },

  loading: state => {
    return state.loading
  },

  saving: state => {
    return state.saving
  },


}

export const actions = {
 
  async fetchowner({ commit }, id){

    let client = this.app.apolloProvider.defaultClient
       
    commit('loading', 1 );

    await client.query({ 

      query: gql` query owner($id: uuid!) {
        owners_by_pk(id: $id) {
          name
          devices {
            id
            name
            history(limit: 1, order_by: {eventid: desc}) {
              batterylevel
              charging
              fluidlevel
              maintenance
              passersby
              signalstrength
              uses
            }
          }
        }
      }`,

      variables: {id:id},

      fetchPolicy: 'network-only'

    }).then((response) => { 
        commit('loading', 0 );
        commit('clearowner');
        commit('setowner', response.data.owners_by_pk );
        commit('stale', response.data.stale );
        commit('networkStatus', response.data.networkStatus );
        return response.data
     })

  },

  async createowner({ commit }, owner){
    
    let client = this.app.apolloProvider.defaultClient
       
    commit('saving', 1 );

    await client.mutate({ 

      mutation: gql`mutation createorganisation($name: String, $street: String, $number: String, $city: String, $postalcode: String, $state: String, $country: String) {
        insert_owners(objects: {name: $name, location: {data: {street: $street, number: $number, city: $city, postalcode: $postalcode, state: $state, country: $country}}}) {
          returning {
            id
            name
          }
        }
      }`,

      variables: owner,

      //fetchPolicy: 'network-only'

    }).then((response) => { 
        commit('saving', 0 );
        commit('networkStatus', response.data.networkStatus );
        commit('latestownerid','828f3db4-68b4-4529-949f-64267a1e4aa2')
     })
    
  }

}