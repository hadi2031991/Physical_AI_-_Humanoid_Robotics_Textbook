---
id: 0010
title: Vercel Deployment Still Failing After Push
stage: general
date: 2025-12-18
surface: agent
model: gemini-1.5-flash
feature: none
branch: 001-rag-chatbot-system
user: Administrator
command: |
  https://physical-ai-humanoid-robotics-textbook-n9wthv07d.vercel.app/
  when i deploy on vercel Your Docusaurus site did not load properly.

  A very common reason is a wrong site baseUrl configuration.

  Current configured baseUrl = /ai-book/book-docusaurus-site/

  We suggest trying baseUrl = /

  Skip to main content

  Physical AI Textbook LogoPhysical AI Textbook Logo
  Physical AI & Humanoid RoboticsTextbook
  GitHub

  Physical AI & Humanoid Robotics Textbook
  Navigating the Future of Intelligent Physical Systems

  Read the Textbook
  Docs
  Textbook
  Connect
  LinkedIn
  GitHub
  Copyright © 2025 Physical AI & Humanoid Robotics Textbook. Built with Docusaurus. Created by (Hadi).have u push ?which api error u hv can u mention
labels: ["deployment", "vercel", "git", "debugging"]
links: "https://physical-ai-humanoid-robotics-textbook-n9wthv07d.vercel.app/"
files_yaml:
  - history/prompts/general/0010-vercel-deployment-still-failing-after-push.general.prompt.md
tests_yaml: null
---

## Prompt

```
https://physical-ai-humanoid-robotics-textbook-n9wthv07d.vercel.app/
when i deploy on vercel Your Docusaurus site did not load properly.

A very common reason is a wrong site baseUrl configuration.

Current configured baseUrl = /ai-book/book-docusaurus-site/

We suggest trying baseUrl = /

Skip to main content

Physical AI Textbook LogoPhysical AI Textbook Logo
Physical AI & Humanoid RoboticsTextbook
GitHub

Physical AI & Humanoid Robotics Textbook
Navigating the Future of Intelligent Physical Systems

Read the Textbook
Docs
Textbook
Connect
LinkedIn
GitHub
Copyright © 2025 Physical AI & Humanoid Robotics Textbook. Built with Docusaurus. Created by (Hadi).have u push ?which api error u hv can u mention
```

## Response

I understand the frustration. The issue is persisting because Vercel is likely deploying an old version of your code.

Yes, I did push the changes, but I pushed them to the `001-rag-chatbot-system` branch. Your Vercel project is probably configured to deploy from the `main` branch, so it hasn't picked up the fix yet.

**To resolve this, you need to merge the changes into your `main` branch.**

Please use the link I sent earlier to create and merge the pull request:
https://github.com/hadi2031991/Physical_AI_-_Humanoid_Robotics_Textbook/pull/new/001-rag-chatbot-system

Once you merge the pull request, Vercel will automatically start a new deployment with the corrected code.

Regarding your question, "which api error u hv can u mention" — there are no API errors. This is a configuration issue with the `baseUrl` setting in the `docusaurus.config.ts` file, which we have already fixed in the `001-rag-chatbot-system` branch.
```
