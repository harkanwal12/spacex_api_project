
import { createBrowserRouter, createRoutesFromElements, Route } from "react-router-dom";
import Layout from "@/pages/Layout";
import Home from "@/pages/Home"

import Launches, {loader as launchesLoader} from "@/pages/Launches/Launches";
import LaunchSites from "@/pages/LaunchSites";

const routes = createRoutesFromElements(
  <Route path='/' element={<Layout/>}>
    <Route index element={<Home/>}/>
    <Route path='launches' element={<Launches/>} loader={launchesLoader}/>
    <Route path='launchsites' element={<LaunchSites/>}/>
  </Route>
)

const router = createBrowserRouter(routes, {
  basename: import.meta.env.BASE_URL
});

export {routes, router}