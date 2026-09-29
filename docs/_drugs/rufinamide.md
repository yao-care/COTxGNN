---
layout: default
title: Rufinamide
parent: Solo Predicción del Modelo (L5)
nav_order: 352
evidence_level: L5
indication_count: 5
---

# Rufinamide
{: .fs-9 }

Nivel de evidencia: **L5** | Indicaciones predichas: **5** 
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

# Rufinamida: De Antiepiléptico (indicación no detallada en el registro) a Síndrome de Epilepsia Relacionada con Infección Febril (FIRES)

---

## Resumen en Una Frase

Rufinamida es un medicamento comercializado en Colombia como tableta recubierta (INOVELON® 400 mg). Su registro sanitario solo indica el nombre del principio activo y no detalla la indicación original. El modelo TxGNN predice que podría ser efectivo para el **síndrome de epilepsia relacionada con infección febril (FIRES)**, pero actualmente hay **0 ensayos clínicos** y **0 publicaciones** que respalden esta dirección.

---

## Resumen Rápido

| Item | Contenido |
|------|------|
| Indicación Original | No especificada en el registro (el texto del registro solo dice "RUFINAMIDA") |
| Nueva Indicación Predicha | Síndrome de epilepsia relacionada con infección febril (FIRES) |
| Puntaje de Predicción TxGNN | 99.57% |
| Nivel de Evidencia | L5 |
| Estado de Mercado en Colombia | ✓ Comercializado |
| Número de Registros Sanitarios | 4 entradas (todas con el mismo número de registro, 20153553) |
| Decisión Recomendada | Hold |

---

## ¿Por qué es Razonable esta Predicción?

Actualmente no se dispone de datos detallados sobre el mecanismo de acción. Según la información conocida, rufinamida es un fármaco antiepiléptico. Por farmacología general (no proviene de los datos suministrados), actúa como modulador de canales de sodio con actividad anticonvulsivante. Mecanísticamente, esto hace plausible un vínculo con una epilepsia refractaria como el FIRES. Este vínculo no está verificado.

Hay una limitación importante. El FIRES se asocia en buena parte con neuroinflamación, y el bloqueo de canales de sodio por sí solo podría no abordarla. La predicción del modelo es entonces una hipótesis de partida, no una conclusión.

Además de FIRES, TxGNN predice otras cuatro indicaciones, todas con puntajes cercanos al 99.4%–99.5% y todas con nivel L5, sin ensayos ni literatura:

- Mioclonías perioral con ausencias.
- Epilepsia fotosensible del lóbulo occipital.
- Epilepsia infantil atípica con puntas centrotemporales.
- Espasmos epilépticos criptogénicos de inicio tardío.

En la epilepsia infantil atípica con puntas centrotemporales, algunos bloqueadores de canales de sodio pueden agravar las crisis. Ese caso requeriría una revisión de seguridad antes de cualquier paso adicional.

---

## Evidencia de Ensayos Clínicos

Actualmente no hay ensayos clínicos relacionados registrados.

---

## Evidencia de Literatura

Actualmente no hay literatura relacionada disponible.

---

## Información de Mercado en Colombia

| Registro Sanitario | Nombre del Producto | Forma Farmacéutica | Indicación Aprobada |
|---------|------|------|-----------|
| 20153553 | INOVELON® 400 MG (BIOTOSCANA FARMA S.A.) | Tableta recubierta | RUFINAMIDA (el registro solo indica el principio activo) |

Los datos traen cuatro entradas idénticas del mismo registro 20153553. Se muestran una sola vez.

---

## Consideraciones de Seguridad

Consultar el prospecto para información de seguridad. No se encontraron interacciones farmacológicas en la consulta realizada.

---

## Conclusión y Próximos Pasos

**Decisión: Hold**

**Justificación:**
La predicción se apoya solo en el puntaje del modelo (nivel L5), sin ensayos clínicos ni literatura. Faltan además los datos de mecanismo de acción y de seguridad, y el mecanismo podría no cubrir la neuroinflamación propia del FIRES.

**Para avanzar se necesita:**
- Obtener el prospecto del INVIMA (advertencias y contraindicaciones) y analizarlo.
- Completar los datos del mecanismo de acción desde DrugBank.
- Confirmar la indicación original aprobada, porque el registro solo muestra el nombre del principio activo.
- Buscar ensayos clínicos y literatura sobre rufinamida en FIRES y en las demás indicaciones predichas.
- Revisar la seguridad antes de considerar la epilepsia infantil atípica con puntas centrotemporales.
## Descargo de responsabilidad

Este contenido es solo con fines de investigación y no constituye asesoramiento médico.
Se requiere validación clínica antes de cualquier aplicación clínica.

---

