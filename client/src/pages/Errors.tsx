import { Button } from "../components/ui/button"
import Header from '../components/Header'
import { Link, useRouteError } from "react-router-dom";

interface RouteError {
  status: number;
}

export const GenericError = () => {
  const error = useRouteError() as RouteError;

  return (
    <>
      <Header />
      <div className="text-white w-[50vw] min-h-[70vh] items-center inline-flex justify-center">
        <div className="flex-col items-center">
          <div className="flex-col justify-center items-center text-center gap-4 inline-flex">
            <div className="w-100 text-primary text-5xl font-bold">Uh oh!</div>
                <div className="text-center text-muted-foreground text-lg mt-2">
                  {error.status === 404 ? <p>
                    This page does not exist. Please return to the homepage.
                  </p> : 
                  <p>
                  An unexpected error has occurred. Please return to the homepage.
                  </p>}
                </div>
                <Button><Link data-testid="returnToHomeLink" to='/'>Return to home</Link></Button>
          </div>
        </div>
      </div>
    </>
  );
}
