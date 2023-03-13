import "@/styles/globals.css";
import { queryClient } from "@/utils/queryClient";
import type { AppProps } from "next/app";
import { Passion_One } from "next/font/google";
import { QueryClientProvider } from "react-query";
import { ReactQueryDevtools } from "react-query/devtools";

const passionOne = Passion_One({ weight: ["400", "700"], subsets: ["latin"] });

export default function App({ Component, pageProps }: AppProps) {
  return (
    <QueryClientProvider client={queryClient} contextSharing>
      <ReactQueryDevtools initialIsOpen={false} />
      <main>
        <style jsx global>{`
          html {
            font-family: ${passionOne.style.fontFamily};
            --font-family: ${passionOne.style.fontFamily};
          }
        `}</style>
        <Component {...pageProps} />
      </main>
    </QueryClientProvider>
  );
}
