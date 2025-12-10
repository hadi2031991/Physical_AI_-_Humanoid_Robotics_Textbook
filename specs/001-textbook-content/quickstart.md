# Quickstart: Physical AI & Humanoid Robotics Textbook Development

This guide will help you set up your local development environment and build the textbook.

## Prerequisites

- Node.js (LTS version recommended)
- npm or Yarn

## 1. Clone the Repository

```bash
git clone https://github.com/hadi2031991/ai-book
cd book-docusaurus-site
```

## 2. Install Dependencies

```bash
npm install # or yarn install
```

## 3. Start Local Development Server

```bash
npm start # or yarn start
```
This command starts a local development server and opens a browser window. Most changes are reflected live without restarting the server.

## 4. Build Static Content

To build the static HTML, CSS, and JavaScript files for production:

```bash
npm run build # or yarn build
```
The static content will be generated in the `build` directory.

## 5. Content Location

All textbook chapters and appendices are located in the `docs/` directory within the Docusaurus site.

```
book-docusaurus-site/
└── docs/
    ├── part1/
    │   └── ...
    └── appendices/
        └── ...
```

## 6. Deploy to GitHub Pages

The project is configured for deployment to GitHub Pages using GitHub Actions.

1.  **Ensure GitHub Pages is enabled for your repository.** Go to your repository settings on GitHub, navigate to "Pages", and select "GitHub Actions" as the source.
2.  **Push your changes to the `main` branch.** The `.github/workflows/deploy.yml` workflow will automatically trigger.
3.  **Monitor the workflow:** Check the "Actions" tab in your GitHub repository to see the deployment progress.
4.  **Access your site:** Once the workflow completes successfully, your Docusaurus site will be available at `https://hadi2031991.github.io/ai-book/book-docusaurus-site/`.

## Next Steps

- Begin generating content for chapters and appendices in the `docs/` directory.
- Refer to the `docusaurus.config.js` and `sidebars.js` for configuration and navigation details.
