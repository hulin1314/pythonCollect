"""
前景色	背景色	颜色
 30	     40	    黑色
 31	     41	    红色
 32	     42	    绿色
 33	     43	    黃色
 34	     44	    蓝色
 35	     45	    紫红色
 36	     46	    青蓝色
 37	     47	    白色

显示方式	意义
 0	    终端默认设置
 1	    高亮显示
 4	    使用下划线
 5	    闪烁
 7	    反白显示
 8	    不可见
"""
# 前景色
ANSI_BLACK = 30
ANSI_RED = 31
ANSI_GREEN = 32
ANSI_YELLOW = 33
ANSI_BLUE = 34
ANSI_PURPLE = 35
ANSI_CYAN = 36
ANSI_WHITE = 37
# 背景色
ANSI_BLACK_BACKGROUND = 40
ANSI_RED_BACKGROUND = 41
ANSI_GREEN_BACKGROUND = 42
ANSI_YELLOW_BACKGROUND = 43
ANSI_BLUE_BACKGROUND = 44
ANSI_PURPLE_BACKGROUND = 45
ANSI_CYAN_BACKGROUND = 46
ANSI_WHITE_BACKGROUND = 47
# 显示方式
MOD_DEFAULT = 0
MOD_HIGHLIGHT = 1
MOD_UNDERLINE = 4
MOD_FLICKER = 5
MOD_INVERSE = 7
MOD_HIDE = 8


def mod_print(message, fg=ANSI_WHITE, bg=ANSI_BLACK_BACKGROUND, mod=MOD_DEFAULT):
    """
    格式化输出
    :param message: 输出的消息
    :param fg: 前景色
    :param bg: 背景色
    :param mod: 打印格式模式
    :return:
    """
    print('\033[{};{};{}m'.format(fg, bg, mod) + message + '\033[0m')
