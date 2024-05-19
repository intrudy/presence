
export function classNames(...classes) {
  return classes.filter(Boolean).join(' ')
}

export class Http {
  constructor(serverUri) {
    this.url = serverUri
  }

  headers() {
    // TODO: Add authorization tokens
    return {'X-FOO': 'BAR'}
  }

  async get(route, params={}) {
    const r = await fetch(this.url + route + new URLSearchParams(params), {
      method: 'GET',
      headers: this.headers()
    })
    if (r.ok) { return r.json() }
    throw new Error(`GET "${this.url + route}" failed with ${r.status}`)
  }

  async put(route, data={}) {
    const r = await fetch(this.url + route, {
      method: 'PUT',
      headers: this.headers(),
      body: JSON.stringify(data)
    })

    if (r.ok) { return r }
    throw new Error(`PUT "${this.url + route}" failed with ${r.status}`)
  }

  async post(route, data={}) {
    const r = await fetch(this.url + route, {
      method: 'PUT',
      headers: this.headers(),
      body: JSON.stringify(data)
    })

    if (r.ok) { return r }
    throw new Error(`POST "${this.url + route}" failed with ${r.status}`)
  }

  async delete(route) {
    const r = await fetch(this.url + route, {
        method: 'DELETE',
        headers: this.headers()
    })

    if (r.ok) { return r }
    throw new Error(`DELETE "${this.url + route}" failed with ${r.status}`)
}
}