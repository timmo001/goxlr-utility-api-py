"""GoXLR Utility API: Status Models."""
from dataclasses import dataclass
from typing import Any


@dataclass
class Config:
    """Config Model."""

    daemon_version: str | None = None
    autostart_enabled: bool | None = None
    show_tray_icon: bool | None = None
    tts_enabled: bool | None = None
    allow_network_access: bool | None = None
    log_level: str | None = None


@dataclass
class Versions:
    """Versions Model."""

    firmware: list[int] | None = None
    fpga_count: int | None = None
    dice: list[int] | None = None


@dataclass
class UsbDevice:
    """USB Device Model."""

    manufacturer_name: str
    product_name: str
    version: list[int]
    bus_number: int
    address: int
    identifier: str


@dataclass
class Hardware:
    """Hardware Model."""

    versions: Versions
    serial_number: str
    manufactured_date: str
    device_type: str
    usb_device: UsbDevice


@dataclass
class FaderStatus:
    """Fader Status Model."""

    channel: str
    mute_type: str
    mute_state: str
    scribble: Any | None = None


@dataclass
class FaderStatuses:
    """Fader Statuses Model."""

    a: FaderStatus = Field(..., alias="A")
    b: FaderStatus = Field(..., alias="B")
    c: FaderStatus = Field(..., alias="C")
    d: FaderStatus = Field(..., alias="D")


@dataclass
class MicGains:
    """Mic Gains Model."""

    dynamic: int | None = None = Field(None, alias="Dynamic")
    condenser: int | None = None = Field(None, alias="Condenser")
    jack: int | None = None = Field(None, alias="Jack")


@dataclass
class Gain:
    """Gain Model."""

    equalizer4_k_hz: int | None = None = Field(None, alias="Equalizer4KHz")
    equalizer16_k_hz: int | None = None = Field(None, alias="Equalizer16KHz")
    equalizer1_k_hz: int | None = None = Field(None, alias="Equalizer1KHz")
    equalizer2_k_hz: int | None = None = Field(None, alias="Equalizer2KHz")
    equalizer125_hz: int | None = None = Field(None, alias="Equalizer125Hz")
    equalizer500_hz: int | None = None = Field(None, alias="Equalizer500Hz")
    equalizer31_hz: int | None = None = Field(None, alias="Equalizer31Hz")
    equalizer63_hz: int | None = None = Field(None, alias="Equalizer63Hz")
    equalizer8_k_hz: int | None = None = Field(None, alias="Equalizer8KHz")
    equalizer250_hz: int | None = None = Field(None, alias="Equalizer250Hz")


@dataclass
class Frequency:
    """Frequency Model."""

    equalizer16_k_hz: int | None = None = Field(None, alias="Equalizer16KHz")
    equalizer500_hz: int | None = None = Field(None, alias="Equalizer500Hz")
    equalizer125_hz: int | None = None = Field(None, alias="Equalizer125Hz")
    equalizer4_k_hz: int | None = None = Field(None, alias="Equalizer4KHz")
    equalizer250_hz: int | None = None = Field(None, alias="Equalizer250Hz")
    equalizer8_k_hz: int | None = None = Field(None, alias="Equalizer8KHz")
    equalizer2_k_hz: int | None = None = Field(None, alias="Equalizer2KHz")
    equalizer31_hz: Optional[float] = Field(None, alias="Equalizer31Hz")
    equalizer1_k_hz: int | None = None = Field(None, alias="Equalizer1KHz")
    equalizer63_hz: int | None = None = Field(None, alias="Equalizer63Hz")


@dataclass
class Equaliser:
    """Equaliser Model."""

    gain: Gain | None = None
    frequency: Frequency | None = None


