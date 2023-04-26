"""GoXLR Utility API: Status Models"""
from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class Config(BaseModel):
    daemon_version: str
    autostart_enabled: bool
    show_tray_icon: bool
    tts_enabled: bool


class Versions(BaseModel):
    firmware: list[int]
    fpga_count: int
    dice: list[int]


class UsbDevice(BaseModel):
    manufacturer_name: str
    product_name: str
    version: list[int]
    bus_number: int
    address: int
    identifier: str


class Hardware(BaseModel):
    versions: Versions
    serial_number: str
    manufactured_date: str
    device_type: str
    usb_device: UsbDevice


class A(BaseModel):
    channel: str
    mute_type: str
    scribble: Any
    mute_state: str


class B(BaseModel):
    channel: str
    mute_type: str
    scribble: Any
    mute_state: str


class C(BaseModel):
    channel: str
    mute_type: str
    scribble: Any
    mute_state: str


class D(BaseModel):
    channel: str
    mute_type: str
    scribble: Any
    mute_state: str


class FaderStatus(BaseModel):
    a: A = Field(..., alias="A")
    b: B = Field(..., alias="B")
    c: C = Field(..., alias="C")
    d: D = Field(..., alias="D")


class MicGains(BaseModel):
    dynamic: int = Field(..., alias="Dynamic")
    condenser: int = Field(..., alias="Condenser")
    jack: int = Field(..., alias="Jack")


class Gain(BaseModel):
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
    gain: Gain
    frequency: Frequency


class Gain1(BaseModel):
    equalizer90_hz: int = Field(..., alias="Equalizer90Hz")
    equalizer250_hz: int = Field(..., alias="Equalizer250Hz")
    equalizer1_k_hz: int = Field(..., alias="Equalizer1KHz")
    equalizer3_k_hz: int = Field(..., alias="Equalizer3KHz")
    equalizer8_k_hz: int = Field(..., alias="Equalizer8KHz")
    equalizer500_hz: int = Field(..., alias="Equalizer500Hz")


class Frequency1(BaseModel):
    equalizer3_k_hz: int = Field(..., alias="Equalizer3KHz")
    equalizer1_k_hz: int = Field(..., alias="Equalizer1KHz")
    equalizer90_hz: int = Field(..., alias="Equalizer90Hz")
    equalizer250_hz: int = Field(..., alias="Equalizer250Hz")
    equalizer8_k_hz: int = Field(..., alias="Equalizer8KHz")
    equalizer500_hz: int = Field(..., alias="Equalizer500Hz")


class EqualiserMini(BaseModel):
    gain: Gain1
    frequency: Frequency1


class NoiseGate(BaseModel):
    threshold: int
    attack: int
    release: int
    enabled: bool
    attenuation: int


class Compressor(BaseModel):
    threshold: int
    ratio: int
    attack: int
    release: int
    makeup_gain: int


class MicStatus(BaseModel):
    mic_type: str
    mic_gains: MicGains
    equaliser: Equaliser
    equaliser_mini: EqualiserMini
    noise_gate: NoiseGate
    compressor: Compressor


class Volumes(BaseModel):
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
    submix_supported: bool
    volumes: Volumes
    submix: Any
    bleep: int
    deess: int


class Microphone(BaseModel):
    headphones: bool = Field(..., alias="Headphones")
    broadcast_mix: bool = Field(..., alias="BroadcastMix")
    chat_mic: bool = Field(..., alias="ChatMic")
    sampler: bool = Field(..., alias="Sampler")
    line_out: bool = Field(..., alias="LineOut")


class Chat(BaseModel):
    headphones: bool = Field(..., alias="Headphones")
    broadcast_mix: bool = Field(..., alias="BroadcastMix")
    chat_mic: bool = Field(..., alias="ChatMic")
    sampler: bool = Field(..., alias="Sampler")
    line_out: bool = Field(..., alias="LineOut")


class Music(BaseModel):
    headphones: bool = Field(..., alias="Headphones")
    broadcast_mix: bool = Field(..., alias="BroadcastMix")
    chat_mic: bool = Field(..., alias="ChatMic")
    sampler: bool = Field(..., alias="Sampler")
    line_out: bool = Field(..., alias="LineOut")


class Game(BaseModel):
    headphones: bool = Field(..., alias="Headphones")
    broadcast_mix: bool = Field(..., alias="BroadcastMix")
    chat_mic: bool = Field(..., alias="ChatMic")
    sampler: bool = Field(..., alias="Sampler")
    line_out: bool = Field(..., alias="LineOut")


