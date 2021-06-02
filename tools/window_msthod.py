# from source.all import get_book, get_one_chapter
# import json


class WindowMethod:
    def __init__(self, window):
        """
        :param window: 窗口对象
        """
        self.window = window

    def set_size(self, size):
        """
        设置窗口大小 (长, 宽), 位置 (左上角顶点)
        :param size: '600x200+274+182'
        """
        self.window.geometry(size)

    def set_title(self, title="阅读"):
        """设置窗口标题"""
        self.window.title(title)

    def set_icon(self, icon=None):
        """设置窗口图标"""
        icon = './icons/bqg.ico' if icon is None else icon
        self.window.iconbitmap(icon)

    def set_top(self, top=False):
        """窗口置顶"""
        self.window.wm_attributes('-topmost', top)

    def set_no_stretching(self):
        """禁止拉伸窗口"""
        self.window.resizable(width=False, height=False)


