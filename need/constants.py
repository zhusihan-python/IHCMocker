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


class HeartbeatStatus(Enum):
    DEVICE_NOT_RESET = 0x00
    DEVICE_RESET_DONE = 0x01
    THREE_AXIS_NOT_RESET = 0x00
    THREE_AXIS_RESETTING = 0x01
    THREE_AXIS_RESET_SUCCESS = 0x11
    THREE_AXIS_RESET_FAIL = 0x21
    THREE_AXIS_REAGENT_SCANNING = 0x02
    THREE_AXIS_REAGENT_SCAN_SUCCESS = 0x12
    THREE_AXIS_REAGENT_SCAN_FAIL = 0x22
    THREE_AXIS_SLIDE_SCANNING = 0x03
    THREE_AXIS_SLIDE_SCAN_SUCCESS = 0x13
    THREE_AXIS_SLIDE_SCAN_FAIL = 0x23
    THREE_AXIS_STEREO_SCANNING = 0x04
    THREE_AXIS_STEREO_SCAN_SUCCESS  = 0x14
    THREE_AXIS_STEREO_SCAN_FAIL = 0x24
    THREE_AXIS_MIXING = 0x05
    THREE_AXIS_MIX_SUCCESS = 0x15
    THREE_AXIS_MIX_FAIL = 0x25
    THREE_AXIS_DRIPPING = 0x06
    THREE_AXIS_DRIP_SUCCESS = 0x16
    THREE_AXIS_DRIP_FAIL = 0x26
    THREE_AXIS_NEEDLE_CLEANING = 0x07
    THREE_AXIS_NEEDLE_CLEAN_SUCCESS = 0x17
    THREE_AXIS_NEEDLE_CLEAN_FAIL = 0x27
    THREE_AXIS_MIX_CLEANING = 0x08
    THREE_AXIS_MIX_CLEAN_SUCCESS = 0x18
    THREE_AXIS_MIX_CLEAN_FAIL = 0x28
    REAGENT_DOOR_NOT_RESET = 0x00
    REAGENT_DOOR_RESETTING = 0x01
    REAGENT_DOOR_RESET_SUCCESS = 0x11
    REAGENT_DOOR_RESET_FAIL = 0x21
    REAGENT_DOOR_OPENNING = 0x02
    REAGENT_DOOR_OPEN_SUCCESS = 0x12
    REAGENT_DOOR_OPEN_FAIL = 0x22
    REAGENT_DOOR_CLOSING = 0x03
    REAGENT_DOOR_CLOSE_SUCCESS = 0x13
    REAGENT_DOOR_CLOSE_FAIL = 0x23
    AUXILIARY_REAGENT_NOT_RESET = 0x00
    AUXILIARY_REAGENT_RESETTING = 0x01
    AUXILIARY_REAGENT_RESET_SUCCESS = 0x11
    AUXILIARY_REAGENT_RESET_FAIL = 0x21
    AUXILIARY_REAGENT_PIPE_EMPTYING = 0x02
    AUXILIARY_REAGENT_PIPE_EMPTY_SUCCESS = 0x12
    AUXILIARY_REAGENT_PIPE_EMPTY_FAIL = 0x22
    AUXILIARY_REAGENT_ADDING = 0x03
    AUXILIARY_REAGENT_ADD_SUCCESS = 0x13
    AUXILIARY_REAGENT_ADD_FAIL = 0x23
    SLIDE_HOLDER_IDLE = 0x00
    SLIDE_HOLDER_EXECUTING = 0x01
    SLIDE_HOLDER_EXECUTE_FINISH = 0x02
    SLIDE_HOLDER_EXECUTE_STOP = 0x03
    SLIDE_HOLDER_EXECUTE_FAULT_STOP = 0x04
    SLIDE_HOLDER_EXECUTE_PAUSE = 0x05


