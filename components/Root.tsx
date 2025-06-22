"use client";

import { QueryClientProvider } from "@tanstack/react-query";
import { ReactQueryDevtools } from "@tanstack/react-query-devtools";
import { css } from "@emotion/react";
import { queryClient } from './query-client';

export default function Root({ children }: React.PropsWithChildren) {
  return (
    <QueryClientProvider client={queryClient}>
      <div
        css={rootCss}
        data-testid="root"
      >
        {children}
      </div>
      <ReactQueryDevtools
        initialIsOpen={false}
        buttonPosition="bottom-right"
      />
      </QueryClientProvider>
  );
}

const rootCss = css`
  background-color: #444;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
`;
