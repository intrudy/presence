
import React from 'react'
import ReactDOM from 'react-dom/client'
import {createBrowserRouter, RouterProvider} from 'react-router-dom'

import App, {Default, Login} from './App'


const router = createBrowserRouter([
  {path: '/', element: <App />, errorElement: <Default />},
  {path: '/login', element: <Login />, errorElement: <Default />}
])


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
