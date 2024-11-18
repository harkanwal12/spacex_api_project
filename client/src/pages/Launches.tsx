import { useLoaderData } from "react-router-dom";
import { ApiClient } from "@/lib/api";
import { DataTable } from "@/components/DataTable";
import { format } from 'date-fns';
import { useMemo, useState } from 'react';
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
  } from "@/components/ui/select"

import { Badge } from "@/components/ui/badge"

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
        let api = new ApiClient()
        let launches = await api.getAllLaunchesInYear(value)
        setLaunches(launches)
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
        {
            accessorKey: "date_utc",
            header: () => <div className="text-center">Date</div>,
            cell: ({ cell }:any) => {
                let date = cell.getValue()
                  return format(new Date(date), 'dd MMM yyyy, HH:mm')
              },
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
            {launchesData.length > 0 ? <DataTable columns={columns} data={launchesData}/> 
            : 
            <div className="text-white flex-col w-[40vw] min-h-[70vh] items-center inline-flex justify-center">
                <div className="w-100 text-primary text-3xl font-bold uppercase ">No year selected</div>
                <div>
            <p className="italic text-center text-muted-foreground text-xl font-medium mt-8">
              Select a year to discover the launches that took place
            </p>
            </div>
                </div>}
        </div>
    )
}

export default Launches