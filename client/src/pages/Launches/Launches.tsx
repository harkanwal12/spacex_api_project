import { useLoaderData } from "react-router-dom";
import { ApiClient } from "@/lib/api";
import { LaunchesTable } from "@/pages/Launches/LaunchesTable";
import { useMemo } from 'react';

export type Launch = {
    id: string
    success: boolean
    name: string
    date_utc: Date
  }

  export type LaunchData = {
    launches: Launch[]
  }

export async function loader() {

    let api = new ApiClient();
    let launches = await api.getAllLaunches()
    
    return { launches }
}

const Launches = () => {
    const {launches} = useLoaderData() as LaunchData;

    const years = [...new Set(launches.map(launch => new Date(launch.date_utc).getFullYear()))]

    // Define table columns
    const columns = useMemo(() => [
        {
            accessorKey: "name",
            header: () => <div className="text-center">Name</div>,
        },
        {
            accessorKey: "success",
            header: () => <div className="text-center">Success</div>,
        },
        {
            accessorKey: "date_utc",
            header: () => <div className="text-center">Date</div>
        },
        ],
        [],
    )

    return (
        <div className="container mx-auto py-2">
            <LaunchesTable columns={columns} data={launches} years={years}/>
        </div>
    )
}

export default Launches