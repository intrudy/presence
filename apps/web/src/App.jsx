
import React from 'react'

import Header from './components/Header'
import Error from './components/Error'
import Dashboard from './components/Dashboard'


export function Default() {
  return (
    <>
      <Header/>
      <Error/>
    </>
  )
}

export default class App extends React.Component {
  render() {
    return (
      <React.StrictMode>
        <Dashboard/>
      </React.StrictMode>
    )
  }
}
