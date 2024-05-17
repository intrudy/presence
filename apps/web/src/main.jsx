
import React from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import App, {Default} from './App'
import Entry from './components/Entry'
import Landing from './components/Landing'
import Analytics from './components/Analytics'


const router = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
    errorElement: <Default/>,
    children: [
      // { path: 'help', element: <Help/> },
      { path: "", element: <Entry/>},
      { path: "login", element: <Landing/> },
      { path: "events", element: <Landing/> },
      { path: "cohorts", element: <Landing/> },
      { path: "guests", element: <Landing/> },
      { path: "guests/:id", element: <Landing/>},
      { path: "register", element: <Landing/> },
      { path: "password/reset", element: <Entry/> },
      { path: "reports", element: <Landing/> },
      { path: "reports/analytics", element: <Analytics/> }
    ]
  },
])


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
