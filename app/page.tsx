"use client";

import { css } from "@emotion/react";
import DemoComponent from '@/components/DemoComponent';

export default function Home() {
  return (
    <div css={homeCss}>
      Hello, world!

      <DemoComponent />
    </div>
  );
}

const homeCss = css`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;

  max-width: 800px;
`;
