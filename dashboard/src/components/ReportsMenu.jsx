
import React from 'react'

import {
  Disclosure,
  DisclosureButton,
  DisclosurePanel,
  Popover,
  PopoverButton,
  PopoverPanel,
  Transition
} from '@headlessui/react'
import { ChevronDownIcon, CloudArrowDownIcon } from '@heroicons/react/20/solid'
import { ArrowPathIcon, ChartPieIcon } from '@heroicons/react/24/outline'

import {classNames} from '../utils'


const reports = [
  { name: 'Analytics', description: 'Accurate attendance metrics for your events', href: '#', icon: ChartPieIcon },
  { name: 'Automations', description: 'Schedule recurring reports and analytics', href: '#', icon: ArrowPathIcon },
]
const actions = [
  { name: 'Download Reports', href: '#', icon: CloudArrowDownIcon },
]


function mobile() {
    return (
      <Disclosure as="div" className="-mx-3">
        {({ open }) => (
          <>
            <DisclosureButton className="flex w-full items-center justify-between rounded-lg py-2 pl-3 pr-3.5 text-base font-semibold leading-7 text-gray-900 hover:bg-gray-50">
              Reports
              <ChevronDownIcon
                className={classNames(open ? 'rotate-180' : '', 'h-5 w-5 flex-none')}
                aria-hidden="true"
              />
            </DisclosureButton>
            <DisclosurePanel className="mt-2 space-y-2">
              {[...reports, ...actions].map((item) => (
                <DisclosureButton
                  key={item.name}
                  as="a"
                  href={item.href}
                  className="block rounded-lg py-2 pl-6 pr-3 text-sm font-semibold leading-7 text-gray-900 hover:bg-gray-50"
                >
                  {item.name}
                </DisclosureButton>
              ))}
            </DisclosurePanel>
          </>
        )}
      </Disclosure>
    )
}

function web() {
    return (
      <Popover className="relative">
          <PopoverButton className="flex items-center gap-x-1 text-sm font-semibold leading-6 text-gray-900">
          Reports
          <ChevronDownIcon className="h-5 w-5 flex-none text-gray-400" aria-hidden="true" />
          </PopoverButton>

          <Transition
            as={React.Fragment}
            enter="transition ease-out duration-200"
            enterFrom="opacity-0 translate-y-1"
            enterTo="opacity-100 translate-y-0"
            leave="transition ease-in duration-150"
            leaveFrom="opacity-100 translate-y-0"
            leaveTo="opacity-0 translate-y-1"
          >
          <PopoverPanel className="absolute -left-8 top-full z-10 mt-3 w-screen max-w-md overflow-hidden rounded-3xl bg-white shadow-lg ring-1 ring-gray-900/5">
              <div className="p-4">
              {reports.map((item) => (
                  <div
                    key={item.name}
                    className="group relative flex items-center gap-x-6 rounded-lg p-4 text-sm leading-6 hover:bg-gray-50"
                  >
                    <div className="flex h-11 w-11 flex-none items-center justify-center rounded-lg bg-gray-50 group-hover:bg-white">
                        <item.icon className="h-6 w-6 text-gray-600 group-hover:text-indigo-600" aria-hidden="true" />
                    </div>
                    <div className="flex-auto">
                        <a href={item.href} className="block font-semibold text-gray-900">
                          {item.name}
                          <span className="absolute inset-0" />
                        </a>
                        <p className="mt-1 text-gray-600">{item.description}</p>
                    </div>
                  </div>
              ))}
              </div>
              <div className="grid grid-cols-1 divide-x divide-gray-900/5 bg-gray-50">
              {actions.map((item) => (
                  <a
                  key={item.name}
                  href={item.href}
                  className="flex items-center justify-center gap-x-2.5 p-3 text-sm font-semibold leading-6 text-gray-900 hover:bg-gray-100"
                  >
                  <item.icon className="h-5 w-5 flex-none text-gray-400" aria-hidden="true" />
                  {item.name}
                  </a>
              ))}
              </div>
          </PopoverPanel>
          </Transition>
      </Popover>
    )
}

const Reports = {Mobile: mobile, Web: web}
export default Reports
