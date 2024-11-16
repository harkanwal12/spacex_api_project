import axios, { AxiosInstance } from 'axios';

const host = window.location.hostname

export class ApiClient {
    axiosInstance: AxiosInstance
    constructor(baseURL = import.meta.env.MODE === 'production' ? "https://"+ host +"/launches/" : "http://"+ host + ":5555/launches/") {
      this.axiosInstance = axios.create({
        baseURL: baseURL
      });
    }
  
    async getAllLaunches() {
      const endpoint = encodeURI("get_all_launches")
      try {
        const response = await this.axiosInstance.get(endpoint)
        return response.data;
      } catch (error) {
        console.error('getAllProgs Error: ', error);
        throw error;
      }
    }

    async getAllLaunchpadsWithLaunches() {
        const endpoint = encodeURI("get_all_launchpads_with_launches")
        try {
          const response = await this.axiosInstance.get(endpoint)
          return response.data;
        } catch (error) {
          console.error('getAllLaunchpadsWithLaunches Error: ', error);
          throw error;
        }
      }
  }