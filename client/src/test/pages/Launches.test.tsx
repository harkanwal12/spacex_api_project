import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { render, screen, waitFor, within } from "@testing-library/react";
import { RouterProvider, createMemoryRouter } from "react-router-dom";
import { testRoutes } from "../routes/TestRoutes";
import userEvent from '@testing-library/user-event'
import {loader as launchesLoader} from "@/pages/Launches/Launches";

vi.mock('@/lib/api', () => {
    return {
      ApiClient: vi.fn().mockImplementation(() => {
        return {
            getAllLaunches: vi.fn().mockResolvedValue({ id: "someid", name: 'somedata' }),
        };
      }),
    };
  });

describe("Launches page", () => {
    let router;

    beforeEach(() => {
        // Mock react router reports route
        router = createMemoryRouter(testRoutes, {
          initialEntries: ["/launches"],
          initialIndex: 0,
        });
    
    
        render(
            <RouterProvider router={router} />
        );
    });

    afterEach(() => {
        vi.clearAllMocks();
    });

    it("Renders filter selector and table content correctly", async () => {
        await waitFor(() => screen.getByText(/Select to filter by year/i))

        const launchesTable = screen.getByRole("table")
        const launchesRows = within(launchesTable).getAllByRole("row");
        const rowCounter = screen.getByTestId("launchesTableRowCounter")
        const yearSelector = screen.getByTestId("yearSelector")

        expect(within(yearSelector).getByText("All"))
        expect(within(yearSelector).getByText("2006"))
        expect(within(yearSelector).getByText("2007"))
        expect(screen.getByText(/Select to filter by year/i)).toBeInTheDocument();
        expect(screen.getByText(/Number of Rocket Launches/i)).toBeInTheDocument();
        expect(within(rowCounter).getByText(2))
        // Row count includes the header row
        expect(launchesRows.length).toBe(3);
    })

    it("Year selection works correctly", async () => {
        await waitFor(() => screen.getByText(/Select to filter by year/i))
        const launchesTable = screen.getByRole("table")
        const launchesRows = within(launchesTable).getAllByRole("row");
        const rowCounter = screen.getByTestId("launchesTableRowCounter")

        // Before filtering table, verify row counts
        expect(within(rowCounter).getByText(2)).toBeInTheDocument()
        expect(launchesRows.length).toBe(3)

        const user = userEvent.setup()
        const yearSelector = screen.getByTestId("yearSelector")
        await user.selectOptions(yearSelector, "2006")

        // Only one row should be present
        const launchesRowsAfterYearSelection = within(launchesTable).getAllByRole("row")
        expect(within(rowCounter).getByText(1)).toBeInTheDocument()
        expect(launchesRowsAfterYearSelection.length).toBe(2)

        expect(within(launchesTable).getByText(/FalconSat/i)).toBeInTheDocument()
        expect(within(launchesTable).getByText(/Fri, 24 Mar 2006 22:30:00 GMT/i)).toBeInTheDocument()
        expect(within(launchesTable).queryByText(/DemoSat/i)).not.toBeInTheDocument()
        expect(within(launchesTable).queryByText(/Wed, 21 Mar 2007 01:10:00 GMT/i)).not.toBeInTheDocument()

        // Now select all rows again
        await user.selectOptions(yearSelector, "All")

        // Both rows should be present
        const launchesRowsAfterAllYearsSelected = within(launchesTable).getAllByRole("row")
        expect(within(rowCounter).getByText(2)).toBeInTheDocument()
        expect(launchesRowsAfterAllYearsSelected.length).toBe(3)

        expect(within(launchesTable).getByText(/FalconSat/i)).toBeInTheDocument()
        expect(within(launchesTable).getByText(/Fri, 24 Mar 2006 22:30:00 GMT/i)).toBeInTheDocument()
        expect(within(launchesTable).getByText(/DemoSat/i)).toBeInTheDocument()
        expect(within(launchesTable).getByText(/Wed, 21 Mar 2007 01:10:00 GMT/i)).toBeInTheDocument()
    })
})

describe("Test Launches Loader", () => {
    it("Loader runs correctly", async () => {
        const launches = await launchesLoader() 
        expect(launches).toEqual({ id: "someid", name: 'somedata' })
    })
})