SD_task1

En este proyecto utilizamos GRPC (middleware de RPC binario) para la comunicación cliente - workstation.
methods.proto: Fichero en el que se especifican los campos que debe recibir la función, o "contrato" (necesario porque trabajamos con RPC binario). En este definimos un solo mensaje genérico para toda la comunicación (por simplicidad). Este mensaje tiene definidos 6 campos: error, worker(worker que realiza el job), command(operación: puede ser el job o create-delete-list worker), url(url de donde el worker cogera los datos), list y result(resultado del job). Además tenemos definido 1 campo de servicios. 
Hemos usado JSON para simplificar el intercambio de datos.

Funcionamiento general del proyecto:
El cliente realiza una petición y espera a recibir una respuesta.
El manager(master.py) coge las peticiones de los clientes y encola los jobs. Tenemos una cola redis para encolar los jobs, además, cuando el cliente realiza una petición se crea una cola aparte solo para esa petición(cola de request).(redis gestiona automaticamente cuando se borra esta cola en función de si está llena o vacía). En esta cola se nos creará un job adicional, para el caso de las invocaciones multiples, que consistirá en realizar la suma de los resultados de todos los jobs que teniamos en esta cola de request.
El worker (worker.py) se encarga de realizar las peticiones. Este mirará en la cola si hay jobs disponibles. En caso de que los haya, este realizará el job (que puede ser countWords o enumerateWords) cogiendo los datos de la URL especificada. Una vez finalizado el job, encolará el resultado en la cola de request. También puede realizar el job de sumar todos los resultados de una invocación multiple. El worker que realice este job será el que enviará el mensaje al cliente. (para invocación simple será el worker que realice el job). 

Ejecución:
Antes de ejecutar el proyecto, hay que tener ejecutando: redis-server(para el almacenamiento), server http(contiene ciertos ficheros que podemos obtener haciendo peticiones http) y master.py(que es el manager de todas las peticiones que llegan de los clientes y de los workers). 

Las peticiones se ejecutan con el fichero client.py, y para que estas comienzen a ejecutarse debemos tener al menos 1 worker. En caso de no tener workers, el programa se quedará esperando sin devolver una respuesta.
En caso de llamar al client sin parametros, se activa el help automaticamente mostrando las acciones que puede realizar este. 

Por ejemplo:
#Creamos el worker
Python3 client.py -o worker -f workerCreate
#Ejecutamos una petición de contar palabras
Python3 client.py -o job -f countWords http://localhost:80/files/sample1.txt
#Ejecutamos una petición de enumerar palabras
Python3 client.py -o job -f wordCount http://localhost:80/files/sample1.txt
#Ejecutamos una petición de contar palabras con invocación múltiple
Python3 client.py -o job -f countWords http://localhost:80/files/sample1.txt  http://localhost:80/files/sample2.txt
#Ejecutamos una petición de enumerar palabras con invocación múltiple
Python3 client.py -o job -f wordCount http://localhost:80/files/sample1.txt  http://localhost:80/files/sample2.txt
#Eliminamos un worker
Python3 client.py -o worker -f workerDdelete -a 1
#Listamos todos los workers
Python3 client.py .o worker -f listWorkers