alarm_message_map = {
   10:	"加热模块1-电机复位异常",
   11:	"加热模块1-电机运动异常",
   20:	"加热模块1-加热片1NTC异常",
   21:	"加热模块1-加热片2NTC异常",
   22:	"加热模块1-加热片3NTC异常",
   23:	"加热模块1-加热片4NTC异常",
   24:	"加热模块1-加热片5NTC异常",
   25:	"加热模块1-加热片6NTC异常",
   26:	"加热模块1-加热片7NTC异常",
   27:	"加热模块1-加热片8NTC异常",
   28:	"加热模块1-加热片9NTC异常",
   29:	"加热模块1-加热片10NTC异常",
   30:	"加热模块1-加热片11NTC异常",
   31:	"加热模块1-加热片12NTC异常",
   92:	"加热模块1-加热片1温控异常",
   93:	"加热模块1-加热片2温控异常",
   94:	"加热模块1-加热片3温控异常",
   95:	"加热模块1-加热片4温控异常",
   96:	"加热模块1-加热片5温控异常",
   97:	"加热模块1-加热片6温控异常",
   98:	"加热模块1-加热片7温控异常",
   99:	"加热模块1-加热片8温控异常",
   100:	"加热模块1-加热片9温控异常",
   101:	"加热模块1-加热片10温控异常",
   102:	"加热模块1-加热片11温控异常",
   103:	"加热模块1-加热片12温控异常",
   12:	"加热模块2-电机复位异常",
   13:	"加热模块2-电机运动异常",
   32:	"加热模块2-加热片1NTC异常",
   33:	"加热模块2-加热片2NTC异常",
   34:	"加热模块2-加热片3NTC异常",
   35:	"加热模块2-加热片4NTC异常",
   36:	"加热模块2-加热片5NTC异常",
   37:	"加热模块2-加热片6NTC异常",
   38:	"加热模块2-加热片7NTC异常",
   39:	"加热模块2-加热片8NTC异常",
   40:	"加热模块2-加热片9NTC异常",
   41:	"加热模块2-加热片10NTC异常",
   42:	"加热模块2-加热片11NTC异常",
   43:	"加热模块2-加热片12NTC异常",
   104:	"加热模块2-加热片1温控异常",
   105:	"加热模块2-加热片2温控异常",
   106:	"加热模块2-加热片3温控异常",
   107:	"加热模块2-加热片4温控异常",
   108:	"加热模块2-加热片5温控异常",
   109:	"加热模块2-加热片6温控异常",
   110:	"加热模块2-加热片7温控异常",
   111:	"加热模块2-加热片8温控异常",
   112:	"加热模块2-加热片9温控异常",
   113:	"加热模块2-加热片10温控异常",
   114:	"加热模块2-加热片11温控异常",
   115:	"加热模块2-加热片12温控异常",
   14:	"加热模块3-电机复位异常",
   15:	"加热模块3-电机运动异常",
   44:	"加热模块3-加热片1NTC异常",
   45:	"加热模块3-加热片2NTC异常",
   46:	"加热模块3-加热片3NTC异常",
   47:	"加热模块3-加热片4NTC异常",
   48:	"加热模块3-加热片5NTC异常",
   49:	"加热模块3-加热片6NTC异常",
   50:	"加热模块3-加热片7NTC异常",
   51:	"加热模块3-加热片8NTC异常",
   52:	"加热模块3-加热片9NTC异常",
   53:	"加热模块3-加热片10NTC异常",
   54:	"加热模块3-加热片11NTC异常",
   55:	"加热模块3-加热片12NTC异常",
   116:	"加热模块3-加热片1温控异常",
   117:	"加热模块3-加热片2温控异常",
   118:	"加热模块3-加热片3温控异常",
   119:	"加热模块3-加热片4温控异常",
   120:	"加热模块3-加热片5温控异常",
   121:	"加热模块3-加热片6温控异常",
   122:	"加热模块3-加热片7温控异常",
   123:	"加热模块3-加热片8温控异常",
   124:	"加热模块3-加热片9温控异常",
   125:	"加热模块3-加热片10温控异常",
   126:	"加热模块3-加热片11温控异常",
   127:	"加热模块3-加热片12温控异常",
   16:	"加热模块4-电机复位异常",
   17:	"加热模块4-电机运动异常",
   56:	"加热模块4-加热片1NTC异常",
   57:	"加热模块4-加热片2NTC异常",
   58:	"加热模块4-加热片3NTC异常",
   59:	"加热模块4-加热片4NTC异常",
   60:	"加热模块4-加热片5NTC异常",
   61:	"加热模块4-加热片6NTC异常",
   62:	"加热模块4-加热片7NTC异常",
   63:	"加热模块4-加热片8NTC异常",
   64:	"加热模块4-加热片9NTC异常",
   65:	"加热模块4-加热片10NTC异常",
   66:	"加热模块4-加热片11NTC异常",
   67:	"加热模块4-加热片12NTC异常",
   128:	"加热模块4-加热片1温控异常",
   129:	"加热模块4-加热片2温控异常",
   130:	"加热模块4-加热片3温控异常",
   131:	"加热模块4-加热片4温控异常",
   132:	"加热模块4-加热片5温控异常",
   133:	"加热模块4-加热片6温控异常",
   134:	"加热模块4-加热片7温控异常",
   135:	"加热模块4-加热片8温控异常",
   136:	"加热模块4-加热片9温控异常",
   137:	"加热模块4-加热片10温控异常",
   138:	"加热模块4-加热片11温控异常",
   139:	"加热模块4-加热片12温控异常",
   170:	"X轴电机复位异常",
   171:	"Y轴电机复位异常",
   172:	"Z轴电机复位异常",
   173:	"T轴电机复位异常",
   174:	"X轴电机运动异常",
   175:	"Y轴电机运动异常",
   176:	"Z轴电机运动异常",
   177:	"T轴电机运动异常",
   178:	"辅助电机1复位异常",
   179:	"辅助电机2复位异常",
   180:	"试剂门电机复位异常",
   181:	"仓门电机复位异常",
   182:	"辅助电机1运动异常",
   183:	"辅助电机2运动异常",
   184:	"试剂门电机运动异常",
   185:	"仓门电机运动异常",
   190:	"辅助试剂1转向阀复位异常",
   191:	"辅助试剂2转向阀复位异常",
   192:	"辅助试剂1注射电机复位异常",
   193:	"辅助试剂2注射电机复位异常",
   194:	"试剂针注射泵复位异常",
   195:	"辅助试剂1注射泵吸排液异常",
   196:	"辅助试剂2注射泵吸排液异常",
   197:	"试剂针注射泵吸排液异常",
   200:	"加热模块1通信异常",
   201:	"加热模块2通信异常",
   202:	"加热模块3通信异常",
   203:	"加热模块4通信异常",
   204:	"三轴电机板通信异常",
   205:	"辅助试剂电机板通信异常",
   206:	"注射泵电机板通信异常",
   207:	"扫描枪通信异常",
   208:	"显示屏通信异常",
   209:	"有害废液桶液满",
   210:	"无害废液桶液满",
   211:	"辅助试剂瓶1不在位",
   212:	"辅助试剂瓶2不在位",
   213:	"辅助试剂瓶3不在位",
   214:	"辅助试剂瓶4不在位",
   215:	"辅助试剂瓶5不在位",
   216:	"辅助试剂瓶6不在位",
   217:	"辅助试剂瓶1缺液",
   218:	"辅助试剂瓶2缺液",
   219:	"辅助试剂瓶3缺液",
   220:	"辅助试剂瓶4缺液",
   221:	"辅助试剂瓶5缺液",
   222:	"辅助试剂瓶6缺液",
   223:	"质控滴液异常(缺液)",
   224:	"质控滴液异常(三轴运动异常)",
   225:	"质控滴液异常(加热模块运动异常)",
   226:	"质控滴液异常(注射泵异常)",
   227:	"试剂针滴液异常(缺液)",
   228:	"试剂针滴液异常(三轴运动异常)",
   229:	"试剂针滴液异常(加热模块运动异常)",
   230:	"试剂针滴液异常(注射泵异常)",
   231:	"混液异常(缺液)",
   232:	"混液液异常(三轴运动异常)",
   233:	"混液异常(注射泵异常)",
   234:	"混液区清洗异常(缺液)",
   235:	"混液区清洗异常(三轴运动异常)",
   236:	"混液区清洗异常(注射泵异常)",
   237:	"辅助试剂1区加液异常(缺液)",
   238:	"辅助试剂1区加液异常(加热模块运动异常)",
   239:	"辅助试剂2区加液异常(缺液)",
   240:	"辅助试剂2区加液异常(加热模块运动异常)",
   241:	"试剂区温度传感器异常",
   242:  "无害缓冲罐液满",
   243:  "有害缓冲罐液满"
}


