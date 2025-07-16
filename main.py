# 彩色输出（仅部分终端支持）
print("\033[1;32mHello, World! (绿色)\033[0m")

# 带表情
print("Hello, World! 😊🌍")

# 不同语言
print("你好，世界！")
print("こんにちは世界！")
print("¡Hola Mundo!")
print("Bonjour le monde!")

# 装饰边框
print("*" * 30)
print("*{:^28}*".format("Hello, World!"))
print("*" * 30)

# 反转输出
print("!dlroW ,olleH"[::-1])

# 大写花体
print("HELLO, WORLD!!!")

# 彩虹色（简单模拟）
rainbow = ['\033[91m','\033[93m','\033[92m','\033[96m','\033[94m','\033[95m']
text = "Hello, World!"
colored = ''.join(rainbow[i%len(rainbow)] + c for i, c in enumerate(text)) + '\033[0m'
print(colored)
