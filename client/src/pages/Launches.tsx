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
import {
Tooltip,
TooltipContent,
TooltipProvider,
TooltipTrigger,
} from "@/components/ui/tooltip"
import { Badge } from "@/components/ui/badge"
import { ArrowUpDown } from "lucide-react"
import { Button } from "@/components/ui/button"
import ytIcon from "../assets/ytIcon.png"
import wikiIcon from "../assets/wikiIcon.png"
import redditIcon from "../assets/redditIcon.png"
import ytDisabled from "../assets/ytDisabled.png"
import wikiDisabled from "../assets/wikiDisabled.png"
import redditDisabled from "../assets/redditDisabled.png"


export type Launch = {
    id: string
    success: boolean
    name: string
    date_utc: Date
    webcast: string
    wikipedia: string
    patch: string
    reddit: string
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

    const dateSortFn = (rowA:any, rowB:any, columnId:string) => {
        /**Custom date sorting function for the launches table */

        const dateA = new Date(rowA.original[columnId])
        const dateB = new Date(rowB.original[columnId])
        return dateA.valueOf() - dateB.valueOf()
      }

    interface IconCreatorProps {
        href?: string
        src: string
        alt: string
        className: string
        id: string
    }

    function IconCreator({id, href, src, alt, className }: IconCreatorProps) {
        /**Handles the availability of external links 
         * and presents as disabled or enabled */
        return (
            <TooltipProvider delayDuration={0}>
                <Tooltip>
                    <TooltipTrigger asChild>
                        {href ? <a href={href} target="_blank" rel="noopener noreferrer" className="inline-block">
                            <img data-testid={id} src={src} alt={alt} className={`${className}`} />
                        </a>
                        :
                        <img data-testid={id} src={src} alt={alt} className={`${className}`} />}
                        </TooltipTrigger>
                <TooltipContent side="bottom">
                {href ? <p>Open {alt}</p> : <p>{alt} Unavailable</p>}
                </TooltipContent>
                </Tooltip>
            </TooltipProvider>
        );
    };
    

    const columns = useMemo(() => [
        {
            accessorKey: "patch",
            header: () => <div className="text-center"></div>,
            cell: ({ cell }:any) => {
                let patchUrl = cell.getValue()
                return (
                    <div className="flex justify-center">
                        {patchUrl ?
                        <img 
                        src={cell.getValue()} 
                        alt="Patch" 
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
            header: ({ column }:any) => {
                return (
                <div className="text-center">
                    <Button
                    data-testid="nameSortButton"
                    variant="ghost"
                    onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
                    >
                    Name
                    <ArrowUpDown className="ml-2 h-4 w-4" />
                    </Button>
                </div>
                )
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
        {
            accessorKey: "date_utc",
            sortingFn: dateSortFn,
            header: ({column}:any) => {
                return (
                <div className="text-center">
                    <Button
                    data-testid="dateButton"
                    variant="ghost"
                    onClick={() => column.toggleSorting(column.getIsSorted() === "asc")}
                    >
                    Date (UTC)
                    <ArrowUpDown className="ml-2 h-4 w-4" />
                    </Button>
                </div>
                )
              },
            cell: ({ cell }:any) => {
                let date = cell.getValue()
                  return format(new Date(date), 'dd MMM yyyy, HH:mm')
              },
        },
        {
            accessorKey: "webcast",
            header: () => <div className="text-center"></div>,
            cell: ({ cell }:any) => {
                let webcastUrl = cell.getValue()
                return (
                    <div className="flex justify-center">
                        {webcastUrl ?
                        <IconCreator
                        id={cell.id}
                        href={cell.getValue()} 
                        src={ytIcon}
                        alt="YouTube"
                        className="w-15 h-10"
                        />
                        : 
                        <IconCreator
                        id={cell.id}
                        src={ytDisabled}
                        alt="YouTube"
                        className="w-15 h-10"
                        />
                        }
                    </div>
                )
            },
        },
        {
            accessorKey: "wikipedia",
            header: () => <div className="text-center"></div>,
            cell: ({ cell }:any) => {
                let wikipediaUrl = cell.getValue()
                return (
                    <div className="flex justify-center">
                        {wikipediaUrl ?
                        <IconCreator
                        id={cell.id}
                        href={cell.getValue()} 
                        src={wikiIcon}
                        alt="Wikipedia"
                        className="w-20 h-15"
                        />
                        : 
                        <IconCreator
                        id={cell.id}
                        src={wikiDisabled}
                        alt="Wikipedia"
                        className="w-20 h-15"
                        />
                        }
                    </div>
                )
            },
        },
        {
            accessorKey: "reddit",
            header: () => <div className="text-center"></div>,
            cell: ({ cell }:any) => {
                let redditUrl = cell.getValue()
                return (
                    <div className="flex justify-center">
                        {redditUrl ?
                        <IconCreator
                        id={cell.id}
                        href={cell.getValue()} 
                        src={redditIcon}
                        alt="Reddit"
                        className="w-15 h-15"
                        />
                        : 
                        <IconCreator
                        id={cell.id}
                        src={redditDisabled}
                        alt="Reddit"
                        className="w-15 h-15"
                        />
                        }
                    </div>
                )
            },
        },
        ],
        [],
    )

    return (
        <div className="flex p-3 flex-col gap-2 items-center">
                <div className="flex w-full space-x-7">
                        <Select onValueChange={onYearSelectionChange}>
                        <SelectTrigger data-testid="yearSelector" className="text-white w-[140px] bg-zinc-900">
                            <SelectValue placeholder="Select a year" />
                        </SelectTrigger>
                        <SelectContent className="text-white bg-zinc-900" >
                            {launchYears.map((year, index) => (
                                <SelectItem  data-testid={`yearSelectorOption${year}`} key={index} value={year}>{year}</SelectItem>
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
                <div className="w-100 text-primary text-3xl font-bold uppercase ">
                    No year selected
                </div>
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