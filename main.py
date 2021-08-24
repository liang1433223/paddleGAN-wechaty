import os
import asyncio
import mix
from wechaty import (
    Contact,
    FileBox,
    Message,
    Wechaty,
    ScanStatus,
)

os.environ['WECHATY_PUPPET'] = "wechaty-puppet-service"
os.environ['WECHATY_PUPPET_SERVICE_TOKEN'] = "puppet_padlocal_baf612278bca466e88ff69a7c076601f"  # 这里填Wechaty token
os.environ['CUDA_VISIBLE_DEVICES'] = "0"
mix_flag = 0


async def on_message(msg: Message):
    global mix_flag

    if msg.text() == 'ding':
        await msg.say('这是自动回复: dong dong dong')

    if msg.text() == 'hi' or msg.text() == '你好':
        await msg.say('这是自动回复: 机器人目前的功能是\n'
                      '发送 "融合", 融合人脸，请根据提示完成操作进行人像融合\n'
                      )

    if msg.text() == '融合':
        mix_flag = 1
        if os.path.exists('image/first_image.png'):
            os.remove('image/first_image.png')
        if os.path.exists('image/second_image.png'):
            os.remove('image/second_image.png')
        await msg.say('请发送男生的照片')

    if mix_flag == 1 and msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
        mix_flag = 2
        # 将Message转换为FileBox
        file_box_user_image = await msg.to_file_box()
        # 获取图片名
        # img_name = file_box_user_image.name
        # 图片保存的路径
        img_path = './image/' + 'first_image.png'
        # 将图片保存为本地文件
        await file_box_user_image.to_file(file_path=img_path)
        mix.gan1()
        await msg.say('请发送女生的照片')

    if mix_flag == 2 and msg.type() == Message.Type.MESSAGE_TYPE_IMAGE:
        mix_flag = 3
        # 将Message转换为FileBox
        file_box_user_image = await msg.to_file_box()
        # 获取图片名
        # img_name = file_box_user_image.name
        # 图片保存的路径
        img_path = './image/' + 'second_image.png'
        # 将图片保存为本地文件
        await file_box_user_image.to_file(file_path=img_path)
        mix.gan2()
        await msg.say("收到，请问要生成男生还是女生，还是我都要")

    if mix_flag == 3 and (msg.text() == '男生' or msg.text() == '女生' or msg.text() == "我都要"):
        mix_flag = 4
        mix.mix_boy()
        mix.mix_girl()
        await msg.say('融合成功')

    if mix_flag == 4 and msg.text() == '男生':
        mix_flag = 0
        file_box = FileBox.from_file('mixoutput_boy/dst.mixing.png')
        await msg.say(file_box)

    if mix_flag == 4 and msg.text() == '女生':
        mix_flag = 0
        file_box = FileBox.from_file('mixoutput_girl/dst.mixing.png')
        await msg.say(file_box)

    if mix_flag == 4 and msg.text() == '我都要':
        mix_flag = 0
        file_box1 = FileBox.from_file('mixoutput_girl/dst.mixing.png')
        file_box = FileBox.from_file('mixoutput_boy/dst.mixing.png')
        await msg.say(file_box1)
        await msg.say(file_box)

async def on_scan(
        qrcode: str,
        status: ScanStatus,
        _data,
):
    print('Status: ' + str(status))
    print('View QR Code Online: https://wechaty.js.org/qrcode/' + qrcode)


async def on_login(user: Contact):
    print(user)


async def main():
    # 确保我们在环境变量中设置了WECHATY_PUPPET_SERVICE_TOKEN
    if 'WECHATY_PUPPET_SERVICE_TOKEN' not in os.environ:
        print('''
            Error: WECHATY_PUPPET_SERVICE_TOKEN is not found in the environment variables
            You need a TOKEN to run the Python Wechaty. Please goto our README for details
            https://github.com/wechaty/python-wechaty-getting-started/#wechaty_puppet_service_token
        ''')

    bot = Wechaty()

    bot.on('scan', on_scan)
    bot.on('login', on_login)
    bot.on('message', on_message)

    await bot.start()

    print('[Python Wechaty] Ding Dong Bot started.')


asyncio.run(main())
