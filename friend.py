#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2016 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------

from ._core import _BaseModel

class _Generated(_BaseModel):
    @property
    def city(self):
        return self._get('City')

    @property
    def province(self):
        return self._get('Province')

    @property
    def remark_pyinitial(self):
        return self._get('RemarkPYInitial')

    @property
    def star_friend(self):
        return self._get('StarFriend')

    @property
    def user_name(self):
        return self._get('UserName')

    @property
    def display_name(self):
        return self._get('DisplayName')

    @property
    def app_account_flag(self):
        return self._get('AppAccountFlag')

    @property
    def hide_input_bar_flag(self):
        return self._get('HideInputBarFlag')

    @property
    def member_count(self):
        return self._get('MemberCount')

    @property
    def contact_flag(self):
        return self._get('ContactFlag')

    @property
    def encry_chat_room_id(self):
        return self._get('EncryChatRoomId')

    @property
    def head_img_flag(self):
        return self._get('HeadImgFlag')

    @property
    def statues(self):
        return self._get('Statues')

    @property
    def owner_uin(self):
        return self._get('OwnerUin')

    @property
    def alias(self):
        return self._get('Alias')

    @property
    def key_word(self):
        return self._get('KeyWord')

    @property
    def signature(self):
        return self._get('Signature')

    @property
    def chat_room_id(self):
        return self._get('ChatRoomId')

    @property
    def sex(self):
        return self._get('Sex')

    @property
    def remark_name(self):
        return self._get('RemarkName')

    @property
    def is_owner(self):
        return self._get('IsOwner')

    @property
    def uin(self):
        return self._get('Uin')

    @property
    def nick_name(self):
        return self._get('NickName')

    @property
    def attr_status(self):
        return self._get('AttrStatus')

    @property
    def pyinitial(self):
        return self._get('PYInitial')

    @property
    def uni_friend(self):
        return self._get('UniFriend')

    @property
    def member_list(self):
        return self._get('MemberList')

    @property
    def pyquan_pin(self):
        return self._get('PYQuanPin')

    @property
    def head_img_url(self):
        return self._get('HeadImgUrl')

    @property
    def web_wx_plugin_switch(self):
        return self._get('WebWxPluginSwitch')

    @property
    def remark_pyquan_pin(self):
        return self._get('RemarkPYQuanPin')

    @property
    def sns_flag(self):
        return self._get('SnsFlag')

    @property
    def verify_flag(self):
        return self._get('VerifyFlag')

class Friend(_Generated):
    pass
