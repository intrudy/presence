
import React from 'react'
import ReactDOM from 'react-dom/client'
import {createBrowserRouter, RouterProvider} from 'react-router-dom'

import App from './App'
import Error from './components/Error'
import Entry from './components/Entry'


const router = createBrowserRouter([
  {path: '/', element: <App />, errorElement: <Error />},
  {path: '/login', element: <Entry />, errorElement: <Error />}
])


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
