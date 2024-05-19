
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

  population() {
    return new Object([
      {'name': 'Tang Fei', 'score': 100, 'avatar': 'https://randomuser.me/api/portraits/women/82.jpg', },
      {'name': 'Harish Navnit', 'score': 88, 'avatar': 'https://randomuser.me/api/portraits/men/81.jpg'},
      {'name': 'Lin Pengcheng', 'score': 95, 'avatar': 'https://randomuser.me/api/portraits/men/80.jpg'},
      {'name': 'Durga Baskar', 'score': 92, 'avatar': 'https://randomuser.me/api/portraits/women/71.jpg'},
      {'name': 'Zang Zidong', 'score': 98, 'avatar': 'https://randomuser.me/api/portraits/men/84.jpg'},
      {'name': 'Zu Lei', 'score': 100, 'avatar': 'https://randomuser.me/api/portraits/women/51.jpg'}
    ])
  }

  activeCohort() {
    return new Object({
      'name': 'MTD (CS)',
      'year': '2024',
      'strength': 20,
      'stats': {
        'avg_turnout': {'absolute': 17, 'percent': 84},
        'shortfall': { 'absolute': 4, 'percent': 20 },
        'last_turnout': { 'absolute': 18, 'percent': 90 }
      }
    })
  }

  render() {
    return (
      <>
        <main className="min-h-full flex-1 p-6 sm:p-10 space-y-6 relative isolate overflow-hidden bg-white">
          <div className="absolute inset-0 -z-10 bg-[radial-gradient(45rem_50rem_at_top,theme(colors.indigo.100),white)] opacity-20" />
          <div className="absolute inset-y-0 right-1/2 -z-10 mr-16 w-[200%] origin-bottom-left skew-x-[-30deg] bg-white shadow-xl shadow-indigo-600/10 ring-1 ring-indigo-50 sm:mr-28 lg:mr-0 xl:mr-16 xl:origin-center" />
          <div className="mx-auto max-w max-h">
            <section className="flex flex-col space-y-6 md:space-y-0 md:flex-row justify-between">
              <PageHeader/>
            </section>
            <br/>

            <section className="grid md:grid-cols-2 xl:grid-cols-4 gap-6">
              <Highlights cohort={this.activeCohort()}/>
            </section>
            <br/>

            <section className="grid md:grid-cols-2 xl:grid-cols-4 xl:grid-rows-3 xl:grid-flow-col gap-6">
              <Charts.Primary/>
              <Leaderboard population={this.population()}/>
              <Charts.Secondary/>
            </section>
            <br/>
          </div>
        </main>
      </>
    )
  }
}