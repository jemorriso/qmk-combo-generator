import json
from classes import LayerKey, Layout, Key, Combo
from model import Model

with open("./keymap.json") as f:
    model = Model(**json.load(f))

layout = Layout(model=model)

num_layer_key = LayerKey(
    layer_name="num", layer_i=4, key=Key(name="BASE_E", keycode="KC_E")
)
num_other_key = Key(name="BASE_I", keycode="KC_I")
one = Key(name="KC_1", keycode="KC_1")
one_combo = Combo(layer_key=num_layer_key, other_key=num_other_key, key=one)

print(one_combo.get_element())
print(one_combo.get_name())
print(one_combo.get_var())

foo = True
