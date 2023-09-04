from classes import LayerKey, Key, Mod

left_thumb_keys = [
    LayerKey(
        layer_name="base",
        layer_i=0,
        key=Key(name="COMBO_THUMB_BASE_LEFT", keycode="LT(NAV, KC_SPACE)"),
    ),
]

right_thumb_keys = [
    LayerKey(
        layer_name="base",
        layer_i=0,
        key=Key(name="COMBO_THUMB_BASE_RIGHT", keycode="LT(NUM, KC_BACKSPACE)"),
    ),
    LayerKey(
        layer_name="num",
        layer_i=4,
        key=Key(name="COMBO_THUMB_NUM", keycode="LT(SYM, KC_ENTER)"),
    ),
    LayerKey(
        layer_name="fun",
        layer_i=6,
        key=Key(name="COMBO_THUMB_FUN", keycode="LT(FUN, KC_DELETE)"),
    ),
]

left_alpha_keys = [
    Key(name="BASE_A", keycode="CTL_T(KC_A)"),
    Key(name="BASE_B", keycode="KC_B"),
    Key(name="BASE_C", keycode="KC_C"),
    Key(name="BASE_D", keycode="KC_D"),
    Key(name="BASE_F", keycode="MEH_T(KC_F)"),
    Key(name="BASE_G", keycode="KC_G"),
    Key(name="BASE_P", keycode="KC_P"),
    Key(name="BASE_Q", keycode="KC_Q"),
    Key(name="BASE_R", keycode="OPT_T(KC_R)"),
    Key(name="BASE_S", keycode="CMD_T(KC_S)"),
    Key(name="BASE_T", keycode="SFT_T(KC_T)"),
    Key(name="BASE_V", keycode="LT(MOUSE,KC_V)"),
    Key(name="BASE_W", keycode="HYPR_T(KC_W)"),
    Key(name="BASE_X", keycode="KC_X"),
    Key(name="BASE_Z", keycode="KC_Z"),
    Key(name="BASE_SPACE", keycode="LT(NAV, KC_SPACE)"),
    Key(name="BASE_ESC", keycode="LT(MEDIA, KC_ESC)"),
    Key(name="BASE_TAB", keycode="LT(0, KC_TAB)"),
]
left_alpha_dict = {k.name: k for k in left_alpha_keys}

right_alpha_keys = [
    Key(name="BASE_E", keycode="CMD_T(KC_E)"),
    Key(name="BASE_H", keycode="KC_H"),
    Key(name="BASE_I", keycode="OPT_T(KC_I)"),
    Key(name="BASE_J", keycode="KC_J"),
    Key(name="BASE_K", keycode="KC_K"),
    Key(name="BASE_L", keycode="KC_L"),
    Key(name="BASE_M", keycode="KC_M"),
    Key(name="BASE_N", keycode="SFT_T(KC_N)"),
    Key(name="BASE_O", keycode="CTL_T(KC_O)"),
    Key(name="BASE_U", keycode="MEH_T(KC_U)"),
    Key(name="BASE_Y", keycode="HYPR_T(KC_Y)"),
    Key(name="BASE_QUOTE", keycode="KC_QUOTE"),
    Key(name="BASE_COMMA", keycode="KC_COMMA"),
    Key(name="BASE_DOT", keycode="KC_DOT"),
    Key(name="BASE_SLASH", keycode="KC_SLASH"),
    Key(name="BASE_ENTER", keycode="LT(SYM, KC_ENTER)"),
    Key(name="BASE_BACKSPACE", keycode="LT(NUM, KC_BACKSPACE)"),
    Key(name="BASE_DELETE", keycode="LT(FUN, KC_DELETE)"),
]
right_alpha_dict = {k.name: k for k in right_alpha_keys}

ctl = Key(name="C", keycode="C")
alt = Key(name="A", keycode="A")
gui = Key(name="G", keycode="G")
sft = Key(name="S", keycode="S")

left_mods = [
    Mod(keys=[ctl], position_key=left_alpha_dict["BASE_A"]),
    Mod(keys=[alt], position_key=left_alpha_dict["BASE_R"]),
    Mod(keys=[gui], position_key=left_alpha_dict["BASE_S"]),
    Mod(keys=[sft], position_key=left_alpha_dict["BASE_T"]),
    Mod(keys=[ctl, alt], position_key=left_alpha_dict["BASE_Q"]),
    Mod(keys=[ctl, gui], position_key=left_alpha_dict["BASE_P"]),
    Mod(keys=[ctl, sft], position_key=left_alpha_dict["BASE_Z"]),
    Mod(keys=[alt, gui], position_key=left_alpha_dict["BASE_D"]),
    Mod(keys=[alt, sft], position_key=left_alpha_dict["BASE_X"]),
    Mod(keys=[gui, sft], position_key=left_alpha_dict["BASE_C"]),
    Mod(keys=[ctl, alt, gui], position_key=left_alpha_dict["BASE_B"]),
    Mod(keys=[ctl, alt, sft], position_key=left_alpha_dict["BASE_F"]),
    Mod(keys=[ctl, gui, sft], position_key=left_alpha_dict["BASE_G"]),
    Mod(keys=[alt, gui, sft], position_key=left_alpha_dict["BASE_V"]),
    Mod(keys=[ctl, alt, gui, sft], position_key=left_alpha_dict["BASE_W"]),
]

right_mods = [
    Mod(keys=[ctl], position_key=right_alpha_dict["BASE_O"]),
    Mod(keys=[alt], position_key=right_alpha_dict["BASE_I"]),
    Mod(keys=[gui], position_key=right_alpha_dict["BASE_E"]),
    Mod(keys=[sft], position_key=right_alpha_dict["BASE_N"]),
    Mod(keys=[ctl, alt], position_key=right_alpha_dict["BASE_QUOTE"]),
    Mod(keys=[ctl, gui], position_key=right_alpha_dict["BASE_L"]),
    Mod(keys=[ctl, sft], position_key=right_alpha_dict["BASE_SLASH"]),
    Mod(keys=[alt, gui], position_key=right_alpha_dict["BASE_H"]),
    Mod(keys=[alt, sft], position_key=right_alpha_dict["BASE_DOT"]),
    Mod(keys=[gui, sft], position_key=right_alpha_dict["BASE_COMMA"]),
    Mod(keys=[ctl, alt, gui], position_key=right_alpha_dict["BASE_J"]),
    Mod(keys=[ctl, alt, sft], position_key=right_alpha_dict["BASE_U"]),
    Mod(keys=[ctl, gui, sft], position_key=right_alpha_dict["BASE_M"]),
    Mod(keys=[alt, gui, sft], position_key=right_alpha_dict["BASE_K"]),
    Mod(keys=[ctl, alt, gui, sft], position_key=right_alpha_dict["BASE_Y"]),
]
