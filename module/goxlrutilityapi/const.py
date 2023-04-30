"""GoXLR Utility API: Constants"""

from typing import Any, Final

from .models.map_item import MapItem
from .models.patch import Patch
from .models.request import Request
from .models.response import Response
from .models.status import Status

# Connection
DEFAULT_HOST: Final[str] = "localhost"
DEFAULT_PORT: Final[int] = 14564

# Mixer
VOLUME_MAX: Final[int] = 255
MUTED_STATE: Final[str] = "MutedToX"
UNMUTED_STATE: Final[str] = "Unmuted"

# Request/Response Keys
KEY_DATA: Final[str] = "data"
KEY_ID: Final[str] = "id"
KEY_TYPE: Final[str] = "type"

# Request Types (https://github.com/GoXLR-on-Linux/goxlr-utility/blob/c2c876dd83ddcd4681b1a674c5cb975796726dd8/ipc/src/lib.rs#L20)
REQUEST_TYPE_COMMAND: Final[str] = "Command"
REQUEST_TYPE_GET_HTTP_STATE: Final[str] = "GetHttpState"
REQUEST_TYPE_GET_STATUS: Final[str] = "GetStatus"
REQUEST_TYPE_OPEN_PATH: Final[str] = "OpenPath"
REQUEST_TYPE_OPEN_UI: Final[str] = "OpenUi"
REQUEST_TYPE_PING: Final[str] = "Ping"
REQUEST_TYPE_RECOVER_DEFAULTS: Final[str] = "RecoverDefaults"
REQUEST_TYPE_SET_AUTOSTART_ENABLED: Final[str] = "SetAutoStartEnabled"
REQUEST_TYPE_SET_SHOW_TRAY_ICON: Final[str] = "SetShowTrayIcon"
REQUEST_TYPE_SET_TTS_ENABLED: Final[str] = "SetTTSEnabled"
REQUEST_TYPE_STOP_DAEMON: Final[str] = "StopDaemon"

# Response Types (https://github.com/GoXLR-on-Linux/goxlr-utility/blob/c2c876dd83ddcd4681b1a674c5cb975796726dd8/ipc/src/lib.rs#L35)
RESPONSE_TYPE_ERROR: Final[str] = "Error"
RESPONSE_TYPE_HTTP_STATE: Final[str] = "HttpState"
RESPONSE_TYPE_OK: Final[str] = "Ok"
RESPONSE_TYPE_PATCH: Final[str] = "Patch"
RESPONSE_TYPE_STATUS: Final[str] = "Status"

# Command Types (https://github.com/GoXLR-on-Linux/goxlr-utility/blob/c2c876dd83ddcd4681b1a674c5cb975796726dd8/ipc/src/lib.rs#LL65C17-L65C17)
COMMAND_TYPE_SET_ALL_FADER_COLOURS: Final[str] = "SetAllFaderColours"
COMMAND_TYPE_SET_ALL_FADER_DISPLAY_STYLE: Final[str] = "SetAllFaderDisplayStyle"
COMMAND_TYPE_SET_BUTTON_COLOURS: Final[str] = "SetButtonColours"
COMMAND_TYPE_SET_BUTTON_GROUP_COLOURS: Final[str] = "SetButtonGroupColours"
COMMAND_TYPE_SET_BUTTON_GROUP_OFF_STYLE: Final[str] = "SetButtonGroupOffStyle"
COMMAND_TYPE_SET_BUTTON_OFF_STYLE: Final[str] = "SetButtonOffStyle"
COMMAND_TYPE_SET_ENCODER_COLOUR: Final[str] = "SetEncoderColour"
COMMAND_TYPE_SET_FADER_COLOURS: Final[str] = "SetFaderColours"
COMMAND_TYPE_SET_FADER_DISPLAY_STYLE: Final[str] = "SetFaderDisplayStyle"
COMMAND_TYPE_SET_SAMPLE_COLOUR: Final[str] = "SetSampleColour"
COMMAND_TYPE_SET_SAMPLE_OFF_STYLE: Final[str] = "SetSampleOffStyle"
COMMAND_TYPE_SET_SIMPLE_COLOUR: Final[str] = "SetSimpleColour"

# Buttons
# pub enum Button {
#     // These are all the buttons from the GoXLR Mini.
#     Fader1Mute,
#     Fader2Mute,
#     Fader3Mute,
#     Fader4Mute,
#     Bleep,
#     Cough,

#     // The rest are GoXLR Full Buttons. On the mini, they will simply be ignored.
#     EffectSelect1,
#     EffectSelect2,
#     EffectSelect3,
#     EffectSelect4,
#     EffectSelect5,
#     EffectSelect6,

#     // FX Button labelled as 'fxClear' in config?
#     EffectFx,
#     EffectMegaphone,
#     EffectRobot,
#     EffectHardTune,

#     SamplerSelectA,
#     SamplerSelectB,
#     SamplerSelectC,

#     SamplerTopLeft,
#     SamplerTopRight,
#     SamplerBottomLeft,
#     SamplerBottomRight,
#     SamplerClear,
# }