class Console(BaseModel):
    headphones: bool = Field(..., alias="Headphones")
    broadcast_mix: bool = Field(..., alias="BroadcastMix")
    chat_mic: bool = Field(..., alias="ChatMic")
    sampler: bool = Field(..., alias="Sampler")
    line_out: bool = Field(..., alias="LineOut")


class LineIn(BaseModel):
    headphones: bool = Field(..., alias="Headphones")
    broadcast_mix: bool = Field(..., alias="BroadcastMix")
    chat_mic: bool = Field(..., alias="ChatMic")
    sampler: bool = Field(..., alias="Sampler")
    line_out: bool = Field(..., alias="LineOut")


class System(BaseModel):
    headphones: bool = Field(..., alias="Headphones")
    broadcast_mix: bool = Field(..., alias="BroadcastMix")
    chat_mic: bool = Field(..., alias="ChatMic")
    sampler: bool = Field(..., alias="Sampler")
    line_out: bool = Field(..., alias="LineOut")


class Samples(BaseModel):
    headphones: bool = Field(..., alias="Headphones")
    broadcast_mix: bool = Field(..., alias="BroadcastMix")
    chat_mic: bool = Field(..., alias="ChatMic")
    sampler: bool = Field(..., alias="Sampler")
    line_out: bool = Field(..., alias="LineOut")


class Router(BaseModel):
    microphone: Microphone = Field(..., alias="Microphone")
    chat: Chat = Field(..., alias="Chat")
    music: Music = Field(..., alias="Music")
    game: Game = Field(..., alias="Game")
    console: Console = Field(..., alias="Console")
    line_in: LineIn = Field(..., alias="LineIn")
    system: System = Field(..., alias="System")
    samples: Samples = Field(..., alias="Samples")


class CoughButton(BaseModel):
    is_toggle: bool
    mute_type: str
    state: str


class Colours(BaseModel):
    colour_one: str
    colour_two: str


class B1(BaseModel):
    style: str
    colours: Colours


class D1(BaseModel):
    style: str
    colours: Colours


class A1(BaseModel):
    style: str
    colours: Colours


class C1(BaseModel):
    style: str
    colours: Colours


class Faders(BaseModel):
    b: B1 = Field(..., alias="B")
    d: D1 = Field(..., alias="D")
    a: A1 = Field(..., alias="A")
    c: C1 = Field(..., alias="C")


class Bleep(BaseModel):
    off_style: str
    colours: Colours


class Fader1Mute(BaseModel):
    off_style: str
    colours: Colours


class Fader3Mute(BaseModel):
    off_style: str
    colours: Colours


class Fader2Mute(BaseModel):
    off_style: str
    colours: Colours


class Fader4Mute(BaseModel):
    off_style: str
    colours: Colours


class Cough(BaseModel):
    off_style: str
    colours: Colours


class Buttons(BaseModel):
    bleep: Bleep = Field(..., alias="Bleep")
    fader1_mute: Fader1Mute = Field(..., alias="Fader1Mute")
    fader3_mute: Fader3Mute = Field(..., alias="Fader3Mute")
    fader2_mute: Fader2Mute = Field(..., alias="Fader2Mute")
    fader4_mute: Fader4Mute = Field(..., alias="Fader4Mute")
    cough: Cough = Field(..., alias="Cough")


class Global(BaseModel):
    colour_one: str


class Accent(BaseModel):
    colour_one: str


class Simple(BaseModel):
    global_: Global = Field(..., alias="Global")
    accent: Accent = Field(..., alias="Accent")


class Lighting(BaseModel):
    faders: Faders
    buttons: Buttons
    simple: Simple
    sampler: dict[str, Any]
    encoders: dict[str, Any]


class Display(BaseModel):
    gate: str
    compressor: str
    equaliser: str
    equaliser_fine: str


class Settings(BaseModel):
    display: Display
    mute_hold_duration: int
    vc_mute_also_mute_cm: bool


class ButtonDown(BaseModel):
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
    hardware: Hardware
    shutdown_commands: list
    fader_status: FaderStatus
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
    profile_directory: str
    mic_profile_directory: str
    samples_directory: str
    presets_directory: str
    icons_directory: str


class Files(BaseModel):
    profiles: list[str]
    mic_profiles: list[str]
    presets: list[str]
    samples: dict[str, Any]
    icons: list[str]


class Status(BaseModel):
    config: Config
    mixers: dict[str, Mixer]
    paths: Paths
    files: Files


class Data(BaseModel):
    status: Status = Field(..., alias="Status")
