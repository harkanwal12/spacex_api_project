import { afterEach, describe, expect, it, vi } from "vitest";
import { render, screen, waitFor } from "@testing-library/react";
import { RouterProvider, createMemoryRouter } from "react-router-dom";
import { testRoutes } from "../routes/TestRoutes";
import Layout from "@/pages/Layout";
import { GenericError } from "@/pages/Errors";
import userEvent from "@testing-library/user-event";

describe("Errors", () => {
    let router;

    afterEach(() => {
        vi.clearAllMocks();
    });
    
    it("Error 404 is triggered when navigating to non-existent route", async () => {
        // Mock react router reports route
        router = createMemoryRouter(testRoutes, {
            initialEntries: ["/somenonexistentroute"],
            initialIndex: 0,
          });
      
      
        render(
            <RouterProvider router={router} />
        );

        const user = userEvent.setup()

        expect(screen.getByText(/This page does not exist. Please return to the homepage./i)).toBeInTheDocument();

        const homeButton = screen.getByTestId("returnToHomeLink")
        await user.click(homeButton)
        expect(screen.getByText(/Welcome to the unofficial/i)).toBeInTheDocument();
    })

    it("Unexpected error throws fallback error", async () => {
        const routes = [
            {
              path: "/",
              element: <Layout />,
              errorElement:<GenericError/>,
              loader: async () => {
                throw new Error("Some unexpected error")
              },
            },
          ];
        // Mock react router reports route
        router = createMemoryRouter(routes, {
            initialEntries: ["/"],
            initialIndex: 0,
          });
      
      
        render(
            <RouterProvider router={router} />
        );

        expect(await waitFor(() => screen.getByText(/An unexpected error has occurred. Please return to the homepage./i))).toBeInTheDocument();
    })
})