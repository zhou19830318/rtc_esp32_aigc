'''
# 鉴权 AK/SK。前往 https://console.volcengine.com/iam/keymanage 获取
AK = "yzitS6Kx0x*****fo08eYmYMhuTu"
SK = "xZN65nz0CFZ******lWcAGsQPqmk"

# 实时音视频 App ID。前往 https://console.volcengine.com/rtc/listRTC 获取或创建
RTC_APP_ID = "678e1574*****b9389357"
# 实时音视频 APP KEY。前往 https://console.volcengine.com/rtc/listRTC 获取
RTC_APP_KEY = "dc7f8939d23*******bacf4a329"

# 大模型推理接入点 EndPointId 前往 https://console.volcengine.com/ark/region:ark+cn-beijing/endpoint?config=%7B%7D 创建
DEFAULT_BOT_ID = "ep-202******36-plsp5"
# 音频生成-语音合成 Voice_type，前往 https://console.volcengine.com/speech/service/8 获取
DEFAULT_VOICE_ID = "BV05******aming"

# 语音识别-流式语音识别 APPID 前往 https://console.volcengine.com/speech/service/16 获取
ASR_APP_ID = "274****256"
# 音频生成-语音合成 APPID，前往 https://console.volcengine.com/speech/service/8 获取
TTS_APP_ID = "274****256"

'''
SK = ""
AK = ""

RTC_APP_ID = ""
RTC_APP_KEY = ""

DEFAULT_BOT_ID = ""
DEFAULT_VOICE_ID = ""

ASR_APP_ID = ""
TTS_APP_ID = ""

# 音频配置参数
CHUNK = 1024      # 数据块大小
RATE = 16000      # 采样率
CHANNELS = 1      # 通道数
BIT_DEPTH = 16    # 位深度

# MIC I2S配置
MIC_SCK_PIN = 9       # I2S SCK引脚
MIC_WS_PIN = 8       # I2S WS引脚
MIC_SD_PIN = 7       # I2S SD引脚

# Speak I2S配置
SPK_SCK_PIN = 11       # I2S SCK引脚
SPK_WS_PIN = 12      # I2S WS引脚
SPK_SD_PIN = 10       # I2S SD引脚
