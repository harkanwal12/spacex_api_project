import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import { RouterProvider, createMemoryRouter } from "react-router-dom";
import { testRoutes } from "../routes/TestRoutes";
import userEvent from '@testing-library/user-event';

describe("Home page", () => {
    let router;

    beforeEach(() => {
        // Mock react router reports route
        router = createMemoryRouter(testRoutes, {
          initialEntries: ["/"],
          initialIndex: 0,
        });
    
    
        render(
            <RouterProvider router={router} />
        );
    });

    afterEach(() => {
        vi.clearAllMocks();
    });

    it("Renders homepage with nav bar and landing page correctly", async () => {
        await waitFor(() => screen.getAllByText(/SpaceX API Client/i))

        const navBar = screen.getByTestId("navigationbar")
        const launchesBoxLink = screen.getByTestId("launchesBoxLink")
        const launchsitesBoxLink = screen.getByTestId("launchsitesBoxLink")

        expect(navBar).toBeInTheDocument();
        expect(launchesBoxLink).toBeInTheDocument();
        expect(launchsitesBoxLink).toBeInTheDocument();
        expect(screen.getByText(/Welcome to the unofficial/i)).toBeInTheDocument();
    })

    it("Verify launches box works", async () => {
        await waitFor(() => screen.getAllByText(/SpaceX API Client/i))

        const user = userEvent.setup();
        const launchesBoxLink = screen.getByTestId("launchesBoxLink")

        await user.click(launchesBoxLink)

        expect(screen.getByText(/Select a year to discover the launches that took place/i)).toBeInTheDocument();
    })

    it("Verify launchsites box works", async () => {
        await waitFor(() => screen.getAllByText(/SpaceX API Client/i))

        const user = userEvent.setup();
        const launchsitesBoxLink = screen.getByTestId("launchsitesBoxLink")

        await user.click(launchsitesBoxLink)

        expect(screen.getByText(/Select a launch site to explore its history and the launches that happened there./i)).toBeInTheDocument();
    })
    it("Verify launches navbar link works", async () => {
        await waitFor(() => screen.getAllByText(/SpaceX API Client/i))

        const user = userEvent.setup();
        const launchesNavLink = screen.getByTestId("launchesNavLink")

        await user.click(launchesNavLink)

        expect(screen.getByText(/Select a year to discover the launches that took place/i)).toBeInTheDocument();
    })

    it("Verify launchsites navbar link works", async () => {
        await waitFor(() => screen.getAllByText(/SpaceX API Client/i))

        const user = userEvent.setup();
        const launchsitesNavLink = screen.getByTestId("launchsitesNavLink")

        await user.click(launchsitesNavLink)

        expect(screen.getByText(/Select a launch site to explore its history and the launches that happened there./i)).toBeInTheDocument();
    })
})