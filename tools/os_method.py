import os


class OsMethod:
    def __init__(self):
        self.os = os

    def sys_name(self):
        """
        获取系统名称
        :return: nt(Windows) | posix(Linux)
        """
        return "Mac" if self.os.name == "posix" else "Win"

    def run_cmd(self, cmd):
        """
        执行 shell 命令
        :param cmd: 命令
        :return: 0(成功) | 1(失败)
        """
        return True if self.os.system(cmd) == 0 else False


if __name__ == '__main__':
    o = OsMethod()
    print(o.sys_name())
    # print(o.run_cmd("docker ps -a"))
    # print(o.run_cmd("exa -hHlF"))
