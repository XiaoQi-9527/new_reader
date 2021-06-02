import tkinter as tk
from tools.os_method import OsMethod
from tools.window_msthod import WindowMethod


def main():
    # 初始化
    root = tk.Tk()
    win = WindowMethod(root)
    # 设置大小
    win.set_size('400x100+100+100')
    # 设置窗口标题
    win.set_title(title='笔趣阁')
    # 设置图标
    win.set_icon(icon=None)
    # 设置窗口置顶
    win.set_top(top=True)
    # 禁止拉伸窗口
    win.set_no_stretching()
    # 获取默认背景色
    bg = "#%x%x%x" % root.winfo_rgb(root.cget('background'))

    # 判断当前设备系统平台
    os = OsMethod()
    sys = os.sys_name()

    if sys == "Mac":
        pass
    else:
        pass

    # 显示窗口
    root.mainloop()


if __name__ == '__main__':
    main()



