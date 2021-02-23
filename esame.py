#Creo la classe da richiamare per evidenziare gli errori
class ExamException(Exception):
    pass 
#Creo la classe madre CSVFile
class CSVFile():
    #Inizializzo la classe con il proprio nome
    def __init__(self,name):
        self.name=name
        #Controllo che il file che viene passato sia una stringa, altrimenti dichiaro un errore
        if not isinstance(name,str):
            raise ExamException("Nome non corretto")
#Creo la classe figlia CSVTimeSeriesFile che richiama la classe madre CSVFile
class CSVTimeSeriesFile(CSVFile):
    #Inizializzo la classe CSVTimeSeriesFile per fare in modo che ottenga dei dati
    #su cui lavorare
    def get_data(self):
        try:
            open(self.name)
        except:
            raise ExamException("File non trovato")
        #Creo la lista che contenga altre liste
        Lista_di_Liste=[]
        #Uso un for che legga il contenuto della classe CSVFile
        for line in open(self.name,"r"):
            #Creo un array linea che divida l'epoch da temperatura tramite lo split
            linea=line.split(",")
            #Controllo se l'epoch passata all'interno del file sia un float tramite il try
            try:
                float(linea[0])
            #Altrimenti passa alla riga successiva
            except:
                continue
            #Controllo se la temperatura all'interno del file sia un float tramite il try
            try:
                float(linea[1])
            #Altrimenti passa alla riga successiva
            except:
                continue
            if linea[0]!="epoch":
                #Ho due variabili che ottengono i dati dall'array linea
                epoch=int(round(float(linea[0])))
                temp=float(linea[1])
                #Inserisco le due variabili nella Lista_Ausiliare
                #per conservare temporaneamente i dati
                Lista_Ausiliare=[epoch,temp]
                #Inserisco la Lista_Ausiliare nella Lista_di_Liste
                Lista_di_Liste.append(Lista_Ausiliare)
        #Ritorno la Lista_di_Liste
        return Lista_di_Liste