@dataclass
class FrequencyGain:
    """Frequency Gain Model."""

    equalizer_1khz: int | None = None
    equalizer_90hz: int | None = None
    equalizer_250hz: int | None = None
    equalizer_500hz: int | None = None
    equalizer_3khz: int | None = None
    equalizer_8khz: int | None = None

    def __post_init__(self):
        """Post Init Method."""
        if isinstance(self, dict) and hasattr(self, "Equalizer3KHz") and hasattr(self, "Equalizer1KHz") and hasattr(self, "Equalizer90Hz") and hasattr(self, "Equalizer250Hz") and hasattr(self, "Equalizer8KHz") and hasattr(self, "Equalizer500Hz"):
            self.equalizer_1khz = int(self["Equalizer1KHz"])
            self.equalizer_90hz = int(self["Equalizer90Hz"])
            self.equalizer_250hz = int(self["Equalizer250Hz"])
            self.equalizer_500hz = int(self["Equalizer500Hz"])
            self.equalizer_3khz = int(self["Equalizer3KHz"])
            self.equalizer_8khz = int(self["Equalizer8KHz"])


@dataclass
class NoiseGate:
    """Noise Gate Model."""

    threshold: int | None = None
    attack: int | None = None
    release: int | None = None
    enabled: bool | None = None
    attenuation: int | None = None


@dataclass
class Compressor:
    """Compressor Model."""

    threshold: int | None = None
    ratio: int | None = None
    attack: int | None = None
    release: int | None = None
    makeup_gain: int | None = None


@dataclass
class MicStatus:
    """Mic Status Model."""

    mic_type: str | None = None
    mic_gains: MicGains | None = None
    equaliser: Equaliser | None = None
    equaliser_mini: Equaliser | None = None
    noise_gate: NoiseGate | None = None
    compressor: Compressor | None = None


@dataclass
class Volumes:
    """Volumes Model."""

    mic: int
    line_in: int
    console: int
    system: int
    game: int
    chat: int
    sample: int
    music: int
    headphones: int
    mic_monitor: int
    line_out: int

    def __post_init__(self):
        """Post Init Method."""
        if isinstance(self, dict) and hasattr(self, "Mic") and hasattr(self, "LineIn") and hasattr(self, "Console") and hasattr(self, "System") and hasattr(self, "Game") and hasattr(self, "Chat") and hasattr(self, "Sample") and hasattr(self, "Music") and hasattr(self, "Headphones") and hasattr(self, "MicMonitor") and hasattr(self, "LineOut"):
            self.mic = int(self["Mic"])
            self.line_in = int(self["LineIn"])
            self.console = int(self["Console"])
            self.system = int(self["System"])
            self.game = int(self["Game"])
            self.chat = int(self["Chat"])
            self.sample = int(self["Sample"])
            self.music = int(self["Music"])
            self.headphones = int(self["Headphones"])
            self.mic_monitor = int(self["MicMonitor"])
            self.line_out = int(self["LineOut"])


@dataclass
class Levels:
    """Levels Model."""

    output_monitor: str
    volumes: Volumes
    submix_supported: bool | None = None
    submix: Any | None = None
    bleep: int | None = None
    deess: int | None = None


@dataclass
class RouterItem:
    """Router Item Model."""

    headphones: bool | None = None
    broadcast_mix: bool | None = None
    chat_mic: bool | None = None
    sampler: bool | None = None
    line_out: bool | None = None

    def __post_init__(self):
        """Post Init Method."""
        if isinstance(self, dict) and hasattr(self, "Headphones") and hasattr(self, "BroadcastMix") and hasattr(self, "ChatMic") and hasattr(self, "Sampler") and hasattr(self, "LineOut"):
            self.headphones = bool(self["Headphones"])
            self.broadcast_mix = bool(self["BroadcastMix"])
            self.chat_mic = bool(self["ChatMic"])
            self.sampler = bool(self["Sampler"])
            self.line_out = bool(self["LineOut"])


@dataclass
class Router:
    """Router Model."""

    microphone: RouterItem | None = None
    chat: RouterItem | None = None
    music: RouterItem | None = None
    game: RouterItem | None = None
    console: RouterItem | None = None
    line_in: RouterItem | None = None
    system: RouterItem | None = None
    samples: RouterItem | None = None

    def __post_init__(self):
        """Post Init Method."""
        if isinstance(self, dict) and hasattr(self, "Microphone") and hasattr(self, "Chat") and hasattr(self, "Music") and hasattr(self, "Game") and hasattr(self, "Console") and hasattr(self, "LineIn") and hasattr(self, "System") and hasattr(self, "Samples"):
            self.microphone = RouterItem(**self["Microphone"])
            self.chat = RouterItem(**self["Chat"])
            self.music = RouterItem(**self["Music"])
            self.game = RouterItem(**self["Game"])
            self.console = RouterItem(**self["Console"])
            self.line_in = RouterItem(**self["LineIn"])
            self.system = RouterItem(**self["System"])
            self.samples = RouterItem(**self["Samples"])


