---
id: 0005
title: User Confirms baseUrl Issue
stage: general
date: 2025-12-18
surface: agent
model: gemini-1.5-flash
feature: none
branch: null
user: Administrator
command: |
  Your Docusaurus site did not load properly.

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
  GitHub the link of deploy is this https://physical-ai-humanoid-robotics-textb-dusky.vercel.app/ kindly resolved this issue
labels: ["deployment", "vercel", "docusaurus", "confirmation"]
links: "https://physical-ai-humanoid-robotics-textb-dusky.vercel.app/"
files_yaml:
  - history/prompts/general/0005-user-confirms-baseurl-issue.general.prompt.md
tests_yaml: null
---

## Prompt

```
Your Docusaurus site did not load properly.

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
GitHub the link of deploy is this https://physical-ai-humanoid-robotics-textb-dusky.vercel.app/ kindly resolved this issue
```

## Response

Thank you for the confirmation. The error you're seeing is the one I identified earlier.

I have already corrected the `docusaurus.config.ts` file to fix this. You now need to commit this change and push it to your GitHub repository. This will trigger a new deployment on Vercel with the corrected configuration.

Please let me know if you need assistance with committing and pushing the change.
```
