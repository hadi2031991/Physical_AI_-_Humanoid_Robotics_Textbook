---
id: 0003
title: Vercel Deployment URL Provided
stage: general
date: 2025-12-18
surface: agent
model: gemini-1.5-flash
feature: none
branch: null
user: Administrator
command: "https://physical-ai-humanoid-robotics-textb-dusky.vercel.app/#__docusaurus_skipToContent_fallback"
labels: ["deployment", "vercel", "docusaurus"]
links: "https://physical-ai-humanoid-robotics-textb-dusky.vercel.app/#__docusaurus_skipToContent_fallback"
files_yaml:
  - history/prompts/general/0003-vercel-deployment-url-provided.general.prompt.md
tests_yaml: null
---

## Prompt

```
https://physical-ai-humanoid-robotics-textb-dusky.vercel.app/#__docusaurus_skipToContent_fallback
```

## Response

Thank you for providing the URL. As suspected, the issue is with the `baseUrl` in your `docusaurus.config.ts`. It's currently set for GitHub Pages, but for Vercel, it should be set to `/`.

I'll now correct the `docusaurus.config.ts` file. I'll also update the `url` to your Vercel domain and remove the GitHub Pages-specific `organizationName` and `projectName` fields, as they are not needed for Vercel.
```
