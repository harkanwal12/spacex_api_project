import { useLoaderData } from "react-router-dom";
import { ApiClient } from "@/lib/api";
import { DataTable } from "@/components/DataTable";
import { useMemo, useState } from 'react';
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
  } from "@/components/ui/select"

export type Launch = {
    id: string
    success: boolean
    name: string
    date_utc: Date
  }

export async function loader() {

    let api = new ApiClient();
    let launchYears = await api.getAllUniqueLaunchYears()
    
    return launchYears
}

const Launches = () => {

    const [launchesData, setLaunches] = useState<Launch[]>([]);

    const launchYears = useLoaderData() as string[];

    const onYearSelectionChange = async (value: string) => {
        if (value === "default") {
            setLaunches([])
        } else {
            let api = new ApiClient()
            let launches = await api.getAllLaunchesInYear(value)
            setLaunches(launches)
        }
        
    }

    const columns = useMemo(() => [
        {
            accessorKey: "patch",
            header: () => <div className="text-center">Patch</div>,
            cell: ({ cell }:any) => {
                let patchUrl = cell.getValue()
                return (
                    <div className="flex justify-center">
                        {patchUrl ?
                        <img 
                        src={cell.getValue()} 
                        alt="Item" 
                        style={{ width: '100px', height: '100px' }} />
                        : 
                        <div className="w-24 h-24 flex items-center justify-center border">
                            No patch available
                        </div>
                        }
                    </div>
                    
                )
            },
        },
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
        <div className="flex p-2 flex-col gap-2 items-center">
                <div className="flex w-full space-x-7">
                        <Select onValueChange={onYearSelectionChange}>
                        <SelectTrigger className="text-white w-[140px] bg-zinc-900">
                            <SelectValue placeholder="Select a year" />
                        </SelectTrigger>
                        <SelectContent className="text-white bg-zinc-900" >
                            {launchYears.map((year, index) => (
                                <SelectItem  data-testid={`yearSelectorOptionAll${year}`} key={index} value={year}>{year}</SelectItem>
                            ))}
                        </SelectContent>
                        </Select>

                    {launchesData.length > 0 && 
                        <div className="text-white flex items-center space-x-2">
                            <span >Number of Launches:</span>
                            <div data-testid="launchesTableRowCounter">{launchesData.length}</div>
                        </div>}
            </div>
            {launchesData.length > 0 && <DataTable columns={columns} data={launchesData}/>}
        </div>
    )
}

export default Launches