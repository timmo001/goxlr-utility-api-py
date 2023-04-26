"""GoXLR Utility API: Status Models"""
from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field  # pylint: disable=no-name-in-module


class Config(BaseModel):
    """Config Model"""

    daemon_version: str
    autostart_enabled: bool
    show_tray_icon: bool
    tts_enabled: bool


class Versions(BaseModel):
    """Versions Model"""

    firmware: list[int]
    fpga_count: int
    dice: list[int]


class UsbDevice(BaseModel):
    """USB Device Model"""

    manufacturer_name: str
    product_name: str
    version: list[int]
    bus_number: int
    address: int
    identifier: str


class Hardware(BaseModel):
    """Hardware Model"""

    versions: Versions
    serial_number: str
    manufactured_date: str
    device_type: str
    usb_device: UsbDevice


class FaderStatus(BaseModel):
    """Fader Status Model"""

    channel: str
    mute_type: str
    scribble: Any
    mute_state: str


class FaderStatuses(BaseModel):
    """Fader Statuses Model"""

    a: FaderStatus = Field(..., alias="A")
    b: FaderStatus = Field(..., alias="B")
    c: FaderStatus = Field(..., alias="C")
    d: FaderStatus = Field(..., alias="D")


class MicGains(BaseModel):
    """Mic Gains Model"""

    dynamic: int = Field(..., alias="Dynamic")
    condenser: int = Field(..., alias="Condenser")
    jack: int = Field(..., alias="Jack")


class Gain(BaseModel):
    """Gain Model"""

    equalizer4_k_hz: int = Field(..., alias="Equalizer4KHz")
    equalizer16_k_hz: int = Field(..., alias="Equalizer16KHz")
    equalizer1_k_hz: int = Field(..., alias="Equalizer1KHz")
    equalizer2_k_hz: int = Field(..., alias="Equalizer2KHz")
    equalizer125_hz: int = Field(..., alias="Equalizer125Hz")
    equalizer500_hz: int = Field(..., alias="Equalizer500Hz")
    equalizer31_hz: int = Field(..., alias="Equalizer31Hz")
    equalizer63_hz: int = Field(..., alias="Equalizer63Hz")
    equalizer8_k_hz: int = Field(..., alias="Equalizer8KHz")
    equalizer250_hz: int = Field(..., alias="Equalizer250Hz")


class Frequency(BaseModel):
    """Frequency Model"""

    equalizer16_k_hz: int = Field(..., alias="Equalizer16KHz")
    equalizer500_hz: int = Field(..., alias="Equalizer500Hz")
    equalizer125_hz: int = Field(..., alias="Equalizer125Hz")
    equalizer4_k_hz: int = Field(..., alias="Equalizer4KHz")
    equalizer250_hz: int = Field(..., alias="Equalizer250Hz")
    equalizer8_k_hz: int = Field(..., alias="Equalizer8KHz")
    equalizer2_k_hz: int = Field(..., alias="Equalizer2KHz")
    equalizer31_hz: float = Field(..., alias="Equalizer31Hz")
    equalizer1_k_hz: int = Field(..., alias="Equalizer1KHz")
    equalizer63_hz: int = Field(..., alias="Equalizer63Hz")


class Equaliser(BaseModel):
    """Equaliser Model"""

    gain: Gain
    frequency: Frequency


class Gain1(BaseModel):
    """Gain1 Model"""

    equalizer90_hz: int = Field(..., alias="Equalizer90Hz")
    equalizer250_hz: int = Field(..., alias="Equalizer250Hz")
    equalizer1_k_hz: int = Field(..., alias="Equalizer1KHz")
    equalizer3_k_hz: int = Field(..., alias="Equalizer3KHz")
    equalizer8_k_hz: int = Field(..., alias="Equalizer8KHz")
    equalizer500_hz: int = Field(..., alias="Equalizer500Hz")


class Frequency1(BaseModel):
    """Frequency1 Model"""

    equalizer3_k_hz: int = Field(..., alias="Equalizer3KHz")
    equalizer1_k_hz: int = Field(..., alias="Equalizer1KHz")
    equalizer90_hz: int = Field(..., alias="Equalizer90Hz")
    equalizer250_hz: int = Field(..., alias="Equalizer250Hz")
    equalizer8_k_hz: int = Field(..., alias="Equalizer8KHz")
    equalizer500_hz: int = Field(..., alias="Equalizer500Hz")


class EqualiserMini(BaseModel):
    """Equaliser Mini Model"""

    gain: Gain1
    frequency: Frequency1


class NoiseGate(BaseModel):
    """Noise Gate Model"""

    threshold: int
    attack: int
    release: int
    enabled: bool
    attenuation: int


class Compressor(BaseModel):
    """Compressor Model"""

    threshold: int
    ratio: int
    attack: int
    release: int
    makeup_gain: int


class MicStatus(BaseModel):
    """Mic Status Model"""

    mic_type: str
    mic_gains: MicGains
    equaliser: Equaliser
    equaliser_mini: EqualiserMini
    noise_gate: NoiseGate
    compressor: Compressor


class Volumes(BaseModel):
    """Volumes Model"""

    mic: int = Field(..., alias="Mic")
    line_in: int = Field(..., alias="LineIn")
    console: int = Field(..., alias="Console")
    system: int = Field(..., alias="System")
    game: int = Field(..., alias="Game")
    chat: int = Field(..., alias="Chat")
    sample: int = Field(..., alias="Sample")
    music: int = Field(..., alias="Music")
    headphones: int = Field(..., alias="Headphones")
    mic_monitor: int = Field(..., alias="MicMonitor")
    line_out: int = Field(..., alias="LineOut")


