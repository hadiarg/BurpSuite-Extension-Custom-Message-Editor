# Arghani - Custom Message Editor Tab with Send Button

## Description
Arghani is a Burp Suite extension that adds a custom message editor tab with a
"Send" button, allowing users to edit and send HTTP requests directly from the
custom tab.

## Features
- Custom message editor tab for HTTP requests
- Editable request content
- Send button to send the modified request directly from the custom tab

## Installation

1. Ensure you have Burp Suite Professional installed and running.
2. Go to "Extender" > "Extensions" > "Add".
3. Choose "Python" as the extension type.
4. Load the `arghani.py` file containing the extension code.
5. Click "Next" to finish the installation.

## Usage

1. After installing the extension, navigate to the "Proxy" > "HTTP history" tab
   in Burp Suite.
2. Click on any request to view its details.
3. You should see a new tab called "My Custom Tab". Click on it.
4. Edit the request in the custom tab as needed.
5. Click the "Send" button in the custom tab to send the modified request.
6. The response will be visible in the "Response" section of the request details.

## Code Overview

The extension code is organized into the following classes:

- `BurpExtender`: Implements the `IBurpExtender` and `IMessageEditorTabFactory`
  interfaces, sets the extension name, and registers the custom message editor
  tab factory.
- `CustomRequestEditorTab`: Implements the `IMessageEditorTab` interface,
  creates the custom message editor tab UI, and handles request editing and
  sending.
- `HttpRequestWorker`: Extends `java.lang.Thread` to send the modified request
  in a separate thread.

## Contributing

We welcome contributions to improve and extend the functionality of Arghani.
Please submit a pull request or open an issue to propose changes or report bugs.
