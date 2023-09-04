in rosetta shell, generate json:

```shell
qmk c2json -kb ergodox_ez/glow -km JeMorriso --no-cpp /Users/jerry/qmk_firmware/keyboards/ergodox_ez/keymaps/JeMorriso/keymap.c > ./keymap.json
```

in shell with virtualenv active, generate pydantic models:

```shell
datamodel-codegen --input keymap.json --input-file-type json --output model.py
```
