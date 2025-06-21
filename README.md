# Gignancing

This project contains a web and mobile app built with React and Expo. Follow these steps to get it running on your computer or phone.

## Requirements

- **Node.js** (download from [nodejs.org](https://nodejs.org)).
- **Git** (or download the repository as a ZIP file).
- **Expo Go** app on your iPhone or Android phone (free from the app store).

## Setup

1. If you downloaded a ZIP, extract it to a folder of your choice. Otherwise clone the repo with Git.
2. Open a terminal (Command Prompt on Windows, Terminal on macOS/Linux).
3. Navigate to the project folder, for example:
   ```bash
   cd path/to/gignancing
   ```
4. Install dependencies:
   ```bash
   npm install
   ```
   The install step also installs the mobile app dependencies automatically.

## Running the App

### Mobile (Expo)

1. Start the Expo development server:
   ```bash
   npm start
   ```
2. A QR code will appear in the terminal or browser. Open the Expo Go app on your phone and scan the code to launch the mobile app.

### Web Version

Run the web build in your browser with:
```bash
npm run web
```
This opens the app at `http://localhost:19006`.

## Building for Deployment

To create a production build (for example for Vercel), run:
```bash
npm run build
```
The output will be in the `dist` folder.

## Running Tests

If you want to run the automated tests:
```bash
npm test
```

That's it! You can now explore the project and start developing.
