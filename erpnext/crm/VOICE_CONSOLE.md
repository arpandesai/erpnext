# Voice Console Integration

ERPNext CRM can be controlled using voice commands via the
[`openai-realtime-console`](https://github.com/openai/openai-realtime-console)
package. This optional feature allows you to interact with your CRM data hands
free.

## Setup

1. Install the dependency:
   ```bash
   pip install openai-realtime-console
   ```
2. Start the voice console from within ERPNext:
   ```python
   from erpnext.crm.voice_console import start_voice_console
   start_voice_console()
   ```

The console will listen for voice input and translate recognised commands into
CRM actions.
