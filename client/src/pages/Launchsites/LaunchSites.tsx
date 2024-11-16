import { useLoaderData } from "react-router-dom";
import { ApiClient } from "@/lib/api";
import { LaunchSitesTable } from "@/pages/Launchsites/LaunchSitesTable";
import { useMemo, useState } from 'react';

export type Launch = {
  id_launch: string
  name_launch: string
  date_utc: Date
  success: boolean
}

export type Launchsite = {
  id_launchpad: string
  name_launchpad: string
  full_name: string
  locality: string
  status: string
  images: string
  details: string
  launch_attempts: number
  launches: Launch[]
}

export type LaunchsiteData = {
  launchsites: Launchsite[]
}

export async function loader() {

  let api = new ApiClient();
  let launchsites = await api.getAllLaunchpadsWithLaunches()
  
  return { launchsites }
}

const LaunchSites = () => {
  const {launchsites} = useLoaderData() as LaunchsiteData
  const [selectedLaunchSite, setSelectedLaunchSite] = useState<Launchsite | null>(null);


  const onLaunchSiteSelectionChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedName = event.target.value;
    const selectedLaunchSite = launchsites.find(obj => obj.name_launchpad === selectedName) || null;
    setSelectedLaunchSite(selectedLaunchSite)
  }

  const columns = useMemo(() => [
    {
        accessorKey: "name_launch",
        header: () => <div className="text-center">Name</div>,
    },
    {
        accessorKey: "date_utc",
        header: () => <div className="text-center">Date</div>
    },
    {
      accessorKey: "success",
      header: () => <div className="text-center">Success</div>
    },
    ],
    [],
)

  return (
    <div className="flex flex-col gap-4 p-3">
      <div className="flex flex-col items-center justify-items-center">
        <div className="flex items-center space-x-2">
        <span>Select launch site:</span>
          <select
            className="border border-gray-300 rounded-md p-2"
            onChange={onLaunchSiteSelectionChange}
          >
            <option value="">Select...</option>
            {launchsites.map((launchsite) => (
            <option key={launchsite.id_launchpad} value={launchsite.name_launchpad}>
              {launchsite.full_name}
            </option>
          ))}
          </select>
        </div>
      </div>
      {selectedLaunchSite ? 
        <div className="flex flex-row justify-between gap-5">
          <div className="flex flex-col place-items-center w-1/2 gap-2">
            <h1 className="font-bold">Launch Site Metadata</h1>
              <div className="grid grid-cols-2">
              <div className="min-h-32 max-h-fit border p-4">
                <img src={selectedLaunchSite?.images} max-width="100%" height="auto"/>
              </div>
              <table className="border border-gray-300">
                <tbody>
                  <tr>
                    <td className="border border-gray-300 p-2">Short Name</td>
                    <td className="border border-gray-300 p-2">{selectedLaunchSite?.name_launchpad}</td>
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
          <div className="w-1/2">
            <LaunchSitesTable columns={columns} data={selectedLaunchSite?.launches}/>
          </div>
        </div>
      :
        <p>No Launch Site selected</p>  
      }
    </div>
  )
}
  
  export default LaunchSites