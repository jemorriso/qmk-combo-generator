from typing import List, Optional
import copy
from dataclasses import dataclass
from model import Model


class Key:
    def __init__(self, name: str, keycode: Optional[str] = None) -> None:
        self.name = name
        self.keycode = keycode if keycode is not None else name


@dataclass
class LayerKey:
    layer_name: str
    layer_i: int
    key: Key


@dataclass
class Mod:
    keys: List[Key]
    position_key: Key

    def modify(self, key: Key) -> str:
        def mod(mod_keys: List[Key]):
            if len(mod_keys) == 0:
                return key.name

            curr_key = mod_keys.pop()
            return f"{curr_key.name}({mod(mod_keys)})"

        return mod(copy.deepcopy(self.keys))


@dataclass
class Pos:
    i: int
    keys: List[Key]


@dataclass
class Layout:
    model: Model

    def position_keys(self, key: Key) -> Pos:
        pos_i = self.model.layers[0].index(key.keycode)
        return Pos(i=pos_i, keys=[Key(x[pos_i]) for x in self.model.layers])


@dataclass
class Combo:
    name: str
    action: str
    keys: List[Key]

    def get_var(self) -> str:
        return f"const uint16_t PROGMEM {self.name}[] = {{{str.join(', ', (x.name for x in self.keys))}, COMBO_END}};"

    def get_element(self) -> str:
        return f"COMBO({self.name}, {self.action})"


@dataclass
class ModCombo:
    def __init__(
        self,
        combo_name: str,
        combo_keys: List[Key],
        mod_keys: List[Key],
        mod_position_key: Key,
        key_to_mod: Key,
    ) -> None:
        self.mod = Mod(keys=mod_keys, position_key=mod_position_key)
        combo_action = self.mod.modify(key_to_mod)
        self.combo = Combo(name=combo_name, action=combo_action, keys=combo_keys)
