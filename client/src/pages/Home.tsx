import { Link } from 'react-router-dom'

const Home = () => {
  return (
    <>
      <div className="text-white w-[50vw] min-h-[70vh] items-center inline-flex justify-center">
        <div className="flex-col items-center">
          <div className="flex-col justify-center items-center text-center gap-1 inline-flex">
            <div className="w-100 text-primary text-5xl font-bold uppercase ">SpaceX API Client</div>
                <div className="text-center text-muted-foreground text-lg mt-2">
                  <p>
                    Welcome to the unofficial SpaceX API Client, which serves as a front-end for the Open Source 
                    REST API for launch and launch site data
                  </p>
                </div>
          </div>
          <div className="flex justify-center gap-5 p-5">
            <Link to={'/launches'} className="box">
              <div className="gap-2">
                <h2 className="font-bold text-lg">Launches</h2>
                <p>Explore the history of SpaceX launches, organized by year.</p>
              </div>
            </Link>
            <Link to={'/launchsites'} className="box">
              <div className="flex-col gap-2">
                <h2 className="font-bold text-lg">Launch Sites</h2>
                <p>Discover launch site history, and their launches.</p>
              </div>
            </Link>
          </div>
        </div>
      </div>
    </>
  )
}

export default Home