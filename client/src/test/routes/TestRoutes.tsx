import { Route, createRoutesFromElements } from "react-router-dom";
import { mockLaunchesLoader, mockLaunchSitesLoader } from "../MockData";
import Home from "@/pages/Home";
import Launches from "@/pages/Launches";
import LaunchSites from "@/pages/LaunchSites";
import Layout from "@/pages/Layout";
import { GenericError } from "@/pages/Errors";

export const testRoutes = createRoutesFromElements(
    <Route path='/' element={<Layout/>} errorElement={<GenericError/>}>
      <Route index element={<Home/>}/>
      <Route path='launches' element={<Launches/>} loader={mockLaunchesLoader}/>
      <Route path='launchsites' element={<LaunchSites/>} loader={mockLaunchSitesLoader}/>
    </Route>
  )