import playsound

def reproducir_audio(ruta_archivo):
    playsound.playsound(ruta_archivo)

def escuchar_traduccion(palabra_a_escuchar):
    if palabra_a_escuchar == "achik":
        reproducir_audio("voz1.mp3")
    elif palabra_a_escuchar == "alli":
        reproducir_audio("voz2.mp3")
    elif palabra_a_escuchar == "ayllu":
        reproducir_audio("voz3.mp3")
    elif palabra_a_escuchar == "chaki":
        reproducir_audio("voz4.mp3")
    elif palabra_a_escuchar == "chaska":
        reproducir_audio("voz5.mp3")
    elif palabra_a_escuchar == "churay":
        reproducir_audio("voz6.mp3")
    elif palabra_a_escuchar == "inti":
        reproducir_audio("voz7.mp3")
    elif palabra_a_escuchar == "killa":
        reproducir_audio("voz8.mp3")
    elif palabra_a_escuchar == "kawsay":
        reproducir_audio("voz9.mp3")
    elif palabra_a_escuchar == "maki":
        reproducir_audio("voz10.mp3")
    elif palabra_a_escuchar == "mama":
        reproducir_audio("voz11.mp3")
    elif palabra_a_escuchar == "mashi":
        reproducir_audio("voz12.mp3")
    elif palabra_a_escuchar == "mikuy":
        reproducir_audio("voz13.mp3")
    elif palabra_a_escuchar == "ñawi":
        reproducir_audio("voz14.mp3")
    elif palabra_a_escuchar == "pacha":
        reproducir_audio("voz15.mp3")
    elif palabra_a_escuchar == "pukllay":
        reproducir_audio("voz16.mp3")
    elif palabra_a_escuchar == "rimay":
        reproducir_audio("voz17.mp3")
    elif palabra_a_escuchar == "runa":
        reproducir_audio("voz18.mp3")
    elif palabra_a_escuchar == "sacha":
        reproducir_audio("voz19.mp3")
    elif palabra_a_escuchar == "sami":
        reproducir_audio("voz20.mp3")
    elif palabra_a_escuchar == "shimi":
        reproducir_audio("voz21.mp3")
    elif palabra_a_escuchar == "sisa":
        reproducir_audio("voz22.mp3")
    elif palabra_a_escuchar == "taita":
        reproducir_audio("voz23.mp3")
    elif palabra_a_escuchar == "tukuy":
        reproducir_audio("voz24.mp3")
    elif palabra_a_escuchar == "tuta":
        reproducir_audio("voz25.mp3")
    elif palabra_a_escuchar == "ushai":
        reproducir_audio("voz26.mp3")
    elif palabra_a_escuchar == "wasi":
        reproducir_audio("voz27.mp3")
    elif palabra_a_escuchar == "yaku":
        reproducir_audio("voz28.mp3")
    elif palabra_a_escuchar == "yana":
        reproducir_audio("voz29.mp3")
    elif palabra_a_escuchar == "yura":
        reproducir_audio("voz30.mp3")
    elif palabra_a_escuchar == "wawa":
        reproducir_audio("voz31.mp3")
    elif palabra_a_escuchar == "yachay":
        reproducir_audio("voz32.mp3")
    elif palabra_a_escuchar == "yuyay":
        reproducir_audio("voz33.mp3")
    elif palabra_a_escuchar == "kuyay":
        reproducir_audio("voz34.mp3")
    elif palabra_a_escuchar == "kuychi":
        reproducir_audio("voz35.mp3")
    elif palabra_a_escuchar == "muyu":
        reproducir_audio("voz36.mp3")
    elif palabra_a_escuchar == "nina":
        reproducir_audio("voz37.mp3")
    elif palabra_a_escuchar == "puka":
        reproducir_audio("voz38.mp3")
    elif palabra_a_escuchar == "rikuy":
        reproducir_audio("voz39.mp3")
    elif palabra_a_escuchar == "sumaq":
        reproducir_audio("voz40.mp3")
    elif palabra_a_escuchar == "taki":
        reproducir_audio("voz41.mp3")
    elif palabra_a_escuchar == "tiyana":
        reproducir_audio("voz42.mp3")
    elif palabra_a_escuchar == "zarapana":
        reproducir_audio("voz43.mp3")
    elif palabra_a_escuchar == "mama llacta":
        reproducir_audio("voz44.mp3")
    elif palabra_a_escuchar == "chiri":
        reproducir_audio("voz45.mp3")
    else:
        print("La palabra no tiene una traducción con audio disponible.")