@dataclass
class CoughButton:
    """Cough Button Model."""

    is_toggle: bool | None = None
    mute_type: str | None = None
    state: str | None = None


@dataclass
class Colours:
    """Colours Model."""

    colour_one: str | None = None
    colour_two: str | None = None


@dataclass
class Fader:
    """Fader Model."""

    style: str | None = None
    colours: Colours | None = None


@dataclass
class Animation:
    """Animation Model."""

    supported: bool | None = None
    mode: str | None = None
    mod1: int | None = None
    mod2: int | None = None
    waterfall_direction: str | None = None


@dataclass
class Faders:
    """Faders Model."""

    a: Fader
    b: Fader
    c: Fader
    d: Fader

    def __post_init__(self):
        """Post Init Method."""
        if isinstance(self, dict) and hasattr(self, "A") and hasattr(self, "B") and hasattr(self, "C") and hasattr(self, "D"):
            self["A"] = Fader(**self["A"])
            self["B"] = Fader(**self["B"])
            self["C"] = Fader(**self["C"])
            self["D"] = Fader(**self["D"])


@dataclass
class Button:
    """Button Model."""

    colours: Colours
    off_style: str | None = None


@dataclass
class Buttons:
    """Buttons Model."""

    bleep: Button
    cough: Button
    fader1_mute: Button
    fader2_mute: Button
    fader3_mute: Button
    fader4_mute: Button

    def __post_init__(self):
        """Post Init Method."""
        if isinstance(self, dict) and hasattr(self, "Bleep") and hasattr(self, "Cough") and hasattr(self, "Fader1Mute") and hasattr(self, "Fader2Mute") and hasattr(self, "Fader3Mute") and hasattr(self, "Fader4Mute"):
            self["Bleep"] = Button(**self["Bleep"])
            self["Cough"] = Button(**self["Cough"])
            self["Fader1Mute"] = Button(**self["Fader1Mute"])
            self["Fader2Mute"] = Button(**self["Fader2Mute"])
            self["Fader3Mute"] = Button(**self["Fader3Mute"])
            self["Fader4Mute"] = Button(**self["Fader4Mute"])


@dataclass
class Global:
    """Global Model."""

    colour_one: str | None = None


@dataclass
class Accent:
    """Accent Model."""

    colour_one: str | None = None


@dataclass
class Simple:
    """Simple Model."""

    accent: Accent
    global_: Global | None = None

    def __post_init__(self):
        """Post Init Method."""
        if isinstance(self, dict) and hasattr(self, "Accent") and hasattr(self, "Global"):
            self["Accent"] = Accent(**self["Accent"])
            self["Global"] = Global(**self["Global"])


@dataclass
class Lighting:
    """Lighting Model."""

    animation: Animation
    faders: Faders
    buttons: Buttons
    simple: Simple
    sampler: dict[str, Any] | None = None
    encoders: dict[str, Any] | None = None


@dataclass
class Display:
    """Display Model."""

    gate: str | None = None
    compressor: str | None = None
    equaliser: str | None = None
    equaliser_fine: str | None = None


@dataclass
class Settings:
    """Settings Model."""

    display: Display | None = None
    mute_hold_duration: int | None = None
    vc_mute_also_mute_cm: bool | None = None


