import { Outlet } from "react-router";

import Header from "@/components/Header";

const Layout = () => {
    
  return (
    <div className={"p-3 min-h-screen overflow-y-hidden flex flex-col"}>
      <Header />
      <div className={`min-h-fit`}>
          <Outlet />
        </div>
    </div>
  );
};

export default Layout;