class AlarmCode(Singleton):
   HeatModuleOneFail = 200
   HeatModuleTwoFail = 201
   HeatModuleThreeFail = 202
   HeatModuleFourFail = 203
   ThreeAxisFail = 204
   AuxiliaryReagentFail = 205
   SyringePumpFail = 206
   ScannerFail = 207
   ScreenFail = 208
   WasteFull = 209
   HarmWasteFull = 210
   AuxiliaryBottleOneMiss = 211
   AuxiliaryBottleTwoMiss = 212
   AuxiliaryBottleThreeMiss = 213
   AuxiliaryBottleFourMiss = 214
   AuxiliaryBottleFiveMiss = 215
   AuxiliaryBottleSixMiss = 216
   AuxiliaryBottleOneEmpty = 217
   AuxiliaryBottleTwoEmpty = 218
   AuxiliaryBottleThreeEmpty = 219
   AuxiliaryBottleFourEmpty = 220
   AuxiliaryBottleFiveEmpty = 221
   AuxiliaryBottleSixEmpty = 222
   ControlReagentEmpty = 223
   ControlDrippingFail = 224
   ControlHeatingFail = 225
   ControlPumpFail = 226
   NeedleDrippingEmpty = 227
   NeedleMotionFail = 228
   NeedleHeatingFail = 229
   NeedlePumpFail = 230
   MixReagentEmpty = 231
   MixMotionFail = 232
   MixPumpingFail = 233
   MixCleanEmpty = 234
   MixCleanMotionFail = 235
   MixCleanPumpingFail = 236
   AuxiliaryAreaEmpty = 237
   AuxiliaryAreaHeatFail = 238
   AuxiliaryAreaTwoEmpty = 239
   AuxiliaryAreaTwoHeatFaile = 240
   ReagentTemperatureFail = 241
   BufferTankFull = 242
   HarmBufferTankFull = 243
