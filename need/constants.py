from enum import Enum
from need.utils.helper import Singleton


class SvtBusProtocol(Enum):
    READ_REQ_APPENDIX = 0x55
    READ_RSP_APPENDIX = 0xaa
    WRITE_REQ_APPENDIX = 0x66
    WRITE_REQ_SUCCESS = 0x88
    WRITE_REQ_FAIL = 0xaa
    WRITE_RSP_APPENDIX = 0x99
    FRAME_HEAD = b'<('
    FRAME_TAIL = b')>'


class Commands(Enum):
    DEVICE_ID = 0x0020 # 仪器ID
    SOFTWARE_VERSION = 0x0021 # 软件版本号
    SERIAL_BURDATE = 0x0022 # 串口波特率
    USE_DEFAULT_PARAM = 0x0023 # 恢复默认参数
    NETWORK_PORT_PARAM = 0x0024 # 网口参数
    CONNECTION_APPLY = 0x0025 # 设备请求入网
    NETWORK_DETECT = 0x0026 # 网络连接检测
    SWITCH_STATUS = 0x0330 # 开关量状态
    SLAVE_DEVICE_CONNECT = 0x0331 # 从设备连接参数
    ALARM_CODE = 0x0332 # 设备当前报警码
    TEMP_BOARD_CONTROL = 0x0333 # 温控板温度
    TEMP_BOARD_STATUS = 0x0334 # 温控板温控状态
    XYZ_MOTOR_DRIVE = 0x0335 # XYZ电机驱动
    AUXILIARY_REAGENT_MOTOR_DRIVE = 0x0336 # XYZ电机驱动
    TEMP_BOARD_MOTOR = 0x0337 # 温控板电机
    REAGENT_MESSAGE = 0x0338 # 试剂架试剂信息
    SLIDE_ON_STATUS = 0x0339 # 玻片在位信息
    MIX_REAGENT_MESSAGE = 0x033a # 混液区状态信息
    MIX_FORMULA_MESSAGE = 0x033b # 混液配方信息
    AUXILIARY_REAGENT_MESSAGE = 0x033c # 辅助试剂区信息
    CONTROL_TEMPLATE_MESSAGE = 0x033d # 质控模板信息
    MODULE_OPERATION_RECORD = 0x033e # 器件运行记录
    HEARTBEAT = 0x033f # 心跳包
    INJECTION_PUMP = 0X0340 # 注射泵
    CAMERA_CONTROL = 0X0341 # 相机控制
    REAGENT_FRONT_DOOR = 0x0342 # 试剂前舱门
    TEMP_CORRECT_COEFFICIENT = 0x0343 # 温度校正系数
    THREE_AXIS_BIAS_CORRECTION = 0x0344 # 三轴平台偏置修正参数
    FLIP_DOOR_UNLOCK = 0x0345 # 机器翻盖门解锁
    DEVICE_STATUS = 0x0350 # 仪器状态与工作流程状态
    FLOW_EDIT = 0x0351 # 流程编辑
    TAKE_PHOTO = 0x0352 # 拍摄照片上传
    FLOW_STEP_STATUS = 0x0353 # 流程状态
    SCAN_QUEUE = 0x0354 # 扫描列队
    SCAN_MESSAGE = 0x0355 # 扫码信息
    REAGENT_HOLDER_ONE_TYPE = 0x0356 # 试剂架1类型配置信息
    INJECTION_PUMP_EMPTY = 0x0357 # 注射泵排空
    LIQUID_LEVEL_DETECTION = 0x0358 # 试剂扫描液位检测使能开关
    NEEDLE_SOAKING_CLEAN = 0x0359 # 试剂针浸泡清洗

