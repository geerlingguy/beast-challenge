import axios, { AxiosInstance, AxiosRequestConfig } from "axios";

const baseURL = process.env.NEXT_PUBLIC_API_URL;

class axiosInstance {
  instance: AxiosInstance;

  constructor() {
    this.instance = axios.create({
      baseURL,
      timeout: 30000,
      headers: {
        "Content-Type": "application/json",
      },
    });
  }

  getRequest = (
    url: string,
    params: unknown = {},
    other?: AxiosRequestConfig
  ) => {
    return this.instance
      .get(url, { ...other, params })
      .then(({ data }) => data)
      .catch((err) => {
        throw err;
      });
  };

  postRequest = (url: string, body?: unknown, other?: AxiosRequestConfig) => {
    return this.instance
      .post(url, body, other)
      .then(({ data }) => data)
      .catch((err) => {
        throw err;
      });
  };

  updateRequest = (url: string, body?: unknown, other?: AxiosRequestConfig) => {
    return this.instance
      .put(url, body, other)
      .then(({ data }) => data)
      .catch((err) => {
        throw err;
      });
  };

  deleteRequest = (url: string, body?: unknown, other?: AxiosRequestConfig) => {
    return this.instance
      .delete(url, { ...other, data: body })
      .then(({ data }) => data)
      .catch((err) => {
        throw err;
      });
  };
}

const apiRequest = new axiosInstance();

export default apiRequest;
