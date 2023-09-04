import json
from itertools import combinations
from typing import Any, List

from classes import Layout, Key, ModCombo
from keys import (
    left_thumb_keys,
    right_thumb_keys,
    left_alpha_keys,
    right_alpha_keys,
    left_mods,
    right_mods,
)
from model import Model


def gen_combis(lst: List[Any]) -> List[Any]:
    combinations_list = [
        list(combination)
        for r in range(1, len(lst) + 1)
        for combination in combinations(lst, r)
    ]
    return combinations_list


def name_combo(layer: str, mod_keys: List[Key], key: Key):
    return str.join("_", (layer, *(m.name for m in mod_keys), key.name)).lower()


with open("./keymap.json") as f:
    model = Model(**json.load(f))

layout = Layout(model=model)

left_crossed = (
    (x, y, z) for x in left_thumb_keys for y in left_mods for z in right_alpha_keys
)

layer_outputs = {
    "base": {
        "vars": [],
        "elements": [],
    },
    "num": {
        "vars": [],
        "elements": [],
    },
    "fun": {
        "vars": [],
        "elements": [],
    },
    # 'base': {
    #     'vars': [],
    #     'elements': [],
    # },
}

for t, m, a in left_crossed:
    pos = layout.position_keys(a)
    layer_a = pos.keys[t.layer_i] if t.layer_name != "base" else a

    mc = ModCombo(
        name_combo(t.layer_name, m.keys, layer_a),
        [t.key, m.position_key, layer_a],
        m.keys,
        m.position_key,
        layer_a,
    )

    layer_outputs[t.layer_name]["vars"].append(mc.combo.get_var())
    layer_outputs[t.layer_name]["elements"].append(mc.combo.get_element())

right_crossed = (
    (x, y, z) for x in right_thumb_keys for y in right_mods for z in left_alpha_keys
)

for t, m, a in right_crossed:
    pos = layout.position_keys(a)
    layer_a = pos.keys[t.layer_i] if t.layer_name != "base" else a

    mc = ModCombo(
        name_combo(t.layer_name, m.keys, layer_a),
        [t.key, m.position_key, layer_a],
        m.keys,
        m.position_key,
        layer_a,
    )

    layer_outputs[t.layer_name]["vars"].append(mc.combo.get_var())
    layer_outputs[t.layer_name]["elements"].append(mc.combo.get_element())

for value in layer_outputs["base"]["vars"]:
    print(value)

for value in layer_outputs["base"]["elements"]:
    print(value)
#
# a_pos = layout.position_keys(left_alpha_dict["BASE_A"])
#
# base_a = a_pos.keys[0]
# left_ctrl = left_mods[0]
# base_left_thumb = left_thumb_keys[0]
#
# base_a_ctrl = ModCombo(mod=left_ctrl, layer_key=base_left_thumb, key=base_a)
#
# print(base_a_ctrl.get_element())
# print(base_a_ctrl.get_name())
# print(base_a_ctrl.get_var())
