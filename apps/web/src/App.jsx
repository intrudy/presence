
import React from 'react'
import { Outlet } from 'react-router-dom'

import Header from './components/Header'
import Error from './components/Error'


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
        <Header/>
        <div id="child">
          <Outlet/>
        </div>
      </React.StrictMode>
    )
  }
}
