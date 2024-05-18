
import React from 'react'
import ReactDOM from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'

import App from './App'
import Entry from './components/Entry'
import Help from './components/Help'
import ComingSoon, { ErrorPage } from './components/Landing'
import Analytics from './components/Analytics'


const router = createBrowserRouter([
  {
    path: "/",
    element: <App/>,
    errorElement: <ErrorPage/>,
    children: [
      { path: "", element: <Entry/>},
      { path: 'help', element: <Help/> },
      { path: "login", element: <ComingSoon/> },
      { path: "events", element: <ComingSoon/> },
      { path: "cohorts", element: <ComingSoon/> },
      { path: "guests", element: <ComingSoon/> },
      { path: "guests/:id", element: <ComingSoon/>},
      { path: "register", element: <ComingSoon/> },
      { path: "password/reset", element: <Entry/> },
      { path: "reports", element: <ComingSoon/> },
      { path: "reports/analytics", element: <Analytics/> }
    ]
  },
])


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)
