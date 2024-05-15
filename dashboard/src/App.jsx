
import React from 'react'

import Header from './components/Header'
import Entry from './components/Entry'


export default class App extends React.Component {
  render() {
    return (
      <React.StrictMode>
        <Header />
        <Entry />
      </React.StrictMode>
    )
  }
}
