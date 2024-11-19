import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { render, screen, waitFor, within } from "@testing-library/react";
import { RouterProvider, createMemoryRouter } from "react-router-dom";
import { testRoutes } from "../routes/TestRoutes";
import userEvent from '@testing-library/user-event'
import {loader as launchesLoader} from "@/pages/Launches";
import { mockLaunchesInYear } from "../MockData";
import { ApiClient } from "@/lib/api";

vi.mock("@/lib/api")

describe("Launches page", () => {
    let router;
    const mockClient = vi.mocked(ApiClient, true);

    beforeEach(() => {
        // Mock react router reports route
        router = createMemoryRouter(testRoutes, {
          initialEntries: ["/launches"],
          initialIndex: 0,
        });
    
        mockClient.prototype.getAllLaunchesInYear.mockResolvedValue(mockLaunchesInYear)
        render(
            <RouterProvider router={router} />
        );
    });

    afterEach(() => {
        vi.clearAllMocks();
    });

    it("Renders year selector correctly on first load", async () => {
        await waitFor(() => screen.getByText(/NO YEAR SELECTED/i))
        const yearSelector = screen.getByTestId("yearSelector")
        expect(yearSelector).toBeInTheDocument()
        expect(screen.getByText(/Select a year to discover the launches that took place/i)).toBeInTheDocument();
        expect(screen.queryByText(/Number of Rocket Launches/i)).not.toBeInTheDocument();
    })

    it("Year selection produces table with correct contents", async () => {
        await waitFor(() => screen.getByText(/NO YEAR SELECTED/i))
        const yearSelector = screen.getByTestId('yearSelector');
        const user = userEvent.setup();

        await user.click(yearSelector)

        const selectOption = screen.getByTestId('yearSelectorOption2002');

        await user.click(selectOption)

        const rowCounter = screen.getByTestId("launchesTableRowCounter")
        const launchesTable = screen.getByRole("table")
        const launchesRows = within(launchesTable).getAllByRole("row")
        // Number of rows includes header
        expect(launchesRows.length).toBe(4)       
        expect(within(rowCounter).getByText(3)).toBeInTheDocument()
        expect(within(launchesTable).getByText(/ZUMA/i)).toBeInTheDocument()
        expect(within(launchesTable).getByText(/08 Jan 2018, 01:00/i)).toBeInTheDocument()
        expect(within(launchesTable).getByText(/No patch available/i)).toBeInTheDocument()
        expect(within(launchesTable).getByText(/SES-16/i)).toBeInTheDocument()
        expect(within(launchesTable).getByText(/31 Jan 2018, 21:25/i)).toBeInTheDocument()    
    })
    it("Icons are enabled and disabled correctly", async () => {
        await waitFor(() => screen.getByText(/NO YEAR SELECTED/i))
        const yearSelector = screen.getByTestId('yearSelector');
        const user = userEvent.setup();
        await user.click(yearSelector)
        const selectOption = screen.getByTestId('yearSelectorOption2002');
        await user.click(selectOption)

        const disabledYoutubeLink = screen.getByTestId("0_webcast")
        const disabledWikipediaLink = screen.getByTestId("0_wikipedia")
        const disabledRedditLink = screen.getByTestId("0_reddit")

        const enabledYoutubeLink = screen.getByTestId("1_webcast")
        const enabledWikipediaLink = screen.getByTestId("1_wikipedia")
        const enabledRedditLink = screen.getByTestId("2_reddit")

        expect(disabledYoutubeLink).toHaveAttribute("src", "/src/assets/ytDisabled.png")
        expect(disabledWikipediaLink).toHaveAttribute("src", "/src/assets/wikiDisabled.png")
        expect(disabledRedditLink).toHaveAttribute("src", "/src/assets/redditDisabled.png")

        expect(enabledYoutubeLink).toHaveAttribute("src", "/src/assets/ytIcon.png")
        expect(enabledWikipediaLink).toHaveAttribute("src", "/src/assets/wikiIcon.png")
        expect(enabledRedditLink).toHaveAttribute("src", "/src/assets/redditIcon.png")
    })
    it("Date sort function works correctly", async () => {
        await waitFor(() => screen.getByText(/NO YEAR SELECTED/i))
        const yearSelector = screen.getByTestId('yearSelector');
        const user = userEvent.setup();
        await user.click(yearSelector)
        const selectOption = screen.getByTestId('yearSelectorOption2002');
        await user.click(selectOption)

        // Get the row order before sorting the date
        const dateHeaderButton = screen.getByTestId("dateButton")
        const rows = screen.getAllByRole('row');

        expect(rows[1]).toHaveTextContent(/08 Jan 2018, 01:00/i)
        expect(rows[2]).toHaveTextContent(/31 Jan 2018, 21:25/i)
        expect(rows[3]).toHaveTextContent(/06 Feb 2012, 20:45/i)

        await user.click(dateHeaderButton)
        // Get the row order after sorting the date
        const rowsAfterSort = screen.getAllByRole('row');
        
        expect(rowsAfterSort[1]).toHaveTextContent(/06 Feb 2012, 20:45/i)
        expect(rowsAfterSort[2]).toHaveTextContent(/08 Jan 2018, 01:00/i)
        expect(rowsAfterSort[3]).toHaveTextContent(/31 Jan 2018, 21:25/i)
    })
    it("Name sort function works correctly", async () => {
        await waitFor(() => screen.getByText(/NO YEAR SELECTED/i))
        const yearSelector = screen.getByTestId('yearSelector');
        const user = userEvent.setup();
        await user.click(yearSelector)
        const selectOption = screen.getByTestId('yearSelectorOption2002');
        await user.click(selectOption)

        // Get the row order before sorting the names
        const nameHeaderButton = screen.getByTestId("nameSortButton")
        const rows = screen.getAllByRole('row');

        expect(rows[1]).toHaveTextContent(/ZUMA/i)
        expect(rows[2]).toHaveTextContent(/SES-16/i)
        expect(rows[3]).toHaveTextContent(/Falcon Heavy/i)

        await user.click(nameHeaderButton)
        // Get the row order after sorting the names
        const rowsAfterSort = screen.getAllByRole('row');
        
        expect(rowsAfterSort[1]).toHaveTextContent(/Falcon Heavy/i)
        expect(rowsAfterSort[2]).toHaveTextContent(/SES-16/i)
        expect(rowsAfterSort[3]).toHaveTextContent(/ZUMA/i)
    })
});

describe("Test Launches Loader", () => {
    const mockClient = vi.mocked(ApiClient, true);
    it("Loader runs correctly", async () => {
        mockClient.prototype.getAllUniqueLaunchYears.mockResolvedValue([2001, 2002])
        const launches = await launchesLoader() 
        expect(launches).toEqual([ 2001,2002])
        expect(mockClient.prototype.getAllUniqueLaunchYears).toHaveBeenCalledOnce()
    })
});