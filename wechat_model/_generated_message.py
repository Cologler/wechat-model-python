#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2017~2999 - cologler <skyoflw@gmail.com>
# ----------
#
# ----------


from ._base import _BaseModel

class _Generated(_BaseModel):
    @property
    def forward_flag(self):
        return self._get('ForwardFlag')
    @property
    def create_time(self):
        return self._get('CreateTime')
    @property
    def media_id(self):
        return self._get('MediaId')
    @property
    def msg_id(self):
        return self._get('MsgId')
    @property
    def status_notify_user_name(self):
        return self._get('StatusNotifyUserName')
    @property
    def file_size(self):
        return self._get('FileSize')
    @property
    def url(self):
        return self._get('Url')
    @property
    def img_height(self):
        return self._get('ImgHeight')
    @property
    def voice_length(self):
        return self._get('VoiceLength')
    @property
    def play_length(self):
        return self._get('PlayLength')
    @property
    def img_width(self):
        return self._get('ImgWidth')
    @property
    def status(self):
        return self._get('Status')
    @property
    def app_msg_type(self):
        return self._get('AppMsgType')
    @property
    def recommend_info(self):
        return self._get('RecommendInfo')
    @property
    def app_info(self):
        return self._get('AppInfo')
    @property
    def has_product_id(self):
        return self._get('HasProductId')
    @property
    def msg_type(self):
        return self._get('MsgType')
    @property
    def new_msg_id(self):
        return self._get('NewMsgId')
    @property
    def to_user_name(self):
        return self._get('ToUserName')
    @property
    def ori_content(self):
        return self._get('OriContent')
    @property
    def ticket(self):
        return self._get('Ticket')
    @property
    def type(self):
        return self._get('Type')
    @property
    def file_name(self):
        return self._get('FileName')
    @property
    def text(self):
        return self._get('Text')
    @property
    def sub_msg_type(self):
        return self._get('SubMsgType')
    @property
    def status_notify_code(self):
        return self._get('StatusNotifyCode')
    @property
    def img_status(self):
        return self._get('ImgStatus')
    @property
    def content(self):
        return self._get('Content')
    @property
    def from_user_name(self):
        return self._get('FromUserName')
