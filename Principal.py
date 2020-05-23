#Inicio de algoritmo, se leeran datos y arrojaran los resultados, lo demas sera mediante 
#los archivos de compañia quienes seran importados.
Padres = []
Hijos = []

N = 5

for k in range(N):
	CC=int(input('\nCedula: '))
	Nombre=input('Nombre: ')
	CantHijos=int(input('No. Hijos: '))
	Padres.append([CC, Nombre, CantHijos])
	Hijos.append([])
	for x in range(CantHijos):
		EstudiantesTI=int(input('\n\tTarjeta de Identidad: '))
		EstudiantesNota=int(input('\tDigite la nota \n\t(Del 1 al 5): '))
		from Funciones import estado
		EstudiantesEstado = estado(EstudiantesNota)
		Hijos[k].append([EstudiantesTI, EstudiantesNota, EstudiantesEstado])

#Salida de Datos		
print('\nResultados: ') 

for k in range(N):     
	print('\nNombre del padre: ',Padres[k][1])    
	print('No. de hijos: ',Padres[k][2])

	for x in range(len(Hijos[k])):
		print('\tHijo TI: ',Hijos[k][x][0]) 
		print('\tNota: ',Hijos[k][x][1])
		print('\tEstado : ',Hijos[k][x][2])
