import { useLoaderData } from "react-router-dom";
import { ApiClient } from "@/lib/api";
import { DataTable } from "@/components/DataTable";
import { useMemo, useState } from 'react';
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
        header: () => <div className="text-center">Name</div>,
    },
    {
        accessorKey: "date_utc",
        header: () => <div className="text-center">Date</div>
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
            case "Unknown":
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
    <div className="flex flex-col gap-4 p-3">
      <div className="flex flex-col">
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
          <div className="flex flex-col place-items-center w-1/2 gap-2">
              <div className="grid grid-cols-2">
              <div className="min-h-32 max-h-fit bg-gray-900 border p-4 ">
                <img data-testid="launchSiteImg" src={selectedLaunchSite?.images} max-width="100%" height="auto"/>
              </div>
              <table data-testid="metaDataTable" className="border bg-gray-900 text-white border-gray-300">
                <tbody>
                  <tr>
                    <td className="border border-gray-300 p-2">Short Name</td>
                    <td className="border border-gray-300 p-2">{selectedLaunchSite?.name}</td>
                  </tr>
                  <tr>
                    <td className="border border-gray-300 p-2">Location</td>
                    <td className="border border-gray-300 p-2">{selectedLaunchSite?.locality}</td>
                  </tr>
                  <tr>
                    <td className="border border-gray-300 p-2">Status</td>
                    <td className="border border-gray-300 p-2">{selectedLaunchSite?.status}</td>
                  </tr>
                  <tr>
                    <td className="border border-gray-300 p-2">Launch Attempts</td>
                    <td className="border border-gray-300 p-2">{selectedLaunchSite?.launch_attempts}</td>
                  </tr>
                </tbody>
              </table>
            </div>
            <p>{selectedLaunchSite?.details}</p>
          </div>
          <div data-testid="LaunchesTableContainer" className="w-1/2">
            <DataTable columns={columns} data={selectedLaunchSite?.launches}/>
          </div>
        </div>
      :
        <p>No Launch Site selected</p>  
      }
    </div>
  )
}
  
  export default LaunchSites