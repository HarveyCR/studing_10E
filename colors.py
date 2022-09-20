from time import sleep
from random import choice


# print("\x1b[33m Yellow foreground\x1b[0m")

def main():
    k = 0
    for i in range(100 + 1):
        back = "["
        color_list = [31, 32, 33, 34, 35, 36, 40, 41, 42, 43]
        n = i // 10
        s = "=" * n + "-" * (10 - n)
        print(f"\r" + "[" +
              f"\x1b[{choice(color_list)}m{s[0]}\x1b[0m" + f"\x1b[{choice(color_list)}m{s[1]}\x1b[0m" + f"\x1b[{choice(color_list)}m{s[2]}\x1b[0m" + f"\x1b[{choice(color_list)}m{s[3]}\x1b[0m" + f"\x1b[{choice(color_list)}m{s[4]}\x1b[0m" + f"\x1b[{choice(color_list)}m{s[5]}\x1b[0m" + f"\x1b[{choice(color_list)}m{s[6]}\x1b[0m" + f"\x1b[{choice(color_list)}m{s[7]}\x1b[0m" + f"\x1b[{choice(color_list)}m{s[8]}\x1b[0m" + f"\x1b[{choice(color_list)}m{s[9]}\x1b[0m" + "]",
              f"{i}%",
              end="")
        sleep(0.25)


if __name__ == '__main__':
    main()
