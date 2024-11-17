
import { Link } from "react-router-dom";
 
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu"

import spacexLogoWhite from "../assets/spacexLogoWhite.png"


const Header = () => {

    return (
      <>
        <div className="text-white z-[2] sticky top-0 w-full h-15 p-2 items-center space-x-5 inline-flex" data-testid='navigationbar'>
        <Link to={"/"}>
            <img src={spacexLogoWhite} alt="Logo" width="300" height="500"/>
        </Link>
        <NavigationMenu>
            <NavigationMenuList>
                <NavigationMenuItem>
                    <NavigationMenuLink asChild className={`${navigationMenuTriggerStyle()} hover:bg-gray-500 rounded`}>
                        <Link to={"/launches"}>
                        Launches
                        </Link>
                    </NavigationMenuLink>
                </NavigationMenuItem>
                <NavigationMenuItem>
                    <NavigationMenuLink asChild className={`${navigationMenuTriggerStyle()} hover:bg-gray-500 rounded`}>
                        <Link to={"/launchsites"}>
                        Launch Sites
                        </Link>
                    </NavigationMenuLink>
                </NavigationMenuItem>
            </NavigationMenuList>
        </NavigationMenu>
        </div>
      </>
      )
    
}

export default Header