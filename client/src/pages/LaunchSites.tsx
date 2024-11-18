import { useLoaderData } from "react-router-dom";
import { ApiClient } from "@/lib/api";
import { DataTable } from "@/components/DataTable";
import { useMemo, useState } from 'react';
import { format } from 'date-fns';
import { Badge } from "@/components/ui/badge"
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from "@/components/ui/select"

export type Launch = {
  id_launch: string
  name_launch: string
  date_utc: Date
  success: boolean
}

export type Launchsite = {
  id: string
  name: string
  full_name: string
  locality: string
  status: string
  images: string
  details: string
  launch_attempts: number
  launch_successes: number
  launch_success_rate: string
  region: string
  latitude: number
  longitude: number
  launches: Launch[]
}

export async function loader() {

  let api = new ApiClient();
  let launchsiteNames = await api.getAllLaunchpadNames()
  
  return launchsiteNames
}

const LaunchSites = () => {
  const launchsiteNames = useLoaderData() as Launchsite[]
  const [selectedLaunchSite, setSelectedLaunchSite] = useState<Launchsite | null>(null);


  const onLaunchSiteSelectionChange = async (id: string) => {
    const launchsite = launchsiteNames.find(obj => obj.id === id)
    let api = new ApiClient()
    let launchesite = await api.getLaunchpadWithLaunches(id, launchsite?.name!)
    setSelectedLaunchSite(launchesite[0])
  }

  const columns = useMemo(() => [
    {
      accessorKey: "name",
      header: () => <div className="text-center">Launch Name</div>,
    },
    {
      accessorKey: "date_utc",
      header: () => <div className="text-center">Date of Launch</div>,
      cell: ({ cell }:any) => {
        let date = cell.getValue()
          return format(new Date(date), 'dd MMM yyyy, HH:mm')
      },
    },
    {
      accessorKey: "success",
      header: () => <div className="text-center">Success</div>,
      cell: ({ cell }:any) => {
        let success = cell.getValue()
        switch (success) {
          case true:
              return (
                  <Badge variant="green">Success</Badge>
              )
          case false:
              return (
                  <Badge variant="red">Failure</Badge>
              )
          default:
              return (
                  <Badge variant="grey">Unknown</Badge>
              )
        }
      },
    },
    ],
    [],
)

  return (
    <div className="flex flex-col items-center gap-4 p-3">
      <div className="flex w-full">
        <Select onValueChange={onLaunchSiteSelectionChange}>
        <SelectTrigger className="text-white w-[500px] bg-zinc-900">
            <SelectValue placeholder="Select a launch site" />
        </SelectTrigger>
        <SelectContent className="text-white bg-zinc-900" >
            {launchsiteNames.map((launchsite) => (
                <SelectItem  key={launchsite.id} value={launchsite.id}>{launchsite.full_name}</SelectItem>
            ))}
        </SelectContent>
        </Select>
      </div>
      {selectedLaunchSite ? 
        <div className="text-white flex flex-row justify-between gap-5">
          <div className="flex flex-col place-items-center w-8/12 gap-2">
              <div className="grid grid-cols-2 gap-5">
              <div className="min-h-32 max-h-fit bg-gray-900 border p-2">
                <img data-testid="launchSiteImg" src={selectedLaunchSite?.images} max-width="100%" height="auto"/>
              </div>
              <div className="uppercase grid grid-cols-3 ">
                <div className="justify-items-start pl-3">
                  <h3 className="text-sm text-gray-200">Short Name</h3>
                  <p className="font-bold text-gray-300">{selectedLaunchSite?.name}</p>
                </div>
                <div className="justify-items-start pl-3 col-span-2">
                  <h3 className="text-sm text-gray-200">Location</h3>
                  <p className="font-bold text-gray-300">{`${selectedLaunchSite?.locality}, ${selectedLaunchSite?.region}`}</p>
                </div>
                <div className="justify-items-start pl-3">
                  <h3 className="text-sm text-gray-200">Launch Attempts</h3>
                  <p className="font-bold text-gray-300">{selectedLaunchSite?.launch_attempts}</p>
                </div>
                <div className="justify-items-start pl-3">
                  <h3 className="text-sm text-gray-200">Launch Successes</h3>
                  <p className="font-bold text-gray-300">{selectedLaunchSite?.launch_successes}</p>
                </div>
                <div className="justify-items-start pl-3">
                  <h3 className="text-sm text-gray-200">Success Rate</h3>
                  <p className="font-bold text-gray-300">{selectedLaunchSite?.launch_success_rate}</p>
                </div>
                <div className="justify-items-start pl-3">
                  <h3 className="text-sm text-gray-200">Status</h3>
                  <p className="font-bold text-gray-300">{selectedLaunchSite?.status}</p>
                </div>
                <div className="justify-items-start pl-3">
                  <h3 className="text-sm text-gray-200">Latitude</h3>
                  <p className="font-bold text-gray-300">{selectedLaunchSite?.latitude}</p>
                </div>
                <div className="justify-items-start pl-3">
                  <h3 className="text-sm text-gray-200">Longitude</h3>
                  <p className="font-bold text-gray-300">{selectedLaunchSite?.longitude}</p>
                </div>
              </div>
            </div>
            <div>
            <p className="text-lg">{selectedLaunchSite?.details}</p>
            </div>
          </div>
          <div data-testid="LaunchesTableContainer" className="w-4/12">
            <DataTable columns={columns} data={selectedLaunchSite?.launches}/>
          </div>
        </div>
      :
      <div className="text-white flex-col w-[40vw] min-h-[70vh] items-center inline-flex justify-center">
          <div className="w-100 text-primary text-3xl font-bold uppercase ">
            No Launch Site selected
          </div>
          <div>
              <p className="italic text-center text-muted-foreground text-xl font-medium mt-8">
              Select a launch site to explore its history and the launches that happened there.
              </p>
          </div>
      </div>}
    </div>
  )
}
  
  export default LaunchSites