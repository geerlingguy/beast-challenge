import { QueryClient } from 'react-query';

// Access the key, status and page variables in your query function!
export const queryClient = new QueryClient({
  defaultOptions: { queries: { refetchOnWindowFocus: false } },
});
