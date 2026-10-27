import tkinter as tk
#Betöltjük a tkinter könyvtárat, és tk néven hivatkozunk rá.

#ablak letrehozasa
ablak = tk.Tk()

#ablak cime
ablak.title("Cicus")

#ablalk merete
ablak.geometry("500x520")
ablak.minsize(450, 450)
ablak.resizable(True, True)

#hatterszin
ablak.configure(bg="white")

boldogsag = 50 #kezdo boldogsag
ehseg = 30 #kezdo jollakottsaf

cim = tk.Label(
    ablak,
    text="Szaros",
    font=("Arial", 18, "bold"),
    bg="#ffe6f2", #hatterszin
    fg="#d63384" #betuszin
)

cim.pack(pady=8) #megjeleniti a FELIRATOT, ALUL ES FELUL 8 PIXEL TERKOZZEL,
#tobbi tk.Label() zgyanigy mukodik

cica = tk.Label(
    ablak,
    text=" /\\_/\\\\\n( o.o )\n > ^ <",
    font=("Consolas", 19),
    bg="#ffe6f2",
    justify="center"
)
cica.pack(pady=5)

uzenet = tk.Label(
    ablak,
    text="Deziii",
    font=("Arial", 13),
    bg="#ffe6f2"
)

uzenet.pack(pady=3)

boldogsag_szoveg = tk.Label(
    ablak,
    text=f"Boldogság: {boldogsag}/100",
    font=("Arial", 14),
    bg="#ffe6f2"
)

boldogsag_szoveg.pack(pady=5)

boldogsag_csik = tk.Canvas(
    ablak,
    width=250,
    height=20,
    bg="white",
    highlightthickness=0 #eltunteti a rajzterulet koruli keretet
)

boldogsag_csik.pack(pady=5)

def csik_frissites():  # a boldoigsagcsik ujrarajzolasaert felel
    boldogsag_csik.delete("all") # torli a korabban rajzolt alakzatot

    boldogsag_csik.create_oval( #ovalis alakzatot rajzol, csik lekerekitett vege
        0, 0, 20, 20,
        fill="#ffe6f2", outline="" # fill-az alakzat belso szine, outline- eltunteti az alakzat korvonalat
    )
    boldogsag_csik.create_rectangle( #teglalapot rajzol, kitoltjuk a csik kozepsoi reszet
        10, 0, 240, 20,
        fill="#ffe6f2", outline=""
    )
    boldogsag_csik.create_oval(
        230, 0, 250, 20,
        fill="#ffe6f2", outline=""
    )

    szelesseg = 250 * boldogsag / 100 #mennyire legyen feltoltve a csik

    if szelesseg > 0: # csak akkor rajzol kitoltest, ha az ertek nagyobb nullanal
        boldogsag_csik.create_oval(
            0, 0, 20, 20,
            fill="#ff69b4", outline=""
        )
        if szelesseg > 10:
            boldogsag_csik.create_rectangle(
                10, 0, max(10, szelesseg - 10), 20,
                fill="#ff69b4", outline=""
            )
        if szelesseg >= 20:
            boldogsag_csik.create_oval(
                szelesseg - 20, 0, szelesseg, 20,
                fill="#ff69b4", outline=""
            )

csik_frissites()


ehseg_szoveg = tk.Label(
    ablak,
    text=f"Jóllakottság: {ehseg}/100",
    font=("Arial", 14),
    bg="white"
)
ehseg_szoveg.pack(pady=5)

ehseg_csik = tk.Canvas(
    ablak,
    width=250,
    height=20,
    bg="white",
    highlightthickness=0
)
ehseg_csik.pack(pady=5)


def ehseg_frissites(): #ujrarajzolja a jollakottsagcsikot
    ehseg_csik.delete("all") #torli a regi rajzot

    #Lekerekített háttér
    ehseg_csik.create_oval(
        0, 0, 20, 20,
        fill="#ffe6f2", outline=""
    )
    ehseg_csik.create_rectangle(
        10, 0, 240, 20,
        fill="#ffe6f2", outline=""
    )
    ehseg_csik.create_oval(
        230, 0, 250, 20,
        fill="#ffe6f2", outline=""
    )

    szelesseg = 250 * ehseg / 100

    if szelesseg > 0:
        ehseg_csik.create_oval(
            0, 0, 20, 20,
            fill="#ff9eb5", outline=""
        )

        if szelesseg > 10:
            ehseg_csik.create_rectangle(
                10, 0, max(10, szelesseg - 10), 20,
                fill="#ff9eb5", outline=""
            )

        if szelesseg >= 20:
            ehseg_csik.create_oval(
                szelesseg - 20, 0, szelesseg, 20,
                fill="#ff9eb5", outline=""
            )


ehseg_frissites()


