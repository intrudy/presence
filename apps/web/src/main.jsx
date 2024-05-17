
import React from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import App, {Default} from './App'
import Entry from './components/Entry'
import Home from './components/Home'
import Feature from './components/Feature'
import Guests from './components/Guests'
import Alternate from './components/Alternate'
import Item from './components/Item'


const router = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
    errorElement: <Default/>,
    children: [
      // { path: 'help', element: <Help/> },
      { path: "", element: <Home/>},
      { path: "login", element: <Entry/> },
      { path: "events", element: <Feature/> },
      { path: "cohorts", element: <Feature/> },
      { path: "guests", element: <Guests/> },
      { path: "guests/:id", element: <Item/>},
      { path: "register", element: <Entry/> },
      { path: "password/reset", element: <Entry/> }
    ]
  }
])


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
