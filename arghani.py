from burp import IBurpExtender
from burp import IMessageEditorTabFactory
from burp import IMessageEditorTab
from javax.swing import JPanel, BoxLayout
from javax.swing import JButton
from java.awt import Component
from javax.swing import SwingWorker
import java
from burp import IBurpExtender
from burp import IMessageEditorTabFactory
from burp import IMessageEditorTab
from javax.swing import JPanel, BoxLayout
from javax.swing import JButton
from java.awt import Component

class BurpExtender(IBurpExtender, IMessageEditorTabFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()
        
        # Set the extension name
        callbacks.setExtensionName("Arghani")

        # Register the custom message editor tab factory
        callbacks.registerMessageEditorTabFactory(self)

    def createNewInstance(self, controller, editable):
        return CustomRequestEditorTab(self, controller, editable)

class CustomRequestEditorTab(IMessageEditorTab):
    def __init__(self, extender, controller, editable):
        self._extender = extender
        self._helpers = extender._helpers
        self._controller = controller
        self._editable = editable

        # Create the message editor component
        self._txtInput = extender._callbacks.createTextEditor()
        self._txtInput.setEditable(True)  # Set to True to enable editing

        # Create the Send button
        self._sendButton = JButton("Send", actionPerformed=self.send_edited_request)

        # Create a JPanel to hold the text editor and the Send button
        self._panel = JPanel()
        self._panel.setLayout(BoxLayout(self._panel, BoxLayout.Y_AXIS))
        self._panel.add(self._txtInput.getComponent())
        self._panel.add(self._sendButton)

    def send_edited_request(self, event):
        # Get the edited request from the text editor
        edited_request_bytes = self._txtInput.getText()

        # Send the edited request directly using the IHttpService from the current message
        http_service = self._controller.getHttpService()
        worker = HttpRequestWorker(self._extender, http_service, edited_request_bytes)
        worker.start()

    def getTabCaption(self):
        return "Arghani"

    def getUiComponent(self):
        return self._panel

    def isEnabled(self, content, isRequest):
        # Enable the custom tab for requests only
        return isRequest

    def setMessage(self, content, isRequest):
        if content is None:
            # Clear the display if the content is None
            self._txtInput.setText(None)
        else:
            # Set the content in the custom tab
            self._txtInput.setText(content)

    def getMessage(self):
        return self._txtInput.getText()

    def isModified(self):
        return self._txtInput.isTextModified()

    def getSelectedData(self):
        return self._txtInput.getSelectedText()

class HttpRequestWorker(java.lang.Thread):
    def __init__(self, extender, http_service, request_bytes):
        self._extender = extender
        self._http_service = http_service
        self._request_bytes = request_bytes
        super(HttpRequestWorker, self).__init__()

    def run(self):
        self._extender._callbacks.makeHttpRequest(self._http_service, self._request_bytes)

    def doInBackground(self):
        self._extender._callbacks.makeHttpRequest(self._http_service, self._request_bytes)

    def done(self):
        pass
