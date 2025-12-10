import type {SidebarsConfig} from '@docusaurus/plugin-content-docs';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.
 */
const sidebars: SidebarsConfig = {
  // By default, Docusaurus generates a sidebar from the docs folder structure
  tutorialSidebar: [
    {
      type: 'category',
      label: 'Foundations of Physical AI',
      items: [
        'part1/ch1',
        'part1/ch2',
        'part1/ch3',
        'part1/ch4',
      ],
    },
    {
      type: 'category',
      label: 'Intelligence for Robots',
      items: [
        'part2/ch5',
        'part2/ch6',
        'part2/ch7',
        'part2/ch8',
      ],
    },
    {
      type: 'category',
      label: 'Building & Programming Humanoids',
      items: [
        'part3/ch9',
        'part3/ch10',
        'part3/ch11',
        'part3/ch12',
      ],
    },
    {
      type: 'category',
      label: 'Future of Work',
      items: [
        'part4/ch13',
        'part4/ch14',
      ],
    },
    {
      type: 'category',
      label: 'Appendices',
      items: [
        'appendices/math',
        'appendices/ros2',
        'appendices/simulation-tools',
      ],
    },
  ],

  // But you can create a sidebar manually
  /*
  tutorialSidebar: [
    'intro',
    'hello',
    {
      type: 'category',
      label: 'Tutorial',
      items: ['tutorial-basics/create-a-document'],
    },
  ],
   */
};

export default sidebars;
