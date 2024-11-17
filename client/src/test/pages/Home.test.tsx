import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import { RouterProvider, createMemoryRouter } from "react-router-dom";
import { testRoutes } from "../routes/TestRoutes";

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

        expect(navBar).toBeInTheDocument();
        expect(screen.getByText(/Welcome to the unofficial/i)).toBeInTheDocument();
        expect(screen.getByText(/This website or its associated/i)).toBeInTheDocument();
    })
})