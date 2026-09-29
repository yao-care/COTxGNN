---
layout: default
title: Etoricoxib
parent: Solo Predicción del Modelo (L5)
nav_order: 190
evidence_level: L5
indication_count: 10
---

# Etoricoxib
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **10** 
{: .fs-6 .fw-300 }

---

## Índice
{: .no_toc .text-delta }

1. TOC
{:toc}

---

<div id="pharmacist">

## Informe de evaluación farmacéutica

</div>

# Etoricoxib: De Indicación Original No Especificada en el Registro a Trastorno de Migraña

## Resumen en Una Frase

Etoricoxib es un antiinflamatorio que inhibe la enzima COX-2 y está comercializado en Colombia, aunque el registro sanitario disponible no detalla su indicación aprobada.
El modelo TxGNN predice que podría ser efectivo para **trastorno de migraña**, con un puntaje muy alto (99.90%).
Sin embargo, actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta predicción específica, por lo que se trata solo de una hipótesis del modelo.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada (el registro solo indica el nombre del principio activo, "Etoricoxib") |
| Nueva Indicación Predicha | Trastorno de migraña |
| Puntaje de Predicción TxGNN | 99.90% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 20 |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción en la base de datos. Según la información conocida, etoricoxib es un inhibidor selectivo de la COX-2, y mecanísticamente podría ser aplicable a la migraña.

La hipótesis es que al bloquear la COX-2 se reduce la producción de prostaglandinas. Estas participan en la neuroinflamación y en la sensibilización del sistema trigeminovascular, dos procesos asociados con el dolor de la migraña.

Este vínculo es **plausible pero no verificado**. El puntaje del modelo es alto, pero no hay ensayos ni literatura que muestren que etoricoxib funcione en migraña. No se pudo comparar la similitud con la indicación original porque el registro no la especifica.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

El paquete de datos reporta 20 registros. Las filas recibidas corresponden solo a dos números de registro distintos, y cuatro de ellas están repetidas (20219448). Aquí se muestran los dos registros únicos.

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20219448 | XICOX® 60 MG (PROCAPS S.A.) | Tableta recubierta | No especificada (solo figura "Etoricoxib") |
| 20226690 | MEDIKET® 90 MG (FARMET DISTRIBUCIONES S.A.S.) | Tableta recubierta | No especificada (solo figura "Etoricoxib") |

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción para migraña tiene un puntaje alto, pero no cuenta con ningún ensayo ni publicación que la respalde (nivel L5). Además, falta el prospecto de INVIMA, necesario para el primer filtro de seguridad.

**Para avanzar se necesita:**
- Descargar y revisar el prospecto de INVIMA (advertencias y contraindicaciones), que es el requisito bloqueante.
- Obtener los datos del mecanismo de acción desde DrugBank.
- Confirmar la indicación aprobada de cada registro sanitario, ya que el campo solo contiene el nombre del principio activo.
- Buscar ensayos clínicos o estudios específicos de etoricoxib en migraña.
- Como línea alternativa, evaluar la indicación vecina **trastorno de cefalea** (nivel L4). Tiene 5 reportes o series de casos con etoricoxib en cefalea punzante primaria, cefalea tusígena y cefaleas que responden a indometacina, pero ninguno es un ensayo controlado. Uno de esos reportes describe un síndrome de vasoconstricción cerebral reversible posiblemente inducido por etoricoxib, una señal de seguridad que debe evaluarse antes de cualquier desarrollo.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

