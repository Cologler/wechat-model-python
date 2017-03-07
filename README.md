# py.itchat.model

## How TO USE

The library provide wrappers:

* MessageHandler
* Message
* Friend

### MessageHandler

``` py
import itchat_model

class MessageHandler(itchat_model.MessageHandler):
    # overwrite any of on_method() you want, like:
    def on_text(self, msg):
        m = Message(msg)
        if self._client.storageClass.userName == m.from_user_name:
            return
        return 'go to hell.'

# then call before itchat run.
CLIENT = itchat.originInstance
MessageHandler(CLIENT)
CLIENT.run()
```

For more API, please read the source code.

### Message

``` py
def on_text(self, msg):
    m = Message(msg)
```

### Friend

``` py
friend = Friend(CLIENT.search_friends())
```

