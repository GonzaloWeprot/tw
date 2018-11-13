->Funcionamiento
----------------

El sistema disparará varios eventos cuando detecte un tweet con la combinación de un @usuario y uno de los #hashtags indicados
Esos datos se almacenan en el archivo hashtags.txt

Se pueden borrar, modificar y consultar esos datos de forma remota a través de un email.
Para ello existen las siguientes instrucciones:

->Borrar los datos actuales
---------------------------
Hay que enviar un email a info@flagbased.com con el asunto:
***borrarGigas***

->Modificar los datos
---------------------
Se sobrescribirán los datos indicados. Para ello es necesario enviar un email a
info@flagbased con el asunto:
***configuraGigasr***
Y en el cuerpo del mensaje hay que escribir los datos en el siguiente formato:
***usuario***hashtag-1***hashtag-2***...***hashtag-n***

Por ejemplo: ***weprot***goodjob***buentrabajo***

El sistema elimina todo lo anterior a los primero tres * y lo posterior a los tres últimos *.
Esto se hace para evitar incluir código HTML que pueda estar dentro del cuerpo del mensaje.
El propio código también añade lo "@" al usuario y pone "#" antes de cada hashtag.

->Consultar los datos actuales
------------------------------
Hay que enviar un email a info@flagbased.com con el asunto:
***consultarGigas***

El sistema devolverá a esta misma dirección el contenido del archivo hashtags.txt.

->Modificar los destinatarios de correo electrónico
---------------------------------------------------
Hay que enviar un email a info@flagbased.com con el asunto:
***mailGigas***

El sistema guardará en correos.txt los nuevos destinatarios y, también, en global.correos
El formato del correo será algo como: ***gonzalo.hernandez@flagbased.com;carlos.royo@flagbased.com***

