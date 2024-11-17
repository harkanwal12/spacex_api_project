import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { render, screen, waitFor, within } from "@testing-library/react";
import { RouterProvider, createMemoryRouter } from "react-router-dom";
import { testRoutes } from "../routes/TestRoutes";
import userEvent from '@testing-library/user-event'
import {loader as launchsiteLoader} from "@/pages/LaunchSites";

vi.mock('@/lib/api', () => {
    return {
      ApiClient: vi.fn().mockImplementation(() => {
        return {
            getAllLaunchpadsWithLaunches: vi.fn().mockResolvedValue({ id: "someid", name: 'somedata' }),
        };
      }),
    };
  });

describe("Launchsites page", () => {
    let router;

    beforeEach(() => {
        // Mock react router reports route
        router = createMemoryRouter(testRoutes, {
          initialEntries: ["/launchsites"],
          initialIndex: 0,
        });
    
    
        render(
            <RouterProvider router={router} />
        );
    });

    afterEach(() => {
        vi.clearAllMocks();
    });

    it("Initial renders occurs correctly", async () => {
        await waitFor(() => screen.getByText(/Select launch site:/i))
        const launchSiteSelector = screen.getByTestId("launchSiteSelector")

        expect(screen.getByText(/Select launch site:/i)).toBeInTheDocument();
        expect(screen.getByText(/No Launch Site selected/i)).toBeInTheDocument();
        expect(within(launchSiteSelector).getByText("Vandenberg Space Force Base Space Launch Complex 3W"))
        expect(within(launchSiteSelector).getByText("test name"))
        
    })

    it("Launch site selection works correctly", async () => {
        await waitFor(() => screen.getByText(/Select launch site:/i))
        const launchSiteSelector = screen.getByTestId("launchSiteSelector")
        const user = userEvent.setup()
        // Click a launch site and verify contents
        await user.selectOptions(launchSiteSelector, "Vandenberg Space Force Base Space Launch Complex 3W")

        const launchesTableContainer = screen.getByTestId("LaunchesTableContainer")
        const launchesRows = within(launchesTableContainer).getAllByRole("row");
        const metaDataTable = screen.getByTestId("metaDataTable")
        const metaDataTableRows = within(metaDataTable).getAllByRole("row");
        const launchSiteImage = screen.getByTestId("launchSiteImg")
        expect(launchesRows.length).toBe(2)
        expect(metaDataTableRows.length).toBe(4)

        expect(within(launchesTableContainer).getByText(/FalconSat/i)).toBeInTheDocument()
        expect(within(launchesTableContainer).getByText(/Fri, 24 Mar 2006 22:30:00 GMT/i)).toBeInTheDocument()
        expect(within(metaDataTable).getByText(/VAFB SLC 3W/i)).toBeInTheDocument()
        expect(within(metaDataTable).getByText(/retired/i)).toBeInTheDocument()
        expect(within(metaDataTable).getByText(/0/i)).toBeInTheDocument()
        expect(within(metaDataTable).getByText(/Short Name/i)).toBeInTheDocument()
        expect(within(metaDataTable).getByText(/Location/i)).toBeInTheDocument()
        expect(within(metaDataTable).getByText(/Status/i)).toBeInTheDocument()
        expect(within(metaDataTable).getByText(/Launch Attempts/i)).toBeInTheDocument()
        expect(screen.getByText(/test launchsite with launch/i)).toBeInTheDocument()
        expect(launchSiteImage).toHaveAttribute("src", "https://i.imgur.com/7uXe1Kv.png")
        
        // Click another launch sites and verify details have changed
        await user.selectOptions(launchSiteSelector, "test name")

        const launchesTableContainerAfterClick = screen.getByTestId("LaunchesTableContainer")
        const launchesRowsAfterClick = within(launchesTableContainer).getAllByRole("row");
        const metaDataTableAfterClick = screen.getByTestId("metaDataTable")
        const metaDataTableRowsAfterClick = within(metaDataTable).getAllByRole("row");
        const launchSiteImageAfterClick = screen.getByTestId("launchSiteImg")
        expect(launchesRowsAfterClick.length).toBe(2)
        expect(metaDataTableRowsAfterClick.length).toBe(4)

        expect(within(launchesTableContainerAfterClick).getByText(/No results./i)).toBeInTheDocument()
        expect(within(metaDataTableAfterClick).getByText(/other/i)).toBeInTheDocument()
        expect(within(metaDataTableAfterClick).getByText(/retired/i)).toBeInTheDocument()
        expect(within(metaDataTableAfterClick).getByText(/0/i)).toBeInTheDocument()
        expect(screen.getByText(/somedetails/i)).toBeInTheDocument()
        expect(launchSiteImageAfterClick).toHaveAttribute("src", "some other link")

        expect(within(launchesTableContainerAfterClick).queryByText(/FalconSat/i)).not.toBeInTheDocument()
        expect(within(launchesTableContainerAfterClick).queryByText(/Fri, 24 Mar 2006 22:30:00 GMT/i)).not.toBeInTheDocument()
        expect(within(metaDataTableAfterClick).queryByText(/VAFB SLC 3W/i)).not.toBeInTheDocument()
        expect(screen.queryByText(/test launchsite with launch/i)).not.toBeInTheDocument()
        expect(launchSiteImageAfterClick).not.toHaveAttribute("src", "https://i.imgur.com/7uXe1Kv.png")
    })
})

describe("Test Launchesites Loader", () => {
    it("Loader runs correctly", async () => {
        const launches = await launchsiteLoader() 
        expect(launches).toEqual({ id: "someid", name: 'somedata' })
    })
})