# Models
MODEL_PATCH: type[Patch] = Patch
MODEL_REQUEST: type[Request] = Request
MODEL_RESPONSE: type[Response[Any]] = Response
MODEL_STATUS: type[Status] = Status

MODEL_MAP: Final[dict[str, Any]] = {
    RESPONSE_TYPE_PATCH: MODEL_PATCH,
    RESPONSE_TYPE_STATUS: MODEL_STATUS,
}

NAME_MAP: Final[dict[str, MapItem]] = {
    "bleep": MapItem(name="Bleep", icon="mdi:exclamation"),
    "chat": MapItem(name="Chat", icon="mdi:chat"),
    "console": MapItem(name="Console", icon="mdi:gamepad-variant"),
    "cough": MapItem(name="Cough", icon="mdi:microphone-off"),
    "effect_fx": MapItem(name="Effect FX", icon="mdi:equalizer-outline"),
    "effect_hard_tune": MapItem(name="Effect Hard Tune", icon="mdi:knob"),
    "effect_megaphone": MapItem(name="Effect Megaphone", icon="mdi:bullhorn-outline"),
    "effect_robot": MapItem(name="Effect Robot", icon="mdi:robot-outline"),
    "effect_select1": MapItem(name="Effect Select 1", icon="mdi:sawtooth-wave"),
    "effect_select2": MapItem(name="Effect Select 2", icon="mdi:sawtooth-wave"),
    "effect_select3": MapItem(name="Effect Select 3", icon="mdi:sawtooth-wave"),
    "effect_select4": MapItem(name="Effect Select 4", icon="mdi:sawtooth-wave"),
    "effect_select5": MapItem(name="Effect Select 5", icon="mdi:sawtooth-wave"),
    "effect_select6": MapItem(name="Effect Select 6", icon="mdi:sawtooth-wave"),
    "fader1_mute": MapItem(name="Fader 1 Mute", icon="mdi:microphone-off"),
    "fader2_mute": MapItem(name="Fader 2 Mute", icon="mdi:microphone-off"),
    "fader3_mute": MapItem(name="Fader 3 Mute", icon="mdi:microphone-off"),
    "fader4_mute": MapItem(name="Fader 4 Mute", icon="mdi:microphone-off"),
    "headphones": MapItem(name="Headphones", icon="mdi:headphones"),
    "line_in": MapItem(name="Line In", icon="mdi:audio-input-stereo-minijack"),
    "line_out": MapItem(name="Line In", icon="mdi:audio-input-stereo-minijack"),
    "LineIn": MapItem(name="Line In", icon="mdi:audio-input-stereo-minijack"),
    "LineOut": MapItem(name="Line In", icon="mdi:audio-input-stereo-minijack"),
    "mic_monitor": MapItem(name="Microphone Monitor", icon="mdi:microphone-outline"),
    "mic": MapItem(name="Microphone", icon="mdi:microphone"),
    "Mic": MapItem(name="Microphone", icon="mdi:microphone"),
    "MicMonitor": MapItem(name="Microphone Monitor", icon="mdi:microphone-outline"),
    "music": MapItem(name="Music", icon="mdi:music"),
    "Music": MapItem(name="Music", icon="mdi:music"),
    "mute_all": MapItem(name="Mute All", icon="mdi:microphone-off"),
    "mute_chat": MapItem(name="Mute Chat", icon="mdi:microphone-off"),
    "mute_console": MapItem(name="Mute Console", icon="mdi:microphone-off"),
    "mute_line_in": MapItem(name="Mute Line In", icon="mdi:microphone-off"),
    "mute_line_out": MapItem(name="Mute Line Out", icon="mdi:microphone-off"),
    "mute_mic": MapItem(name="Mute Microphone", icon="mdi:microphone-off"),
    "mute_microphone": MapItem(name="Mute Microphone", icon="mdi:microphone-off"),
    "mute_music": MapItem(name="Mute Music", icon="mdi:microphone-off"),
    "mute_system": MapItem(name="Mute System", icon="mdi:microphone-off"),
    "mute": MapItem(name="Mute", icon="mdi:microphone-off"),
    "sample": MapItem(name="Sample", icon="mdi:music-note"),
    "sampler_bottom_left": MapItem(name="Sampler Bottom Left", icon="mdi:music-note"),
    "sampler_bottom_right": MapItem(name="Sampler Bottom Right", icon="mdi:music-note"),
    "sampler_clear": MapItem(name="Sampler Clear", icon="mdi:music-note"),
    "sampler_select_a": MapItem(name="Sampler Select A", icon="mdi:music-note"),
    "sampler_select_b": MapItem(name="Sampler Select B", icon="mdi:music-note"),
    "sampler_select_c": MapItem(name="Sampler Select C", icon="mdi:music-note"),
    "sampler_top_left": MapItem(name="Sampler Top Left", icon="mdi:music-note"),
    "sampler_top_right": MapItem(name="Sampler Top Right", icon="mdi:music-note"),
    "system": MapItem(name="System", icon="mdi:music-box-outline"),
    "System": MapItem(name="System", icon="mdi:music-box-outline"),
}
