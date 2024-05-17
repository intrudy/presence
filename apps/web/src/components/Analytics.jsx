
import React from "react"

import Charts from './Charts'
import { Highlights, Leaderboard } from "./Stats"


export default class Analytics extends React.Component {
  render() {
    return (
      <>
        <main className="p-6 sm:p-10 space-y-6">
          <div className="flex flex-col space-y-6 md:space-y-0 md:flex-row justify-between">
            <div className="mr-6">
              <h1 className="text-4xl font-semibold mb-2">Cohort Name</h1>
              <h2 className="text-gray-600 ml-0.5">A brief description of the Cohort</h2>
            </div>
          </div>
          <section className="grid md:grid-cols-2 xl:grid-cols-4 gap-6">
            <Highlights/>
          </section>

          <section className="grid md:grid-cols-2 xl:grid-cols-4 xl:grid-rows-3 xl:grid-flow-col gap-6">
            <Charts.Primary/>
            <Leaderboard/>
            <Charts.Secondary/>
          </section>
        </main>
      </>
    )
  }
}