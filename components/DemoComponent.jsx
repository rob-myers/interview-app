import Carousel from './Carousel';

import ExampleImage1 from '../public/images/desktop-empty-world__20250612.webp';
import ExampleImage2 from '../public/images/many-robs-test.webp';
import ExampleImage3 from '../public/images/desktop-empty-world__20250612.webp';

export default function DemoComponent() {
  return (
    <Carousel
      items={[
        {
          img: ExampleImage1,
          label: <>Our system <em>NPC CLI</em> is built into this site.</>,
          objectPosition: '0% 50%',
        },
        {
          img: ExampleImage2,
          label: <>Our system <em>NPC CLI</em> is built into this site.</>,
          objectPosition: '0% 75%',
        },
        {
          img: ExampleImage3,
          label: <>CLI stands for <em>Command Line Interface.</em></>,
          objectPosition: '0% 70%',
        },
      ]}
      filter="brightness(1.0)"
      maxHeight={600}
      minHeight={400}
    />
  );
}

