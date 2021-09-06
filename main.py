# Programa Python para ilustrar um cronômetro
# usando Tkinter
#importing as bibliotecas necessárias
import tkinter as Tkinter
from datetime import datetime
counter = 66600
running = False
def counter_label(label):
	def count():
		if running:
			global counter

			# Para gerenciar o atraso inicial.
			if counter==66600:			
				display="Starting..."
			else:
				tt = datetime.fromtimestamp(counter)
				string = tt.strftime("%H:%M:%S")
				display=string

			label['text']=display # Ou label.config (text = display)

                    # label.after (arg1, arg2) atrasa em
                    # primeiro argumento fornecido em milissegundos
                    # e então chama a função fornecida como segundo argumento.
                    # Geralmente como aqui, precisamos chamar o
                    # função na qual está presente repetidamente.
                    # Atrasos em 1000ms = 1 segundo e contagem de chamadas novamente.
			label.after(1000, count)
			counter += 1

	# Disparando o início do contador.
	count()	

# função de início do cronômetro
def Start(label):
	global running
	running=True
	counter_label(label)
	start['state']='disabled'
	stop['state']='normal'
	reset['state']='normal'

# Função de parada do cronômetro
def Stop():
	global running
	start['state']='normal'
	stop['state']='disabled'
	reset['state']='normal'
	running = False

# Função de reset do cronômetro
def Reset(label):
	global counter
	counter=66600

	# Se pousar for pressionado após pressionar parar.
	if running==False:	
		reset['state']='disabled'
		label['text']='Welcome!'

	# Se reset for pressionado enquanto o cronômetro estiver em execução.
	else:			
		label['text']='Starting...'

root = Tkinter.Tk()
root.title("Stopwatch")

# Corrigindo o tamanho da janela.
root.minsize(width=250, height=70)
label = Tkinter.Label(root, text="Welcome!", fg="black", font="Verdana 30 bold")
label.pack()
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6, command=lambda:Start(label))
stop = Tkinter.Button(f, text='Stop',width=6,state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label))
f.pack(anchor = 'center',pady=5)
start.pack(side="left")
stop.pack(side ="left")
reset.pack(side="left")
root.mainloop()
