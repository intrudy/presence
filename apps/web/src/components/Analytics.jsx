
import React from "react"

import Charts from './Charts'
import { Highlights, Leaderboard } from "./Stats"


export function PageHeader() {
  return (
    <>
      <div className="mr-6">
        <h1 className="text-4xl font-semibold mb-2">Cohort Name</h1>
        <h2 className="text-gray-600 ml-0.5">A brief description of the Cohort</h2>
      </div>
    </>
  )
}

export default class Analytics extends React.Component {
  render() {
    return (
      <>
        <main className="p-6 sm:p-10 space-y-6 relative isolate overflow-hidden bg-white">
          <div className="absolute inset-0 -z-10 bg-[radial-gradient(45rem_50rem_at_top,theme(colors.indigo.100),white)] opacity-20" />
          <div className="absolute inset-y-0 right-1/2 -z-10 mr-16 w-[200%] origin-bottom-left skew-x-[-30deg] bg-white shadow-xl shadow-indigo-600/10 ring-1 ring-indigo-50 sm:mr-28 lg:mr-0 xl:mr-16 xl:origin-center" />
          <div className="mx-auto max-w max-h">
            <section className="flex flex-col space-y-6 md:space-y-0 md:flex-row justify-between">
              <PageHeader/>
            </section>
            <br/>

            <section className="grid md:grid-cols-2 xl:grid-cols-4 gap-6">
              <Highlights/>
            </section>
            <br/>

            <section className="grid md:grid-cols-2 xl:grid-cols-4 xl:grid-rows-3 xl:grid-flow-col gap-6">
              <Charts.Primary/>
              <Leaderboard/>
              <Charts.Secondary/>
            </section>
            <br/>
          </div>
        </main>
      </>
    )
  }
}