class Levels(BaseModel):
    """Levels Model"""

    submix_supported: bool
    volumes: Volumes
    submix: Any
    bleep: int
    deess: int


class RouterItem(BaseModel):
    """Router Item Model"""

    headphones: bool = Field(..., alias="Headphones")
    broadcast_mix: bool = Field(..., alias="BroadcastMix")
    chat_mic: bool = Field(..., alias="ChatMic")
    sampler: bool = Field(..., alias="Sampler")
    line_out: bool = Field(..., alias="LineOut")


class Router(BaseModel):
    """Router Model"""

    microphone: RouterItem = Field(..., alias="Microphone")
    chat: RouterItem = Field(..., alias="Chat")
    music: RouterItem = Field(..., alias="Music")
    game: RouterItem = Field(..., alias="Game")
    console: RouterItem = Field(..., alias="Console")
    line_in: RouterItem = Field(..., alias="LineIn")
    system: RouterItem = Field(..., alias="System")
    samples: RouterItem = Field(..., alias="Samples")


class CoughButton(BaseModel):
    """Cough Button Model"""

    is_toggle: bool
    mute_type: str
    state: str


class Colours(BaseModel):
    """Colours Model"""

    colour_one: str
    colour_two: str


class Fader(BaseModel):
    """Fader Model"""

    style: str
    colours: Colours


class Faders(BaseModel):
    """Faders Model"""

    a: Fader = Field(..., alias="A")
    b: Fader = Field(..., alias="B")
    c: Fader = Field(..., alias="C")
    d: Fader = Field(..., alias="D")


class Button(BaseModel):
    """Button Model"""

    off_style: str
    colours: Colours


class Buttons(BaseModel):
    """Buttons Model"""

    bleep: Button = Field(..., alias="Bleep")
    fader1_mute: Button = Field(..., alias="Fader1Mute")
    fader3_mute: Button = Field(..., alias="Fader3Mute")
    fader2_mute: Button = Field(..., alias="Fader2Mute")
    fader4_mute: Button = Field(..., alias="Fader4Mute")
    cough: Button = Field(..., alias="Cough")


class Global(BaseModel):
    """Global Model"""

    colour_one: str


class Accent(BaseModel):
    """Accent Model"""

    colour_one: str


class Simple(BaseModel):
    """Simple Model"""

    global_: Global = Field(..., alias="Global")
    accent: Accent = Field(..., alias="Accent")


class Lighting(BaseModel):
    """Lighting Model"""

    faders: Faders
    buttons: Buttons
    simple: Simple
    sampler: dict[str, Any]
    encoders: dict[str, Any]


class Display(BaseModel):
    """Display Model"""

    gate: str
    compressor: str
    equaliser: str
    equaliser_fine: str


class Settings(BaseModel):
    """Settings Model"""

    display: Display
    mute_hold_duration: int
    vc_mute_also_mute_cm: bool


class ButtonDown(BaseModel):
    """Button Down Model"""

    fader1_mute: bool = Field(..., alias="Fader1Mute")
    fader2_mute: bool = Field(..., alias="Fader2Mute")
    fader3_mute: bool = Field(..., alias="Fader3Mute")
    fader4_mute: bool = Field(..., alias="Fader4Mute")
    bleep: bool = Field(..., alias="Bleep")
    cough: bool = Field(..., alias="Cough")
    effect_select1: bool = Field(..., alias="EffectSelect1")
    effect_select2: bool = Field(..., alias="EffectSelect2")
    effect_select3: bool = Field(..., alias="EffectSelect3")
    effect_select4: bool = Field(..., alias="EffectSelect4")
    effect_select5: bool = Field(..., alias="EffectSelect5")
    effect_select6: bool = Field(..., alias="EffectSelect6")
    effect_fx: bool = Field(..., alias="EffectFx")
    effect_megaphone: bool = Field(..., alias="EffectMegaphone")
    effect_robot: bool = Field(..., alias="EffectRobot")
    effect_hard_tune: bool = Field(..., alias="EffectHardTune")
    sampler_select_a: bool = Field(..., alias="SamplerSelectA")
    sampler_select_b: bool = Field(..., alias="SamplerSelectB")
    sampler_select_c: bool = Field(..., alias="SamplerSelectC")
    sampler_top_left: bool = Field(..., alias="SamplerTopLeft")
    sampler_top_right: bool = Field(..., alias="SamplerTopRight")
    sampler_bottom_left: bool = Field(..., alias="SamplerBottomLeft")
    sampler_bottom_right: bool = Field(..., alias="SamplerBottomRight")
    sampler_clear: bool = Field(..., alias="SamplerClear")


class Mixer(BaseModel):
    """Mixer Model"""

    hardware: Hardware
    shutdown_commands: list
    fader_status: FaderStatuses
    mic_status: MicStatus
    levels: Levels
    router: Router
    cough_button: CoughButton
    lighting: Lighting
    effects: Any
    sampler: Any
    settings: Settings
    button_down: ButtonDown
    profile_name: str
    mic_profile_name: str


class Paths(BaseModel):
    """Paths Model"""

    profile_directory: str
    mic_profile_directory: str
    samples_directory: str
    presets_directory: str
    icons_directory: str


class Files(BaseModel):
    """Files Model"""

    profiles: list[str]
    mic_profiles: list[str]
    presets: list[str]
    samples: dict[str, Any]
    icons: list[str]


class Status(BaseModel):
    """Status Model"""

    config: Config
    mixers: dict[str, Mixer]
    paths: Paths
    files: Files


class Data(BaseModel):
    """Data Model"""

    status: Status = Field(..., alias="Status")
