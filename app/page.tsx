"use client";

import React from 'react';
import { css } from "@emotion/react";
import DemoComponent from '@/components/DemoComponent';
import CoramInterview from './coram-interview';

export default function Home() {

  return (
    <div css={homeCss}>
      Hello, world!

      {/* <DemoComponent /> */}
      <CoramInterview />
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
