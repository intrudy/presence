
import React from "react"
import { Link } from 'react-router-dom'

import Footer from "./Footer"
import { Header, Sidebar } from "./Dashboard"


export function Signature() {
  return (
    <>
      <figcaption className="mt-10">
        <img
          className="mx-auto h-10 w-10 rounded-full"
          src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=facearea&facepad=2&w=256&h=256&q=80"
          alt=""
        />
        <div className="mt-4 flex items-center justify-center space-x-3 text-base">
          <div className="font-semibold text-gray-900">Harish Navnit</div>
          <svg viewBox="0 0 2 2" width={3} height={3} aria-hidden="true" className="fill-gray-900">
            <circle cx={1} cy={1} r={1} />
          </svg>
          <div className="text-gray-600">Founder, Turnout</div>
        </div>
      </figcaption>
    </>
  )
}

export function PageNotFound() {
  return (
    <>
      <section className="grid min-h-full place-items-center bg-white px-6 py-24 sm:py-32 lg:px-8">
        <div className="text-center">
          <p className="text-base font-semibold text-indigo-600">404</p>
          <h1 className="mt-4 text-3xl font-bold tracking-tight text-gray-900 sm:text-5xl">Page not found</h1>
          <p className="mt-6 text-base leading-7 text-gray-600">Sorry, we couldn’t find the page you’re looking for.</p>
          <div className="mt-10 flex items-center justify-center gap-x-6">
            <Link
              to={'/'}
              className="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            >
              Go back home
            </Link>
            <Link to={'/help'} className="text-sm font-semibold text-gray-900">
              Contact support <span aria-hidden="true">&rarr;</span>
            </Link>
          </div>
        </div>
      </section>
    </>
  )
}

export class ErrorPage extends React.Component {
  render() {
    return (
      <>
        <div className="flex h-full bg-gray-100">
          <Sidebar/>
          <div className="flex-grow text-gray-800">
            <Header/>
            <div id="content">
              <PageNotFound/>
            </div>
            <Footer.Minimal/>
          </div>
        </div>
      </>
    )
  }
}

export default class ComingSoon extends React.Component {
  render() {
    return (
      <>
        {/* <section className="relative isolate overflow-hidden bg-white px-6 py-24 sm:py-32 lg:px-8"> */}
        <section className="h-full flex p-6 sm:p-10 space-y-6 relative isolate overflow-hidden bg-white">
          <div className="absolute inset-0 -z-10 bg-[radial-gradient(45rem_50rem_at_top,theme(colors.indigo.100),white)] opacity-20" />
          <div className="absolute inset-y-0 right-1/2 -z-10 mr-16 w-[200%] origin-bottom-left skew-x-[-30deg] bg-white shadow-xl shadow-indigo-600/10 ring-1 ring-indigo-50 sm:mr-28 lg:mr-0 xl:mr-16 xl:origin-center" />
          <br/><br/>

          <div className="mx-auto max-w-2xl lg:max-w-4xl">
            <h2 className="text-2xl font-bold leading-7 text-gray-900 sm:truncate sm:text-3xl sm:tracking-tight">
              Coming Soon!
            </h2>
            <figure className="mt-10">
              <blockquote className="text-center text-xl font-semibold leading-8 text-gray-900 sm:text-2xl sm:leading-9">
                <p>
                  “We are working on bringing you the best experience. Please try again later or <Link to={'/help'}><span className="underline">contact us</span></Link> with your requests.”
                </p>
              </blockquote>
            </figure>
          </div>
        </section>
      </>
    )
  }
}