gomb_keret = tk.Frame(ablak, bg="white") #tarolo a gombok szamara
gomb_keret.pack(pady=10) #elhelyezi a gombok tarolojat az ablakban


#ETETES!!
def etetes(): #ez a fuggveny fut le amikor az etetes gombra kattontok
    global ehseg #engedelyezi a kulso ehseg valtozo modositasat

    if ehseg == 100:
        cica.config(text=" /\\_/\\\\\n( ^.^ )\n > ^ <")
        uzenet.config(text="Good girl")
    else: #ha meg nincs teljesen jollakva
        ehseg = min(100, ehseg + 20)

        cica.config(text=" /\\_/\\\\\n( ^o^ )\n > ^ <")
        uzenet.config(text="Meowowow^^ <33")

    ehseg_szoveg.config(
        text=f"Jóllakottság: {ehseg}/100" # kiirja az aktualis erteket
    )

    ehseg_frissites() #frissiti a jollakottsagcsikot



etetes_gomb = tk.Button(
    gomb_keret,
    text="Etetés",
    font=("Arial", 14),
    bg="#ffb3d9",
    activebackground="#ff85c1",
    relief="flat", #lapos megjelenes, kiemelkedo keret nelk,ul
    padx=10, #belso vizszintes terkoz
    pady=5, #belso fuggoleges terkoz
    command=etetes #kattintaskor az etetes fuggvenyt inditja
)
etetes_gomb.pack(side="left", padx=5) #balrol jobbra rendezi a gombokat

#SIMOGATAS!!!
def simogatas():
    global boldogsag #a fuggvenyen belul is ezt a kulso valtozot szeretnem modositanui

    boldogsag = min(100, boldogsag + 10) #min- ket szam kozul a kisebbet valasztja

    if boldogsag == 100: #akkor fut le ha a boldogsag pontsan 100
        cica.config(text=" /\\_/\\\\\n( >w< )\n > ^ <")
    else:
        cica.config(text=" /\\_/\\\\\n( ^.^ )\n > ^ <")

    boldogsag_szoveg.config(
        text=f"Boldogság: {boldogsag}/100"
    )

    csik_frissites()

simogatas_gomb = tk.Button(
    gomb_keret,
    text="Simogatás",
    font=("Arial", 14),
    bg="#ffb3d9",
    activebackground="#ff85c1",
    relief="flat",
    padx=10,
    pady=5,
    command=simogatas
)
simogatas_gomb.pack(side="left", padx=5)

#VERES
def bantas():
    global boldogsag

    boldogsag = max(0, boldogsag - 20) #csokkenti a boldogssgot 20-szal, de nem engedi 0 alá

    if boldogsag <= 20: #akkor fut le ha a korabbi feltetel nem teljesult, es a boldogsag 20 v annal kevesebb
        cica.config(text=" /\\_/\\\\\n( T.T )\n > ^ <")
        uzenet.config(text="Krrvaa >:(")
    else:
        cica.config(text=" /\\_/\\\\\n( >.< )\n > ^ <")
        uzenet.config(text="Csicskam vagy stnm!!!")

    boldogsag_szoveg.config(
        text=f"Boldogság: {boldogsag}/100"
    )
    csik_frissites()
bantas_gomb = tk.Button(
    gomb_keret,
    text="Verés",
    font=("Arial", 14),
    bg="#ff9999",
    activebackground="#ff85c1",
    relief="flat",
    padx=10,
    pady=5,
    command=bantas
)

bantas_gomb.pack(side="left", padx=5)


#JATEK
def jatek(): #jatek gomb
    global boldogsag, ehseg

    if ehseg <= 10:
        cica.config(text=" /\\_/\\\\\n( T.T )\n > ^ <")
        uzenet.config(text="Éhes vagyok cseléd!")
    else:
        boldogsag = min(100, boldogsag + 15)
        ehseg = max(0, ehseg - 10)

        cica.config(text=" /\\_/\\\n( >w< )\n  > ^ <  🧶")
        uzenet.config(text="Meoow!")

    boldogsag_szoveg.config(text=f"Boldogság: {boldogsag}/100") #frissiti a boldogsag feliratat
    ehseg_szoveg.config(text=f"Jóllakottság: {ehseg}/100") #frissiti a jollakottsag feliratat

    csik_frissites() #ujrarajzolja a boldogssgcsikot
    ehseg_frissites() #ujrarajzolja a jollakottsagcsikot


jatek_gomb = tk.Button(
    gomb_keret,
    text="Játék",
    font=("Arial", 14),
    bg="#ffb3d9",
    activebackground="#ff85c1",
    relief="flat",
    padx=10,
    pady=5,
    command=jatek
)

jatek_gomb.pack(side="left", padx=5)


#ablak megjelenitese
ablak.mainloop()