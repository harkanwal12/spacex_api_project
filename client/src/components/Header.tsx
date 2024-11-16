
import { Link } from "react-router-dom";
 
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
  navigationMenuTriggerStyle,
} from "@/components/ui/navigation-menu"

import spacexLogoBlack from "../assets/spacexLogoBlack.png"


const Header = () => {

    return (
      <>
        <div className="z-[2] bg-white sticky top-0 w-full h-15 p-2 border-b-2 items-center space-x-5 inline-flex" data-testid='navigationbar'>
        <Link to={"/"}>
            <img src={spacexLogoBlack} alt="Logo" width="300" height="500"/>
        </Link>
        <NavigationMenu>
            <NavigationMenuList>
                <NavigationMenuItem>
                <Link to={"/launches"}>
                    <NavigationMenuLink className={`${navigationMenuTriggerStyle()} hover:bg-gray-100 rounded`}>
                    Launches
                    </NavigationMenuLink>
                </Link>
                </NavigationMenuItem>
                <NavigationMenuItem>
                <Link to={"/launchsites"}>
                    <NavigationMenuLink className={`${navigationMenuTriggerStyle()} hover:bg-gray-100 rounded`}>
                    Launch Sites
                    </NavigationMenuLink>
                </Link>
                </NavigationMenuItem>
            </NavigationMenuList>
        </NavigationMenu>
        </div>
      </>
      )
    
}

export default Header