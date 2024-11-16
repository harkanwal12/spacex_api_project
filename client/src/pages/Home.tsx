const Home = () => {
  return (
    <>
      <div className="w-[40vw] min-h-[70vh] items-center inline-flex justify-center">
        <div className="flex-col justify-center items-center text-center gap-1.5 inline-flex">
            <div className="w-100 text-primary text-5xl font-bold uppercase ">SpaceX API Client</div>
            <div className="text-center text-muted-foreground text-lg font-medium mt-8">
              <p>
                Welcome to the unofficial SpaceX API Client, which serves as a front-end for the Open Source 
                REST API for launch and launch site data
              </p>
            </div>
            <div>
            <p className="italic text-center text-muted-foreground text-base font-medium mt-8">
              This website or its associated Python Wrapper Module are not affiliated, associated, authorized, endorsed by, or in any way officially connected with Space 
              Exploration Technologies Corp (SpaceX), or any of its subsidiaries or its affiliates. 
              The names SpaceX as well as related names, marks, emblems and images are registered trademarks of their respective owners.
            </p>
            </div>
        </div>
      </div>
    </>
  )
}

export default Home