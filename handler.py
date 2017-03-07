#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

import itchat as wc
import itchat.content as wcc

'''
NimbleText data:
TEXT       = 'Text'
MAP        = 'Map'
CARD       = 'Card'
NOTE       = 'Note'
SHARING    = 'Sharing'
PICTURE    = 'Picture'
RECORDING  = 'Recording'
ATTACHMENT = 'Attachment'
VIDEO      = 'Video'
FRIENDS    = 'Friends'
SYSTEM     = 'System'

NimbleText template for $0:
<% $0.trim() %>

NimbleText template for $1:
<% $1.toWords().replace(/[ ']/gm, '').toLowerCase() %>
'''

'''
NimbleText template (for methods):
    def on_<% $1.toWords().replace(/[ ']/gm, '').toLowerCase() %>(self, msg):
        pass
'''
class _BaseMessageHandler:
    # generated
    def on_text(self, msg):
        pass
    def on_map(self, msg):
        pass
    def on_card(self, msg):
        pass
    def on_note(self, msg):
        pass
    def on_sharing(self, msg):
        pass
    def on_picture(self, msg):
        pass
    def on_recording(self, msg):
        pass
    def on_attachment(self, msg):
        pass
    def on_video(self, msg):
        pass
    def on_friends(self, msg):
        pass
    def on_system(self, msg):
        pass
    # generated end

'''
NimbleText template (for methods):
    def on_<% $1.toWords().replace(/[ ']/gm, '').toLowerCase() %>(self, msg):
        self._parent.on_<% $1.toWords().replace(/[ ']/gm, '').toLowerCase() %>(msg)

NimbleText template (for register_handler):
        core.msg_register(wcc.<% $0.trim() %>, is_friend_chat, is_group_chat, is_mp_chat)(self.on_<% $1.toWords().replace(/[ ']/gm, '').toLowerCase() %>)
'''
class TypedMessageHandler:
    def __init__(self, parent):
        assert isinstance(parent, MessageHandler)
        self._parent = parent

    def register_handler(self, core: wc.Core, is_friend_chat, is_group_chat, is_mp_chat):
        # generated
        core.msg_register(wcc.TEXT, is_friend_chat, is_group_chat, is_mp_chat)(self.on_text)
        core.msg_register(wcc.MAP, is_friend_chat, is_group_chat, is_mp_chat)(self.on_map)
        core.msg_register(wcc.CARD, is_friend_chat, is_group_chat, is_mp_chat)(self.on_card)
        core.msg_register(wcc.NOTE, is_friend_chat, is_group_chat, is_mp_chat)(self.on_note)
        core.msg_register(wcc.SHARING, is_friend_chat, is_group_chat, is_mp_chat)(self.on_sharing)
        core.msg_register(wcc.PICTURE, is_friend_chat, is_group_chat, is_mp_chat)(self.on_picture)
        core.msg_register(wcc.RECORDING, is_friend_chat, is_group_chat, is_mp_chat)(self.on_recording)
        core.msg_register(wcc.ATTACHMENT, is_friend_chat, is_group_chat, is_mp_chat)(self.on_attachment)
        core.msg_register(wcc.VIDEO, is_friend_chat, is_group_chat, is_mp_chat)(self.on_video)
        core.msg_register(wcc.FRIENDS, is_friend_chat, is_group_chat, is_mp_chat)(self.on_friends)
        core.msg_register(wcc.SYSTEM, is_friend_chat, is_group_chat, is_mp_chat)(self.on_system)
        # generated end

    # generated
    def on_text(self, msg):
        self._parent.on_text(msg)
    def on_map(self, msg):
        self._parent.on_map(msg)
    def on_card(self, msg):
        self._parent.on_card(msg)
    def on_note(self, msg):
        self._parent.on_note(msg)
    def on_sharing(self, msg):
        self._parent.on_sharing(msg)
    def on_picture(self, msg):
        self._parent.on_picture(msg)
    def on_recording(self, msg):
        self._parent.on_recording(msg)
    def on_attachment(self, msg):
        self._parent.on_attachment(msg)
    def on_video(self, msg):
        self._parent.on_video(msg)
    def on_friends(self, msg):
        self._parent.on_friends(msg)
    def on_system(self, msg):
        self._parent.on_system(msg)
    # generated end

'''
NimbleText template (for methods):
    def on_<% $1.toWords().replace(/[ ']/gm, '').toLowerCase() %>(self, msg):
        self.on_any(msg)
'''
class MessageHandler(TypedMessageHandler):
    '''inherit to create your custom handler.'''
    def __init__(self, core: wc.Core):
        self._client = core
        self.friend_chat_handler.register_handler(core, True, False, False)
        self.group_chat_handler.register_handler(core, False, True, False)
        self.mp_chat_handler.register_handler(core, False, False, True)

    @property
    def friend_chat_handler(self) -> TypedMessageHandler:
        '''overwrite to create your custom handler.'''
        return TypedMessageHandler(self)

    @property
    def group_chat_handler(self) -> TypedMessageHandler:
        '''overwrite to create your custom handler.'''
        return TypedMessageHandler(self)

    @property
    def mp_chat_handler(self) -> TypedMessageHandler:
        '''overwrite to create your custom handler.'''
        return TypedMessageHandler(self)

    def on_any(self, msg):
        pass

    # generated
    def on_text(self, msg):
        self.on_any(msg)
    def on_map(self, msg):
        self.on_any(msg)
    def on_card(self, msg):
        self.on_any(msg)
    def on_note(self, msg):
        self.on_any(msg)
    def on_sharing(self, msg):
        self.on_any(msg)
    def on_picture(self, msg):
        self.on_any(msg)
    def on_recording(self, msg):
        self.on_any(msg)
    def on_attachment(self, msg):
        self.on_any(msg)
    def on_video(self, msg):
        self.on_any(msg)
    def on_friends(self, msg):
        self.on_any(msg)
    def on_system(self, msg):
        self.on_any(msg)
    # generated end
