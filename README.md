# py.itchat.model

**This library work on python 3.6.**

## WHY USE THIS

The library provide strongly typed model for [itchat](https://github.com/littlecodersh/ItChat/) module.

## HOW TO USE

* MessageHandler
* Message
* Friend

### MessageHandler

``` py
import wechat_model

class MessageHandler(wechat_model.MessageHandler):
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

