SD_task1

En este proyecto utilizamos GRPC (middleware de RPC binario) para la comunicación cliente - workstation.

methods.proto: 
	Fichero en el que se especifican los campos que debe recibir la función, o "contrato" (necesario porque trabajamos con RPC binario). 
	En este definimos un solo mensaje genérico para toda la comunicación por escalabilidad debido a que si queremos añadir una nueva función o servicio en el master no hace falta modificar los mensages. 
	El mensaje tiene definidos 6 campos: 
		-error - Que se utiliza para devolver códigos de error en caso de falla de algún elemento del sistema.
		-worker - Que se utiliza cuando un cliente quiere hacer referencia a un worker mediante su id, para eliminarlo por ejemplo.
		-command - Que utilizamos para determinar que operación queremos que se realize de entre las siguientes crear worker, borrar worker, listar workers y contar o enumerar palabras de un fichero.
		-url - Dirección de el/los ficheros que queremos que se procesen. 
		-list - Que lo utilizamos para devolver listas, como en el caso de el comando enumerar.
		-result - Que lo utilizamos para devolver resultados genéricos al cliente. 

Funcionamiento general del proyecto:
	El cliente realiza una petición síncrona al servidor master que gestiona las peticiones.
	El manager(master.py) coge las peticiones de los clientes y encola los jobs en forma de JSON en una cola de redis. 
	Cuando el cliente realiza una petición se crea una cola aparte solo para esa petición donde se irán almacenando los resultados de los jobs en caso de múltiples ficheros a procesar. 
	Redis gestiona automaticamente la creación de colas y posterior borrado en caso de estar vacías.
	En la cola principal de jobs se nos creará un job adicional, para el caso de las invocaciones multiples, que consistirá en realizar la suma de los resultados de todos los jobs que teniamos en esta cola de request.
	El worker (worker.py) se encarga de procesar los jobs de la cola y encolar los resultados en la cola de request. Este mirará en la cola si hay jobs disponibles. En caso de que los haya, este realizará el job (que puede ser countWords o enumerateWords) cogiendo los datos de la URL especificada. Una vez finalizado el job, encolará el resultado en la cola de request. También puede realizar el job de sumar todos los resultados de una invocación multiple. El worker que realice este job será el que enviará el mensaje al cliente. (para invocación simple será el worker que realice el job). 

Ejecución:
Antes de ejecutar el proyecto, hay que tener ejecutando: 
	-redis-server(para el almacenamiento)
	-server http sobre el fichero files del proyecto(contiene ciertos ficheros que podemos obtener haciendo peticiones http)
	-master.py(que es el manager de todas las peticiones que llegan de los clientes y de los workers). 

Las peticiones se ejecutan con el fichero client.py, y para que estas comienzen a ejecutarse debemos tener al menos 1 worker. En caso de no tener workers, el programa se quedará esperando sin devolver una respuesta.
En caso de llamar al client sin parametros, se activa el help automaticamente mostrando las acciones que puede realizar este. 

Por ejemplo:
#Creamos el worker
Python3 client.py create
#Ejecutamos una petición de contar palabras
Python3 client.py count http://localhost:80/sample1.txt
#Ejecutamos una petición de enumerar palabras
Python3 client.py enumerate http://localhost:80/sample1.txt
#Ejecutamos una petición de contar palabras con invocación múltiple
Python3 client.py count http://localhost:80/sample1.txt http://localhost:80/sample2.txt
#Ejecutamos una petición de enumerar palabras con invocación múltiple
Python3 client.py enumerate http://localhost:80/sample1.txt http://localhost:80/sample2.txt
#Eliminamos un worker
Python3 client.py delete <id>
#Listamos todos los workers
Python3 client.py list
