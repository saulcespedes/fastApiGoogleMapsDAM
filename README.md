# Guía de Configuración de API de Rutas
Esta guía proporciona los pasos necesarios para configurar y utilizar una API de rutas utilizando FastAPI en el backend y Retrofit en el frontend para Android.

Requisitos Previos
SQL Workbench para instalar la base de datos.
FastAPI y sus dependencias instaladas en el backend.
Retrofit configurado en el proyecto de Android para interactuar con la API.
Pasos de Configuración
1. Instalar la Base de Datos
Utiliza SQL Workbench para instalar la base de datos proporcionada. Asegúrate de tener la base de datos en funcionamiento antes de continuar.

pip install fastapi uvicorn

Una vez que estés en esa carpeta del main.py, simplemente ejecuta el siguiente comando:

bash
Copy code
```
~/.local/bin/uvicorn main:app --reload
```

2. Configurar la Contraseña de la Base de Datos
En el archivo main.py del backend, configura la contraseña de la base de datos para establecer la conexión. Modifica la configuración de la base de datos según sea necesario para reflejar tu entorno local.

python
Copy code
# main.py

PASSWORD = "tu_contrasena"

3. Ejecutar el Servidor API
Abre una terminal en la carpeta que contiene el archivo main.py y ejecuta el siguiente comando para iniciar el servidor de la API:

bash
Copy code
~/.local/bin/uvicorn main:app --reload

4. Definir el Endpoint POST
El endpoint POST para agregar una ubicación está definido en la API. Asegúrate de que la ruta sea coherente con la configuración de tu proyecto.

kotlin
Copy code
```

clase 

data class Missatge(
    val missatge: String
)
class Rutas : ArrayList<Ruta>()
data class Ruta(
    val alumne: String?,
    val descripcio: String,
    var latitud: Double,
    var longitud: Double
) : Parcelable {
    constructor(parcel: Parcel) : this(
        parcel.readString(),
        parcel.readString() ?: "",
        parcel.readDouble(),
        parcel.readDouble()
    )


 fun addRuta(ruta: Ruta): Boolean {
        var resposta: Response<Missatge>? = null
        runBlocking {
            val corrutina = launch {
                resposta = getRetrofit().create(ApiService::class.java)
                    .addUbicacion("saulcespedes", ruta)
            }
            corrutina.join()
        }

        if (resposta?.isSuccessful!!)
            return true
        else {
            Log.d("addProducte", resposta?.code().toString())
            return false
        }
    }


```
5. Dirección Local para Conectarse a la API
En el frontend de Android, utiliza la siguiente dirección para conectarte a la API en el emulador:

kotlin
Copy code
private val urlapi = "http://10.0.2.2:8000/"

6. Función para GET

kotlin
Copy code
```

      fun getAllProductesjordi(): Rutas? {
        var resposta : Response<Rutas>? = null
        runBlocking {
            val corrutina = launch {
                resposta = getRetrofit().create(ApiService::class.java).getAllUbicacions("saulcespedes")
            }
            corrutina.join()
        }
        if (resposta?.isSuccessful!!)
            return resposta!!.body()
        else {
            Log.d("getAllProductes", resposta?.code().toString())
            return null
        }

    }




```
