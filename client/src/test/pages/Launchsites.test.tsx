import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { render, screen, waitFor, within } from "@testing-library/react";
import { RouterProvider, createMemoryRouter } from "react-router-dom";
import { testRoutes } from "../routes/TestRoutes";
import userEvent from '@testing-library/user-event'
import {loader as launchsiteLoader} from "@/pages/LaunchSites";
import { mockLaunchSitesWithLaunches, mockLaunchSitesWithNoLaunches } from "../MockData";
import { ApiClient } from "@/lib/api";

vi.mock("@/lib/api")

describe("Launchsites page", () => {
    let router;
    const mockClient = vi.mocked(ApiClient, true)

    beforeEach(() => {
        // Mock react router reports route
        router = createMemoryRouter(testRoutes, {
          initialEntries: ["/launchsites"],
          initialIndex: 0,
        });
        
        mockClient.prototype.getLaunchpadWithLaunches.mockResolvedValue(mockLaunchSitesWithLaunches)
    
        render(
            <RouterProvider router={router} />
        );
    });

    afterEach(() => {
        vi.clearAllMocks();
    });

    it("Renders year selector correctly on first load", async () => {
        await waitFor(() => screen.getByText(/No Launch Site selected/i))
        const siteSelector = screen.getByTestId("LaunchSiteSelector")
        expect(siteSelector).toBeInTheDocument()
        expect(screen.getByText(/Select a launch site to explore its history and the launches that happened there./i)).toBeInTheDocument();
    })

    it("Launch site selection works correctly", async () => {
        await waitFor(() => screen.getByText(/NO LAUNCH SITE SELECTED/i))
        const launchSiteSelector = screen.getByTestId("LaunchSiteSelector")
        const user = userEvent.setup()
        await user.click(launchSiteSelector)
        // Click a launch site and verify contents
        const selectOption = screen.getByTestId('launchSiteSelectorOption5e9e4501f509094ba4566f84');
        await user.click(selectOption)

        const launchesTableContainer = screen.getByTestId("LaunchesTableContainer")
        const launchSiteImage = screen.getByTestId("launchSiteImg")

        expect(within(launchesTableContainer).getByText(/Starlink 4-20/i)).toBeInTheDocument()
        expect(within(launchesTableContainer).getByText(/05 Sep 2022/i)).toBeInTheDocument()
        expect(within(launchesTableContainer).getByText(/Unknown/i)).toBeInTheDocument()
        expect(screen.getByText(/active/i)).toBeInTheDocument()
        expect(screen.getByText(/28.5618571/i)).toBeInTheDocument()
        expect(screen.getByText(/97/i)).toBeInTheDocument()
        expect(screen.getByText(/98%/i)).toBeInTheDocument()
        expect(screen.getByText(/99/i)).toBeInTheDocument()
        expect(screen.getByText(/Location/i)).toBeInTheDocument()
        expect(screen.getByText(/Status/i)).toBeInTheDocument()
        expect(screen.getByText(/Cape Canaveral, Florida/i)).toBeInTheDocument()
        expect(screen.getByText(/Launch Attempts/i)).toBeInTheDocument()
        expect(screen.getByText(/SpaceX's primary Falcon 9 pad/i)).toBeInTheDocument()
        expect(screen.getByText(/Unknown/i)).toBeInTheDocument()
        expect(screen.getByText(/Failure/i)).toBeInTheDocument()
        expect(mockClient.prototype.getLaunchpadWithLaunches).toHaveBeenCalledWith("5e9e4501f509094ba4566f84", 'CCSFS SLC 40')
        
        expect(launchSiteImage).toHaveAttribute("src", "https://i.imgur.com/9oEMXwa.png")
    })
})

describe("Test Launchesites Loader", () => {
    const mockClient = vi.mocked(ApiClient, true)
    mockClient.prototype.getAllLaunchpadNames.mockResolvedValueOnce("something")

    it("Loader runs correctly", async () => {
        const launches = await launchsiteLoader() 
        expect(launches).toEqual("something")
        expect(mockClient.prototype.getAllLaunchpadNames).toHaveBeenCalledOnce()
    })
})

describe("Launchesites with no table data", () => {
    let router;
    const mockClient = vi.mocked(ApiClient, true)
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

    it("Loader runs correctly", async () => {
        mockClient.prototype.getLaunchpadWithLaunches.mockResolvedValueOnce(mockLaunchSitesWithNoLaunches)
        await waitFor(() => screen.getByText(/NO LAUNCH SITE SELECTED/i))
        const launchSiteSelector = screen.getByTestId("LaunchSiteSelector")
        const user = userEvent.setup()
        await user.click(launchSiteSelector)
        // Click a launch site and verify contents
        const selectOption = screen.getByTestId('launchSiteSelectorOption5e9e4501f509094ba4566f84');
        await user.click(selectOption)

        expect(screen.getByText(/No results/i)).toBeInTheDocument()
    });
});