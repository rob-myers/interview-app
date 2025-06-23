"use client";

import React from 'react';
import { css } from "@emotion/react";
import DemoComponent from '@/components/DemoComponent';

const testWalls: Wall[] = [
  [[0,0],[0,1],[1,0],[1,1]],
  [[1,1],[0,1],[0,0],[1,0]],
  [[0,0],[0,1]],
  [[0,0],[1,1]],
  [[0,0],[0,1],[1,0]],
  [[0,0],[0,1],[0,1],[1,1]],
];

export default function CoramInterview() {

  return (
    <div css={coramInterviewCss}>
      <div className='walls'>
        {testWalls.map((wall, i) =>
          <div key={i} className="wall">
            <div>{JSON.stringify(wall)}</div>
            <div>{wallIsValid(wall) ? 'true' : 'false'}</div>
          </div>
        )}
      </div>

      {/* <DemoComponent /> */}
    </div>
  );
}

const coramInterviewCss = css`

  .walls {
    background-color: #000;
    padding: 16px;
    font-size: 40px;
  }
  .wall {
    display: flex;
    gap: 8px;
  }
`;

type Tile = [number, number];
type Wall = Tile[];

function wallIsValid(wall: Wall): boolean {
  if (wall.length === 0) {
    return false;
  }
  
  const width = Math.max(...wall.map(([x, _y]) => x)) + 1;
  const height = Math.max(...wall.map(([_x, y]) => y)) + 1;
  // (i, j) s.t. 0 ≤ i < width, 0 ≤ j < height
  const set = new Set(wall.map(([x, y]) => `${x},${y}`));
  
  console.log({ wall, width, height, set });
  if (
    wall.length === width * height
    && set.size === width * height
  ) {
    return true;
  } else {
    return false;
  }
}
