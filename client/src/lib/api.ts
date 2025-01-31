import axios, { AxiosInstance } from 'axios';

const host = window.location.hostname

export class ApiClient {
    axiosInstance: AxiosInstance
    constructor(baseURL = import.meta.env.MODE === 'production' ? "https://"+ host +"/api/" : "http://"+ host + ":5000/api/") {
      this.axiosInstance = axios.create({
        baseURL: baseURL
      });
    }
  
    async getAllLaunchpadNames() {
      const endpoint = encodeURI("get_all_launchpad_names")
      try {
        const response = await this.axiosInstance.get(endpoint)
        return response.data;
      } catch (error) {
        console.error('getAllLaunchpadNames Error: ', error);
        throw error;
      }
    }

    async getAllUniqueLaunchYears() {
      const endpoint = encodeURI("get_all_launch_years")
      try {
        const response = await this.axiosInstance.get(endpoint)
        return response.data;
      } catch (error) {
        console.error('getAllUniqueLaunchYears Error: ', error);
        throw error;
      }
    }

    async getAllLaunchesInYear(year:string) {
      const endpoint = encodeURI(`/${year}/get_all_launches_in_year`)
      try {
        const response = await this.axiosInstance.get(endpoint)
        return response.data;
      } catch (error) {
        console.error('getAllLaunchesInYear Error: ', error);
        throw error;
      }
    }

    async getLaunchpadWithLaunches(id:string, shortname:string) {
        const endpoint = encodeURI(`${id}/${shortname}/get_launchpad_with_launches`)
        try {
          const response = await this.axiosInstance.get(endpoint)
          return response.data;
        } catch (error) {
          console.error('getLaunchpadWithLaunches Error: ', error);
          throw error;
        }
      }
  }