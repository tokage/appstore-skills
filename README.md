# App Store Listing Skills

This repository contains a collection of AI-powered "Skills" designed to automate and streamline the process of creating assets and metadata for apple App Store submissions.

These are standard agent skills that can be used by AI tools that support the [Agent Skills](https://agentskills.io).

## Available Skills

### 1. [App Store Screenshot Generator](./appstore-screenshot-generator)

Create professional, App Store-compliant marketing screenshots in minutes.

**Key Features:**
*   **Auto-Device Detection**: Automatically identifies device models from screenshot dimensions.
*   **Professional Compositing**: Places your raw screenshots into realistic device bezels.
*   **Customizable Styling**: Support for gradient backgrounds, text overlays (titles & taglines), and various bezel colors.
*   **Batch Processing**: Generate an entire set of marketing images from a simple JSON configuration.
*   **Compliance**: Ensures output matches strict App Store dimension requirements.

[View Documentation & Usage](./appstore-screenshot-generator/SKILL.md)

### 2. [App Store Listing Generator](./appstore-listing-generator)

Generate optimized App Store metadata (ASO) by analyzing your project's code and documentation.

**Key Features:**
*   **Context Aware**: Analyzes your PRD, README, and source code to understand your app's value proposition.
*   **ASO Optimization**: Suggests keywords and descriptions tailored for search visibility.
*   **Comprehensive Output**: Generates App Name, Subtitle, Promotional Text, Description, Keywords, and potentially What's New text.
*   **Localization Friendly**: Provides guidelines for adapting content to different markets.

[View Documentation & Usage](./appstore-listing-generator/SKILL.md)

## License

This project is licensed under the terms of the [MIT License](LICENSE).
