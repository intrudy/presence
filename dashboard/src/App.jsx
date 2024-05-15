
import React from 'react'

import Header from './components/Header'
import Entry from './components/Entry'
import Error from './components/Error'


export function Default() {
  return (
    <>
      <Header />
      <Error />
    </>
  )
}

export function Login() {
  return (
    <>
      <Header />
      <Entry />
    </>
  )
}

export default class App extends React.Component {
  render() {
    return (
      <React.StrictMode>
        <Header />
      </React.StrictMode>
    )
  }
}