#Creo una funzione che mi restituisca quante volte ci sia stato un cambio di trend ogni determinata epoch, in questo caso
#la divisione è di ogni ora
def hourly_trend_changes(time_series):
    #Inizializzo variabile Inizio per indicare che non ci sono cambi nella prima temperatura,
    #la variabile Cambio_Trend per tenere conto di quante volte cambierà il trend nel corso del tempo
    #e la Lista_Cambio_Trend da ritornare per mostrare i vari cambi di trend per ogni ora
    Inizio=True
    Cambio_Trend=0
    Lista_Cambio_Trend=[]
    #Inizio a confrontare le varie temperature per controllare l'andamento del trend
    for i in range(len(time_series)):
        #Per evitare di uscire dalla lista, questa parte conclude il ciclo for in anticipo e aggiunge l'ultimo
        #cambio alla Lista_Cambio_Trend
        if i == len(time_series)-1:
            #Controllo se il trend risulta negativo
            if Trend=="Negativo":
                if time_series[i-1][1]>time_series[i][1]:
                    #Il trend non è cambiato, quindi passa avanti
                    Trend="Negativo"
                if time_series[i-1][1]<time_series[i][1]:
                    #Il trend è cambiato in positivo, quindi aumento il conteggio
                    Trend="Positivo"
                    Cambio_Trend+=1
                if time_series[i-1][1]==time_series[i][1]:
                    #Il trend è cambiato in invariato  , quindi aumento il conteggio  
                    Trend="Invariato"
                    Cambio_Trend+=1
            #Controllo se il trend risulta positivo
            if Trend=="Positivo":
                if time_series[i-1][1]>time_series[i][1]:
                    #Il trend è cambiato in negativo, quindi aumento il conteggio
                    Trend="Negativo"
                    Cambio_Trend+=1
                if time_series[i-1][1]<time_series[i][1]:
                    #Il trend non è cambiato, quindi passa avanti
                    Trend="Positivo"
                if time_series[i-1][1]==time_series[i][1]:
                    #Il trend è cambiato in invariato  , quindi aumento il conteggio  
                    Trend="Invariato"
                    Cambio_Trend+=1
            #Controllo se il trend risulta invariato
            if Trend=="Invariato":
                if time_series[i-1][1]>time_series[i][1]:
                    #Il trend è cambiato in negativo, quindi aumento il conteggio
                    Trend="Negativo"
                    Cambio_Trend+=1
                if time_series[i-1][1]<time_series[i][1]:
                    #Il trend è cambiato in positivo, quindi aumento il conteggio
                    Trend="Positivo"
                    Cambio_Trend+=1
                if time_series[i-1][1]==time_series[i][1]:
                    #Il trend non è cambiato, quindi passa avanti
                    Trend="Invariato"
            Lista_Cambio_Trend.append(Cambio_Trend)
            break
        if not Inizio:
            #Controllo se il trend risulta negativo
            if Trend=="Negativo":
                if time_series[i-1][1]>time_series[i][1]:
                    #Il trend non è cambiato, quindi passa avanti
                    Trend="Negativo"
                if time_series[i-1][1]<time_series[i][1]:
                    #Il trend è cambiato in positivo, quindi aumento il conteggio
                    Trend="Positivo"
                    Cambio_Trend+=1
                if time_series[i-1][1]==time_series[i][1]:
                    #Il trend è cambiato in invariato  , quindi aumento il conteggio  
                    Trend="Invariato"
                    Cambio_Trend+=1
            #Controllo se il trend risulta positivo
            if Trend=="Positivo":
                if time_series[i-1][1]>time_series[i][1]:
                    #Il trend è cambiato in negativo, quindi aumento il conteggio
                    Trend="Negativo"
                    Cambio_Trend+=1
                if time_series[i-1][1]<time_series[i][1]:
                    #Il trend non è cambiato, quindi passa avanti
                    Trend="Positivo"
                if time_series[i-1][1]==time_series[i][1]:
                    #Il trend è cambiato in invariato  , quindi aumento il conteggio  
                    Trend="Invariato"
                    Cambio_Trend+=1
            #Controllo se il trend risulta invariato
            if Trend=="Invariato":
                if time_series[i-1][1]>time_series[i][1]:
                    #Il trend è cambiato in negativo, quindi aumento il conteggio
                    Trend="Negativo"
                    Cambio_Trend+=1
                if time_series[i-1][1]<time_series[i][1]:
                    #Il trend è cambiato in positivo, quindi aumento il conteggio
                    Trend="Positivo"
                    Cambio_Trend+=1
                if time_series[i-1][1]==time_series[i][1]:
                    #Il trend non è cambiato, quindi passa avanti
                    Trend="Invariato"
        if Inizio:
            if time_series[i][1]>time_series[i+1][1]:
                #La temperatura sta diminuendo
                Trend="Negativo"
                Inizio=False
            if time_series[i][1]<time_series[i+1][1]:
                #La temperatura sta aumentando
                Trend="Positivo"
                Inizio=False
            if time_series[i][1]==time_series[i+1][1]:
                #La temperatura è rimasta invariata
                Trend="Invariato"
                Inizio=False
        #Controllo se l'epoch precedente non faccia parte della stessa ora dell'epoch corrente, in quel caso aggiungo
        #alla Lista_Cambio_Trend quanto volte sia cambiato il trend in quell'ora e infine resetto il contatore per 
        #cominciare un'altra ora
        if time_series[i][0]-(time_series[i][0]%3600)!=time_series[i+1][0]-(time_series[i+1][0]%3600):
            Lista_Cambio_Trend.append(Cambio_Trend)
            Cambio_Trend=0
    #Ritorno la Lista_Cambio_Trend
    return Lista_Cambio_Trend