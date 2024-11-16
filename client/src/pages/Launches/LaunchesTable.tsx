import * as React from "react"

import {
  ColumnFiltersState,
  ColumnDef,
  flexRender,
  getCoreRowModel,
  useReactTable,
  getFilteredRowModel,
} from "@tanstack/react-table"

import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"

interface LaunchesTableProps<TData, TValue> {
  columns: ColumnDef<TData, TValue>[]
  data: TData[]
  years: number[]
}

export function LaunchesTable<TData, TValue>({
  columns,
  data,
  years
}: LaunchesTableProps<TData, TValue>) {

  const [columnFilters, setColumnFilters] = React.useState<ColumnFiltersState>(
    []
  )

  const table = useReactTable({
    data,
    columns,
    getCoreRowModel: getCoreRowModel(),
    onColumnFiltersChange: setColumnFilters,
    getFilteredRowModel: getFilteredRowModel(),
    state: {
      columnFilters
    }
  })

  return (
    <div className="flex flex-col gap-2 items-center">
    <div className="flex space-x-20">
      <div className="flex items-center space-x-2">
      <span>Select year of Rocket Launch:</span>
        <select
          className="border border-gray-300 rounded-md p-2"
          onChange={e => table.getColumn("date_utc")?.setFilterValue(e.target.value)}
          value={(table.getColumn("date_utc")?.getFilterValue() as string) ?? ""}
        >
          <option value="">All</option>
          {years.map((year, index) => (
            <option key={index} value={year}>{year}</option>
          ))}
        </select>
      </div>
      <div className="flex items-center space-x-2">
      <span>Number of Rocket Launches:</span>
      <div>{table.getRowModel().rows.length}</div>
      </div>

    </div>
    <div className="rounded-md border w-full">
      <Table>
        <TableHeader>
          {table.getHeaderGroups().map((headerGroup) => (
            <TableRow key={headerGroup.id}>
              {headerGroup.headers.map((header) => {
                return (
                  <TableHead key={header.id} style={{ width: `${header.getSize()}px` }}>
                    {header.isPlaceholder
                      ? null
                      : flexRender(
                          header.column.columnDef.header,
                          header.getContext()
                        )}
                  </TableHead>
                )
              })}
            </TableRow>
          ))}
        </TableHeader>
        <TableBody>
          {table.getRowModel().rows?.length ? (
            table.getRowModel().rows.map((row) => (
              <TableRow
                key={row.id}
                data-state={row.getIsSelected() && "selected"}
              >
                {row.getVisibleCells().map((cell) => (
                  <TableCell key={cell.id}>
                    {flexRender(cell.column.columnDef.cell, cell.getContext())}
                  </TableCell>
                ))}
              </TableRow>
            ))
          ) : (
            <TableRow>
              <TableCell colSpan={columns.length} className="h-24 text-center">
                No results.
              </TableCell>
            </TableRow>
          )}
        </TableBody>
      </Table>
    </div>
    </div>
  )
}
