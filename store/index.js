import cookieparser from 'cookieparser'
import gql from 'graphql-tag'

export const state = () => ({
    owners: [],
    loading: 0,
    stale: false,
    networkStatus : 0
  })
  
export const mutations = {

  setowners(state, owners) {
    state.owners = owners
  },

  clearowners(state) {
    state.owners = []
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

  owners: state => {
    return state.owners
  },

  loading: state => {
    return state.loading
  },


}

export const actions = {
 
  async fetchowners({ commit }){

    let client = this.app.apolloProvider.defaultClient
       
    commit('loading', 1 );

    await client.query({ 

      query: gql`query {
          owners {
            id
            name
          }
      }`,

      variables: {},

      fetchPolicy: 'network-only'

    }).then((response) => { 
        commit('loading', 0 );
        commit('clearowners');
        commit('setowners', response.data.owners );
        commit('stale', response.data.stale );
        commit('networkStatus', response.data.networkStatus );
     })

  },

  nuxtServerInit({ commit }, { req }) {
    
    let user = null

    if (req && req.headers && req.headers.cookie) {

      const parsed = cookieparser.parse(req.headers.cookie)

      user = (parsed.user && JSON.parse(parsed.user)) || null
 
    }

    commit('auth/setUser', user)

  }
}

