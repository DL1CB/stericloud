import { HttpLink } from 'apollo-link-http'
import { InMemoryCache } from 'apollo-cache-inmemory'
import { WebSocketLink } from 'apollo-link-ws'


// Replace this with your project's endpoint
// const GRAPHQL_ENDPOINT = 'https://tryhasura.herokuapp.com/v1/graphql'
const GRAPHQL_WSSENDPOINT = 'wss://tryhasura.herokuapp.com/v1/graphql'

export default () => ({
 // link: new HttpLink({ uri: GRAPHQL_ENDPOINT }),
  link: new WebSocketLink({ uri: GRAPHQL_WSSENDPOINT }),
  cache: new InMemoryCache()
})