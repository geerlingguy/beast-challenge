import { useQuery, UseQueryOptions, QueryFunctionContext } from "react-query";
import apiRequest from "../utils/apiRequest";

const twentyFourHoursInMs = 1000 * 60 * 60 * 24;

export function queryFetcher({ queryKey }: QueryFunctionContext) {
  const [url, params] = queryKey as [string, unknown];
  return apiRequest.getRequest(url, {
    ...Object.assign({}, params),
  });
}

export function useBaseQuery<T>(
  url: string,
  params?: unknown,
  options?: UseQueryOptions<T>
) {
  const key: any = [url];
  if (params) {
    key.push(params);
  }
  return useQuery<T>({
    queryKey: key,
    queryFn: queryFetcher,
    useErrorBoundary: false,
    refetchOnWindowFocus: false,
    refetchOnReconnect: false,
    refetchOnMount: false,
    retry: false,
    staleTime: twentyFourHoursInMs,
    ...options,
  });
}