@dataclass
class ButtonDown:
    """Button Down Model."""

    bleep: bool | None = None
    cough: bool | None = None
    effect_fx: bool | None = None
    effect_hard_tune: bool | None = None
    effect_megaphone: bool | None = None
    effect_robot: bool | None = None
    effect_select1: bool | None = None
    effect_select2: bool | None = None
    effect_select3: bool | None = None
    effect_select4: bool | None = None
    effect_select5: bool | None = None
    effect_select6: bool | None = None
    fader1_mute: bool | None = None
    fader2_mute: bool | None = None
    fader3_mute: bool | None = None
    fader4_mute: bool | None = None
    sampler_bottom_left: bool | None = None
    sampler_bottom_right: bool | None = None
    sampler_clear: bool | None = None
    sampler_select_a: bool | None = None
    sampler_select_b: bool | None = None
    sampler_select_c: bool | None = None
    sampler_top_left: bool | None = None
    sampler_top_right: bool | None = None

    def __post_init__(self):
        """Post Init Method."""
        if isinstance(self, dict) and hasattr(self, "Bleep") and hasattr(self, "Cough") and hasattr(self, "EffectFx") and hasattr(self, "EffectHardTune") and hasattr(self, "EffectMegaphone") and hasattr(self, "EffectRobot") and hasattr(self, "EffectSelect1") and hasattr(self, "EffectSelect2") and hasattr(self, "EffectSelect3") and hasattr(self, "EffectSelect4") and hasattr(self, "EffectSelect5") and hasattr(self, "EffectSelect6") and hasattr(self, "Fader1Mute") and hasattr(self, "Fader2Mute") and hasattr(self, "Fader3Mute") and hasattr(self, "Fader4Mute") and hasattr(self, "SamplerBottomLeft") and hasattr(self, "SamplerBottomRight") and hasattr(self, "SamplerClear") and hasattr(self, "SamplerSelectA") and hasattr(self, "SamplerSelectB") and hasattr(self, "SamplerSelectC") and hasattr(self, "SamplerTopLeft") and hasattr(self, "SamplerTopRight"):
            self["Bleep"] = bool(self["Bleep"])
            self["Cough"] = bool(self["Cough"])
            self["EffectFx"] = bool(self["EffectFx"])
            self["EffectHardTune"] = bool(self["EffectHardTune"])
            self["EffectMegaphone"] = bool(self["EffectMegaphone"])
            self["EffectRobot"] = bool(self["EffectRobot"])
            self["EffectSelect1"] = bool(self["EffectSelect1"])
            self["EffectSelect2"] = bool(self["EffectSelect2"])
            self["EffectSelect3"] = bool(self["EffectSelect3"])
            self["EffectSelect4"] = bool(self["EffectSelect4"])
            self["EffectSelect5"] = bool(self["EffectSelect5"])
            self["EffectSelect6"] = bool(self["EffectSelect6"])
            self["Fader1Mute"] = bool(self["Fader1Mute"])
            self["Fader2Mute"] = bool(self["Fader2Mute"])
            self["Fader3Mute"] = bool(self["Fader3Mute"])
            self["Fader4Mute"] = bool(self["Fader4Mute"])
            self["SamplerBottomLeft"] = bool(self["SamplerBottomLeft"])
            self["SamplerBottomRight"] = bool(self["SamplerBottomRight"])
            self["SamplerClear"] = bool(self["SamplerClear"])
            self["SamplerSelectA"] = bool(self["SamplerSelectA"])
            self["SamplerSelectB"] = bool(self["SamplerSelectB"])
            self["SamplerSelectC"] = bool(self["SamplerSelectC"])
            self["SamplerTopLeft"] = bool(self["SamplerTopLeft"])
            self["SamplerTopRight"] = bool(self["SamplerTopRight"])


@dataclass
class Mixer:
    """Mixer Model."""

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


@dataclass
class Paths:
    """Paths Model."""

    profile_directory: str | None = None
    mic_profile_directory: str | None = None
    samples_directory: str | None = None
    presets_directory: str | None = None
    icons_directory: str | None = None


@dataclass
class Files:
    """Files Model."""

    profiles: list[str]
    mic_profiles: list[str]
    presets: list[str]
    samples: dict[str, Any]
    icons: list[str]


@dataclass
class Status:
    """Status Model."""

    config: Config
    mixers: dict[str, Mixer]
    paths: Paths
    files: Files


@dataclass
class Data:
    """Data Model."""

    status: Status

    def __post_init__(self):
        """Post Init Method."""
        if isinstance(self, dict) and hasattr(self, "Status"):
            self["Status"] = Status(**self["Status"])
